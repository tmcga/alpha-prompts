#!/usr/bin/env python3
"""Session state — save and load analysis results for iterative workflows.

Usage: python state.py --save myanalysis --data '{"irr": 0.24}'
       python state.py --load myanalysis
       python state.py --list
       python state.py --delete myanalysis
"""

import argparse
import json
import os
from datetime import datetime

STATE_DIR = os.path.join(os.path.expanduser("~"), ".alpha-stack", "sessions")


def _ensure_dir():
    os.makedirs(STATE_DIR, exist_ok=True)


def _path(name: str) -> str:
    safe = "".join(c if c.isalnum() or c in "-_." else "_" for c in name)
    return os.path.join(STATE_DIR, f"{safe}.json")


def save_session(name: str, data: dict, tags: list[str] | None = None) -> dict:
    """Save analysis results to a named session file.

    Args:
        name: Session name (e.g., 'techcorp-lbo', 'q4-attribution').
        data: Any dict — typically the output of a tool function.
        tags: Optional tags for filtering (e.g., ['lbo', 'cybervault']).

    Returns:
        Dict confirming save with path and metadata.
    """
    _ensure_dir()
    envelope = {
        "name": name,
        "saved_at": datetime.now().isoformat(),
        "tags": tags or [],
        "data": data,
    }
    path = _path(name)
    with open(path, "w") as f:
        json.dump(envelope, f, indent=2, default=str)
    return {"status": "saved", "name": name, "path": path, "saved_at": envelope["saved_at"]}


def load_session(name: str) -> dict:
    """Load a previously saved session by name.

    Args:
        name: Session name to load.

    Returns:
        The full envelope (name, saved_at, tags, data) or error.
    """
    path = _path(name)
    if not os.path.exists(path):
        return {"error": f"Session '{name}' not found", "path": path}
    with open(path) as f:
        return json.load(f)


def list_sessions() -> dict:
    """List all saved sessions with metadata.

    Returns:
        Dict with list of sessions (name, saved_at, tags, path).
    """
    _ensure_dir()
    sessions = []
    for fname in sorted(os.listdir(STATE_DIR)):
        if not fname.endswith(".json"):
            continue
        path = os.path.join(STATE_DIR, fname)
        try:
            with open(path) as f:
                env = json.load(f)
            sessions.append(
                {
                    "name": env.get("name", fname),
                    "saved_at": env.get("saved_at", "unknown"),
                    "tags": env.get("tags", []),
                    "path": path,
                }
            )
        except (json.JSONDecodeError, KeyError):
            sessions.append({"name": fname, "saved_at": "error", "tags": [], "path": path})
    return {"sessions": sessions, "count": len(sessions), "directory": STATE_DIR}


def delete_session(name: str) -> dict:
    """Delete a saved session by name.

    Args:
        name: Session name to delete.

    Returns:
        Dict confirming deletion or error.
    """
    path = _path(name)
    if not os.path.exists(path):
        return {"error": f"Session '{name}' not found"}
    os.remove(path)
    return {"status": "deleted", "name": name, "path": path}


def main():
    parser = argparse.ArgumentParser(description="Session State Manager")
    parser.add_argument("--save", type=str, metavar="NAME", help="Save session with this name")
    parser.add_argument("--data", type=str, help="JSON data to save (with --save)")
    parser.add_argument("--tags", type=str, help="Comma-separated tags (with --save)")
    parser.add_argument("--load", type=str, metavar="NAME", help="Load session by name")
    parser.add_argument("--list", action="store_true", help="List all saved sessions")
    parser.add_argument("--delete", type=str, metavar="NAME", help="Delete session by name")
    args = parser.parse_args()

    if args.list:
        r = list_sessions()
        print(f"\n{'=' * 55}")
        print(f"  Saved Sessions ({r['count']})")
        print(f"{'=' * 55}")
        if not r["sessions"]:
            print("  (none)")
        for s in r["sessions"]:
            tags = f" [{', '.join(s['tags'])}]" if s["tags"] else ""
            print(f"  {s['name']:<25s}  {s['saved_at'][:19]}{tags}")
        print(f"{'=' * 55}")
        print(f"  Directory: {r['directory']}")
        print()
    elif args.save:
        if not args.data:
            parser.error("--save requires --data '<json>'")
        data = json.loads(args.data)
        tags = [t.strip() for t in args.tags.split(",")] if args.tags else None
        r = save_session(args.save, data, tags)
        print(f"  Saved: {r['name']} -> {r['path']}")
    elif args.load:
        r = load_session(args.load)
        if "error" in r:
            print(f"  Error: {r['error']}")
        else:
            print(json.dumps(r, indent=2, default=str))
    elif args.delete:
        r = delete_session(args.delete)
        if "error" in r:
            print(f"  Error: {r['error']}")
        else:
            print(f"  Deleted: {r['name']}")
    else:
        parser.error("Provide --save, --load, --list, or --delete")


if __name__ == "__main__":
    main()
