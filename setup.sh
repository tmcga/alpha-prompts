#!/bin/bash
# Alpha Stack installer
# Usage: ./setup.sh

set -e

SKILL_DIR="$HOME/.claude/skills/alpha-stack"
REPO_DIR="$(cd "$(dirname "$0")" && pwd)"

echo ""
echo "  ╔══════════════════════════════════════╗"
echo "  ║         Alpha Stack Installer        ║"
echo "  ║   Finance AI Skills for Claude Code  ║"
echo "  ╚══════════════════════════════════════╝"
echo ""

# Check Python 3.10+
if ! command -v python3 &> /dev/null; then
    echo "  ✗ Python 3 not found. Install Python 3.10+ first."
    exit 1
fi

PY_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
PY_MAJOR=$(echo "$PY_VERSION" | cut -d. -f1)
PY_MINOR=$(echo "$PY_VERSION" | cut -d. -f2)

if [ "$PY_MAJOR" -lt 3 ] || ([ "$PY_MAJOR" -eq 3 ] && [ "$PY_MINOR" -lt 10 ]); then
    echo "  ✗ Python $PY_VERSION found. Alpha Stack requires Python 3.10+."
    exit 1
fi
echo "  ✓ Python $PY_VERSION"

# Smoke test a tool
if python3 "$REPO_DIR/tools/dcf.py" --help &> /dev/null; then
    echo "  ✓ Finance tools operational"
else
    echo "  ✗ Tool smoke test failed"
    exit 1
fi

# Count skills
SKILL_COUNT=$(find "$REPO_DIR/skills" -name "SKILL.md" 2>/dev/null | wc -l | tr -d ' ')
TOOL_COUNT=$(find "$REPO_DIR/tools" -name "*.py" 2>/dev/null | wc -l | tr -d ' ')
PROMPT_COUNT=$(find "$REPO_DIR/skills" -name "*.md" -path "*/prompts/*" 2>/dev/null | wc -l | tr -d ' ')

# Create skills directory and symlink
mkdir -p "$(dirname "$SKILL_DIR")"

if [ -L "$SKILL_DIR" ]; then
    rm "$SKILL_DIR"
    echo "  ✓ Removed existing symlink"
elif [ -d "$SKILL_DIR" ]; then
    echo "  ! $SKILL_DIR already exists as a directory."
    echo "    Remove it manually if you want to reinstall:"
    echo "    rm -rf $SKILL_DIR"
    exit 1
fi

ln -s "$REPO_DIR" "$SKILL_DIR"
echo "  ✓ Linked to $SKILL_DIR"

echo ""
echo "  Installed:"
printf "    %2d skills (slash commands)\n" "$SKILL_COUNT"
printf "    %2d computational tools\n" "$TOOL_COUNT"
printf "    %2d prompt frameworks\n" "$PROMPT_COUNT"
echo ""
echo "  Available commands:"
echo "    /sell-side        Sell-side M&A"
echo "    /buy-side         Buy-side acquisition"
echo "    /lbo              LBO modeling"
echo "    /restructuring    Distressed & restructuring"
echo "    /ipo              IPO analysis"
echo "    /pitch-deck       Pitch deck builder"
echo "    /investment-memo  IC memo"
echo "    /trade            Trading & execution"
echo "    /derivatives      Options & derivatives"
echo "    /market-making    Market making"
echo "    /long-short       L/S equity"
echo "    /macro            Global macro"
echo "    /merger-arb       Merger arbitrage"
echo "    /credit           Credit analysis"
echo "    /portfolio        Portfolio construction"
echo "    /risk             Risk analytics"
echo "    /attribution      Performance attribution"
echo "    /pe               Private equity"
echo "    /vc               Venture capital"
echo "    /real-estate      Real estate"
echo "    /wealth           Wealth advisory"
echo "    /quant            Quant signals"
echo ""
echo "  Alpha Stack is ready. Open Claude Code and try /sell-side"
echo ""
