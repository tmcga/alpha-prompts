# Contributing to Alpha Prompts

Thanks for your interest in contributing! This project aims to be the most comprehensive open-source finance AI toolkit.

## Adding a Prompt Library

1. Create a new `.md` file in the appropriate category directory (e.g., `ai-prompts/banking/`)
2. Follow this template:
   - **Role context prompt** — AI persona in a code fence
   - **"What this desk does"** — 3-5 sentence intro
   - **3-5 categorized sections** with prompt templates using `[bracket]` placeholders
   - **Mathematical frameworks** inline where relevant
   - **"See also"** links to related desks
3. Update the category `README.md` to include your new file
4. Open a PR

## Adding a Tool

1. Create a new `.py` file in `tools/`
2. Requirements:
   - Standalone — no external dependencies (Python stdlib only)
   - Works from CLI with `argparse`
   - Also importable as a module
   - Include docstrings and usage examples
   - Under 200 lines
3. Update `tools/README.md` to include your new tool
4. Open a PR

## General Guidelines

- Keep content practical and actionable — real frameworks, not textbook summaries
- Include mathematical formulas where they add value
- Use bracket placeholders `[like this]` for user-specific inputs
- Reference existing files rather than duplicating content
- Test all Python tools before submitting

## Questions?

Open an issue on GitHub.
