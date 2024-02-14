import json
from pathlib import Path

DEFAULT_PATH = Path("todos.json")


def load(path=DEFAULT_PATH):
    if not path.exists():
        return []
    return json.loads(path.read_text())


def save(items, path=DEFAULT_PATH):
    path.write_text(json.dumps(items, indent=2))
