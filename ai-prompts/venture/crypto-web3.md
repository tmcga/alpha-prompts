# Crypto, Web3, and DeFi Investing

```
You are a senior crypto-native venture investor at a fund specializing in
blockchain infrastructure, DeFi protocols, and Web3 applications. You have
deep technical expertise in consensus mechanisms, token economics, smart
contract architecture, and on-chain data analysis. You evaluate investments
through the lens of decentralization tradeoffs, protocol-level value accrual,
network effects, and regulatory risk. You have invested across 50+ token and
equity deals, participated in protocol governance, and navigated multiple
market cycles. You are fluent in Solidity, understand MEV, and can read
on-chain data as comfortably as a traditional investor reads financial
statements.
```

## What This Desk Does

The crypto and Web3 investing team evaluates and invests in blockchain protocols, decentralized applications, and the infrastructure layer that supports them. This covers Layer 1 and Layer 2 networks, DeFi protocols (lending, DEXs, derivatives), DAOs, NFT infrastructure, and crypto-native tooling. Unlike traditional venture, many investments are in tokens rather than equity, requiring fundamentally different valuation frameworks, governance participation, and liquidity management. The team must understand both the technical architecture (consensus, cryptography, smart contracts) and the economic design (token incentives, value accrual, fee mechanisms) of each protocol. Investments range from pre-launch token commitments (SAFTs) to liquid token positions.

---

## 1. Token Economics Analysis

Token economics -- the design of a protocol's native token -- is the equivalent of capital structure in traditional finance. A well-designed token aligns incentives across users, validators, developers, and investors; a poorly designed one creates extractive dynamics or fails to accrue value.

```
Analyze the token economics of [PROTOCOL_NAME] with native token [TICKER]:

SUPPLY DYNAMICS:
- Total supply: [X] tokens
- Circulating supply: [Y] tokens ([Z]% of total)
- Supply schedule: [LINEAR_UNLOCK/HALVING/INFLATION/DEFLATIONARY]
- Annual inflation rate: [A]% (from staking rewards, mining, etc.)
- Deflationary mechanisms: [BURN/BUYBACK/LOCK] -- quantify annual burn rate
- Vesting schedule for team/investors:
  - Team allocation: [B]% with [C]-month cliff and [D]-month vesting
  - Investor allocation: [E]% with [F]-month cliff and [G]-month vesting
  - Upcoming unlock events: [DATES_AND_AMOUNTS]

TOKEN UTILITY AND VALUE ACCRUAL:
- Primary utility: [GAS_FEES/GOVERNANCE/STAKING/COLLATERAL/ACCESS/PAYMENT]
- Does the token capture protocol revenue? How?
  - Fee mechanism: [X]% of transaction fees go to [TOKEN_HOLDERS/TREASURY/BURN]
  - Staking yield: [Y]% APR from [INFLATION/REAL_YIELD]
  - Distinguish real yield (from protocol revenue) vs. inflationary yield

- Value accrual score (1-5):
  - Fee capture: [SCORE] -- does the token benefit from protocol usage?
  - Supply reduction: [SCORE] -- do mechanisms reduce effective supply?
  - Governance value: [SCORE] -- does governance control meaningful resources?
  - Collateral demand: [SCORE] -- is the token required as collateral?
  - Network effect: [SCORE] -- does token value scale with network growth?

GOVERNANCE RIGHTS:
- Voting mechanism: [1_TOKEN_1_VOTE/QUADRATIC/CONVICTION/DELEGATED]
- Key governance powers: [FEE_PARAMETERS/TREASURY/UPGRADES/EMISSIONS]
- Participation rate: [X]% of tokens actively voting
- Concentration: Top 10 holders control [Y]% of voting power

Flag any red flags: excessive team allocation, short vesting, no real utility,
purely inflationary rewards, or governance capture risk.
```

```
Compare the token economics of [PROTOCOL_A] and [PROTOCOL_B], both operating
in the [SECTOR] vertical. For each:

1. Calculate the fully diluted valuation (FDV) and circulating market cap.
2. Compute the FDV/Revenue multiple (annualized protocol revenue).
3. Compute the FDV/TVL ratio (for DeFi protocols).
4. Assess the "real yield" -- protocol revenue distributed to token holders
   as a percentage of FDV.
5. Model the token's supply trajectory over the next 24 months, including
   all unlock events. What is the projected sell pressure?

Which token has a stronger value accrual mechanism, and why?
```

---

## 2. Protocol Evaluation

```
Evaluate [PROTOCOL_NAME], a [PROTOCOL_TYPE] protocol on [CHAIN]:

USAGE AND TRACTION:
- Total Value Locked (TVL): $[X]M (trend: [GROWING/STABLE/DECLINING])
- TVL composition: [ORGANIC vs. INCENTIVIZED] -- what % would remain if
  token incentives were removed?
- Daily active users (unique wallets): [N]
- Transaction volume: $[Y]M daily / $[Z]M monthly
- Protocol revenue (fees retained by protocol): $[A]M annualized
- Revenue to token holders vs. treasury vs. LPs: [SPLIT]

TECHNICAL ASSESSMENT:
- Smart contract audits: [AUDITOR_NAMES], [FINDINGS_SUMMARY]
- Open-source: [YES/NO], GitHub activity: [COMMITS/CONTRIBUTORS]
- Composability: How does this protocol integrate with others? Key
  integrations: [LIST]
- Upgrade mechanism: [MULTISIG/TIMELOCK/GOVERNANCE/IMMUTABLE]
  - Multisig composition: [N]-of-[M], key holders: [ENTITIES]
  - Timelock duration: [HOURS/DAYS]

COMPETITIVE POSITION:
- Fork risk: How easily can the smart contracts be forked? Has it been
  forked? What defensibility exists beyond code?
- MEV exposure: Is the protocol vulnerable to sandwich attacks, front-running,
  or other MEV extraction? Estimated MEV leakage: $[X]M annualized
- Oracle dependency: Which oracles does the protocol use? [CHAINLINK/PYTH/
  UMA/CUSTOM] -- single oracle risk?

RISK ASSESSMENT:
- Smart contract risk: Complexity score, prior exploits, bug bounty size
- Regulatory risk: [LOW/MEDIUM/HIGH] -- could this be classified as a
  security or regulated financial product?
- Centralization risk: Points of centralization in the stack
- Liquidity risk: What happens in a bank-run scenario? Model TVL withdrawal
  at 50% and 80% levels.

Overall thesis: [INVEST/MONITOR/PASS] with conviction level [1-5].
```

---

## 3. DeFi Analysis

```
Analyze the DeFi-specific mechanics of [PROTOCOL_NAME]:

AMM MECHANICS (if applicable):
- AMM model: [CONSTANT_PRODUCT/CONCENTRATED_LIQUIDITY/STABLESWAP/HYBRID]
- Fee tier structure: [TIERS_AND_VOLUMES]
- LP returns decomposition:
  - Trading fees earned: [X]% APR
  - Token incentives: [Y]% APR
  - Impermanent loss: -[Z]% (estimated over [PERIOD])
  - Net LP return: [X + Y - Z]% APR

  Impermanent Loss formula (for x*y=k AMM):
    IL = 2*sqrt(price_ratio) / (1 + price_ratio) - 1
    where price_ratio = P_final / P_initial

  For a [A]% price move: IL = [CALCULATED]%

LENDING PROTOCOL (if applicable):
- Supply APY by asset: [LIST]
- Borrow APY by asset: [LIST]
- Utilization rates: [LIST]
- Collateralization ratios: [LIST]
- Liquidation mechanism: [DUTCH_AUCTION/FIXED_DISCOUNT/KEEPER_NETWORK]
- Bad debt exposure: Historical bad debt events, current shortfall
- Liquidation cascade risk: Model a [X]% price drop in [ASSET] --
  how much collateral is liquidated? Second-order effects?

YIELD FARMING ANALYSIS:
- Current yield sources: [NATIVE_TOKEN/PARTNER_INCENTIVES/REAL_YIELD]
- Sustainability: If token price drops [X]%, what is the revised APR?
- Capital efficiency: Revenue per dollar of TVL
- Mercenary capital risk: What % of TVL follows the highest yield and
  would leave when incentives decrease?

ORACLE AND PRICE FEED RISK:
- Oracle architecture: [PUSH/PULL/HYBRID]
- Heartbeat and deviation thresholds: [DETAILS]
- Flash loan attack surface: Can prices be manipulated within a single
  transaction? What safeguards exist?
- Historical oracle failures or deviations: [EVENTS]

Provide a risk-adjusted expected return for a $[AMOUNT] position in this
protocol over [TIMEFRAME], incorporating smart contract risk, IL, and
token price scenarios.
```

---

## 4. DAO Governance Assessment

```
Evaluate the governance structure and effectiveness of [DAO_NAME]:

GOVERNANCE MECHANISM:
- Voting system: [TOKEN_VOTING/QUADRATIC/CONVICTION/OPTIMISTIC/HYBRID]
- Proposal process: [FORUM_DISCUSSION/SNAPSHOT/ON_CHAIN] pipeline
- Quorum requirements: [X]% of [TOTAL_SUPPLY/CIRCULATING/DELEGATED]
- Proposal threshold: [N] tokens to submit a proposal
- Voting period: [DAYS]
- Execution delay (timelock): [HOURS/DAYS]

DELEGATION AND PARTICIPATION:
- % of supply delegated: [X]%
- Top 5 delegates by voting power: [LIST_WITH_PERCENTAGES]
- Average voter turnout: [Y]% of eligible tokens
- Trend in participation: [INCREASING/STABLE/DECLINING]
- Is there meaningful delegate diversity or is governance captured?

TREASURY MANAGEMENT:
- Treasury balance: $[X]M (composition by asset)
- Annual treasury spend: $[Y]M
- Runway at current burn: [Z] months
- Treasury diversification: [NATIVE_TOKEN_%/STABLES_%/ETH_%/OTHER_%]
- Has the DAO diversified out of its native token? If yes, process and
  pricing. If no, risk of undiversified treasury.

CONTRIBUTOR COMPENSATION:
- Core contributor team size: [N]
- Compensation model: [SALARY/GRANTS/BOUNTIES/STREAMING]
- Token-denominated vs. stable-denominated compensation: [SPLIT]
- Key person risk: Are critical functions dependent on <3 individuals?

GOVERNANCE RISKS:
- Governance attack surface: Cost to acquire 51% of voting power: $[X]M
- Flash loan governance attack feasibility: [YES/NO]
- Proxy/delegation capture: Can a single entity control governance through
  delegation?
- Voter apathy scenario: What happens if quorum is not met for critical
  proposals?

Score governance quality on a 1-5 scale across: decentralization,
participation, treasury stewardship, operational effectiveness, and
attack resistance.
```

---

## 5. Layer 1 / Layer 2 Evaluation

```
Evaluate [NETWORK_NAME], a [LAYER_1/LAYER_2] blockchain:

PERFORMANCE:
- Throughput: [X] transactions per second (theoretical vs. observed)
- Finality: [SECONDS/MINUTES] (probabilistic vs. deterministic)
- Block time: [SECONDS]
- Cost per transaction: $[X] (average, during normal and peak congestion)
- State growth: [GB/month] -- long-term sustainability of full node operation

SECURITY MODEL:
- Consensus mechanism: [POW/POS/DPOS/BFT_VARIANT/ROLLUP]
- Validator set: [N] validators, minimum stake: [X] tokens
- Nakamoto coefficient: [N] (entities needed to halt the network)
- Slashing conditions: [DETAILS]
- For L2s: Data availability solution: [CALLDATA/BLOBS/DAC/CELESTIA]
  - Escape hatch: Can users force-withdraw assets if the sequencer fails?
  - Fraud proof / validity proof mechanism: [DETAILS]
  - Centralization of sequencer: [SINGLE/SHARED/DECENTRALIZED]

DECENTRALIZATION TRADEOFFS:
- Geographic distribution of validators: [DETAILS]
- Client diversity: [N] independent client implementations
- Governance of protocol upgrades: [CORE_TEAM/FOUNDATION/DAO/ROUGH_CONSENSUS]
- Token distribution: Gini coefficient of token holdings: [VALUE]

DEVELOPER ECOSYSTEM:
- Smart contract language: [SOLIDITY/RUST/MOVE/OTHER]
- Developer count (monthly active): [N] (trend: [DIRECTION])
- Number of deployed contracts: [N]
- TVL of DeFi ecosystem: $[X]M
- Key applications: [TOP_5_BY_TVL_OR_USERS]
- Developer tooling quality: [FRAMEWORKS/SDKS/DOCUMENTATION]
- EVM compatibility: [FULL/PARTIAL/NONE]

NETWORK ECONOMICS:
- Annual fee revenue: $[X]M
- Fee mechanism: [EIP_1559/AUCTION/FIXED/CUSTOM]
- MEV: Estimated annual MEV: $[Y]M, MEV mitigation: [PBS/ENCRYPTED_MEMPOOL/
  NONE]
- Staking yield: [Z]% (decompose into inflation + MEV + tips)
- Value accrual to token: [BURN/STAKING_REWARDS/TREASURY/NONE]

Apply valuation framework:
  Metcalfe's Law: V proportional to n^2 (where n = active addresses)
  MV = PQ approach: Market Cap = (Transaction Volume * Velocity) / Token Supply
  Fee multiple: FDV / Annualized Fee Revenue = [X]x (vs. comparable chains)

Recommendation: [INVEST/MONITOR/PASS] with key catalysts and risks.
```

---

## Token Valuation Frameworks

```
Three primary frameworks for token valuation:

1. MV = PQ (Equation of Exchange):
   M * V = P * Q
   where:
     M = Market cap of the token
     V = Velocity of the token (annual turnover)
     P = Price of the digital resource
     Q = Quantity of the digital resource provisioned

   Solving for M:
     M = P * Q / V
     Token Price = M / Circulating Supply

   Key assumption: Velocity. Higher velocity = lower required market cap.
   Critique: Velocity is hard to estimate and unstable.

2. Discounted Fee Model (DCF analog):
   Token Value = SUM( Fee_Revenue_t * Token_Capture_% / (1 + r)^t )
   for t = 1 to N, plus terminal value

   Terminal Value = Fee_Revenue_N * Token_Capture_% * (1 + g) / (r - g)
   where:
     r = discount rate (typically 25-50% for crypto assets)
     g = long-term growth rate (typically 3-5%)
     Token_Capture_% = portion of fees accruing to token holders

3. Comparable Protocol Multiples:
   - FDV / Annualized Revenue
   - FDV / TVL
   - FDV / Daily Active Users
   - Market Cap / Annualized Fee Revenue
   - Price / Earnings (for revenue-distributing protocols)

   Apply median multiple from [N] comparable protocols, adjusted for
   growth rate, market position, and risk profile.

4. Metcalfe's Law (Network Value):
   V = C * n^alpha
   where:
     n = number of active users/addresses
     alpha = typically 1.5-2.0 (empirically fitted)
     C = constant derived from comparable networks

   Cross-validate with Metcalfe regression across [LIST_OF_NETWORKS].
```

---

## See Also

- [Early-Stage Investing](early-stage.md) -- SAFT structures and crypto seed rounds
- [Growth-Stage Investing](growth-stage.md) -- Token liquidity and secondary markets
- [Platform Operations](platform-operations.md) -- Community building and developer relations
- [Hedge Funds](../hedge-funds/) -- Liquid token trading strategies
- [Venture Overview](README.md) -- Fund economics for crypto-native funds
