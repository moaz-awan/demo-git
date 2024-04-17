from todo import store


def test_load_missing_file(tmp_path):
    assert store.load(tmp_path / "none.json") == []


def test_roundtrip(tmp_path):
    path = tmp_path / "todos.json"
    items = [{"text": "a", "done": False}]
    store.save(items, path)
    assert store.load(path) == items
