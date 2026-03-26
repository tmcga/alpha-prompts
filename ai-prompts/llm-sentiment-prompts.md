# LLM Sentiment Strategy Prompts

Prompt architecture for building an LLM-powered sentiment strategy that classifies market text into trading signals.

## Overview

The LLM sentiment strategy maps text data (news headlines, social media, analyst reports) to directional signals: **long (+1)**, **short (-1)**, or **neutral (0)**. The prompts below show how to build it.

## Classification Prompt

The core prompt for single-headline classification:

```
You are a quantitative trading signal generator. Your job is to classify market-relevant text into a directional signal.

Analyze the following text about {asset}:

"{headline}"

Classify the sentiment as exactly one of:
- BULLISH: the text suggests price is likely to increase
- BEARISH: the text suggests price is likely to decrease
- NEUTRAL: the text is ambiguous, irrelevant, or has no clear directional implication

Respond with ONLY one word: BULLISH, BEARISH, or NEUTRAL.
```

Map the response: `BULLISH -> +1`, `BEARISH -> -1`, `NEUTRAL -> 0`.

## Batch Classification Prompt

For efficiency, classify multiple headlines in a single API call:

```
You are a quantitative trading signal generator. Classify each headline's sentiment for {asset}.

For each headline, respond with exactly one of: BULLISH, BEARISH, NEUTRAL.

Headlines:
1. "{headline_1}"
2. "{headline_2}"
3. "{headline_3}"
...
N. "{headline_n}"

Respond with ONLY a numbered list of classifications, one per line:
1. [BULLISH/BEARISH/NEUTRAL]
2. [BULLISH/BEARISH/NEUTRAL]
...
```

## Confidence-Weighted Prompt

For more nuanced signals with position sizing:

```
You are a quantitative trading signal generator. Analyze the following text about {asset} and provide a sentiment score.

"{headline}"

Respond with a JSON object:
{
  "signal": "BULLISH" | "BEARISH" | "NEUTRAL",
  "confidence": 0.0 to 1.0,
  "reasoning": "one sentence explanation"
}

Guidelines:
- confidence 0.8-1.0: strong, unambiguous signal (major earnings beat, Fed rate decision)
- confidence 0.5-0.8: moderate signal (analyst upgrade, sector rotation)
- confidence 0.0-0.5: weak or ambiguous signal
- Use NEUTRAL for anything not clearly directional
```

Map to position: `signal_value * confidence` (e.g., BULLISH with 0.7 confidence = +0.7 position).

## Implementation Notes

To build a sentiment strategy using these prompts:

1. **Data requirement**: Your DataFrame needs a text column (e.g., `headline`, `news_text`). This is passed via `text_col` parameter.

2. **API calls**: Use the `anthropic` Python SDK. Batch headlines to reduce API calls — one call per bar is expensive.

3. **Caching**: Cache sentiment results by headline hash to avoid re-classifying identical text.

4. **Rate limits**: Anthropic API has rate limits. For backtesting, pre-classify all headlines before running the backtest.

5. **Model selection**: Use `claude-haiku-4-5-20251001` for classification (fast, cheap). Reserve larger models for complex analysis.

```python
# Example implementation sketch
import anthropic

client = anthropic.Anthropic()  # uses ANTHROPIC_API_KEY env var

def classify_headline(headline: str, asset: str) -> int:
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=10,
        messages=[{
            "role": "user",
            "content": f'Classify sentiment for {asset}: "{headline}"\nRespond with ONLY: BULLISH, BEARISH, or NEUTRAL.'
        }]
    )
    text = response.content[0].text.strip().upper()
    return {"BULLISH": 1, "BEARISH": -1}.get(text, 0)
```

## Data Sources for Text

To use this strategy, you need a text data feed. Options:

- **News APIs**: NewsAPI, Polygon.io news, Alpha Vantage news sentiment
- **Social media**: Reddit (via PRAW), Twitter/X API, StockTwits
- **Filings**: SEC EDGAR (10-K, 8-K), earnings call transcripts
- **Free options**: RSS feeds from financial news sites, CryptoPanic API (crypto news)
