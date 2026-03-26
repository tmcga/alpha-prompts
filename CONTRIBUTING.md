# Contributing to Alpha Stack

Alpha Stack is built on three types of contributions: **skills**, **prompts**, and **tools**.

## Adding a Prompt

Prompts live inside skill directories at `skills/<skill-name>/prompts/`.

1. Identify which skill your prompt belongs to (see the 26 skills in README.md)
2. Create a new `.md` file in that skill's `prompts/` directory
3. Follow this template:
   - **Role context** — AI persona in a code fence (4-8 sentences)
   - **"What this desk does"** — 3-5 sentence overview
   - **3-6 workflow sections** with prompt templates using `[bracket]` placeholders
   - **Mathematical frameworks** inline where they add value
   - **"See also"** links to related skills
4. Open a PR

## Adding a Tool

Tools live in `tools/` and must follow strict conventions:

1. **Standalone** — Python stdlib only, no external dependencies
2. **Dual-mode** — CLI with `argparse` AND importable as a module
3. **Under 200 lines**
4. **Python 3.10+**
5. **ASCII table output** — formatted, readable terminal output
6. Update `tools/README.md` with your new tool
7. Open a PR

## Adding a Skill

Skills are the highest-level contribution. Each skill is a directory with:

```
skills/<skill-name>/
├── SKILL.md          # Skill definition (frontmatter + workflows)
└── prompts/          # Related prompt files
```

A SKILL.md file must include:
- **Frontmatter** with `name` and `description` (trigger conditions)
- **What I Do** — capabilities summary
- **Available Tools** — table mapping tools to use cases
- **Workflows** — step-by-step analysis procedures
- **Role Context** — the expert persona
- **Related Skills** — links to other skills

## General Guidelines

- Keep content practical — real frameworks, not textbook summaries
- Include mathematical formulas where they add analytical value
- Use bracket placeholders `[like this]` for user-specific inputs
- Reference existing skills and tools rather than duplicating
- Test all Python tools before submitting
- Follow the Source > Diligence > Model > Stress > Decide > Monitor workflow

## Questions?

Open an issue on GitHub.
