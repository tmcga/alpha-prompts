#!/bin/bash
# Alpha Stack MCP Server installer for Claude Desktop
# Usage: ./setup-mcp.sh
set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
CONFIG_FILE="$HOME/Library/Application Support/Claude/claude_desktop_config.json"

echo ""
echo "  ╔══════════════════════════════════════╗"
echo "  ║   Alpha Stack MCP Server Installer   ║"
echo "  ║      Finance Tools for Claude        ║"
echo "  ╚══════════════════════════════════════╝"
echo ""

# 1. Check for uv
if ! command -v uv &> /dev/null; then
    echo "  Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
fi
echo "  ✓ uv available"

# 2. Install MCP dependency
cd "$REPO_DIR"
uv sync --quiet
echo "  ✓ MCP SDK installed"

# 3. Smoke test — verify imports work
if uv run python -c "
import sys, os
sys.path.insert(0, os.path.join('$REPO_DIR', 'tools'))
from dcf import dcf_valuation
from mcp.server.fastmcp import FastMCP
" 2>/dev/null; then
    echo "  ✓ Server imports verified"
else
    echo "  ✗ Import verification failed"
    exit 1
fi

# 4. Update Claude Desktop config
export REPO_DIR
python3 << 'PYEOF'
import json, os

repo_dir = os.environ["REPO_DIR"]
config_path = os.path.expanduser("~/Library/Application Support/Claude/claude_desktop_config.json")
config = {}
if os.path.exists(config_path):
    with open(config_path) as f:
        config = json.load(f)

if "mcpServers" not in config:
    config["mcpServers"] = {}

config["mcpServers"]["alpha-stack"] = {
    "command": "uv",
    "args": ["run", "--directory", repo_dir, "python", "mcp_server.py"]
}

os.makedirs(os.path.dirname(config_path), exist_ok=True)
with open(config_path, "w") as f:
    json.dump(config, f, indent=2)

print("  ✓ Claude Desktop config updated")
PYEOF

echo ""
echo "  23 finance tools registered as MCP tools."
echo "  Restart Claude Desktop to activate."
echo ""
echo "  Try asking Claude:"
echo "    'What is the DCF value for FCFs of 100, 110, 121"
echo "     with 10% WACC and 2.5% terminal growth?'"
echo ""
