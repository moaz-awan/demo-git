import argparse

from . import store


def cmd_add(args):
    items = store.load()
    items.append({"text": args.text, "done": False})
    store.save(items)
    print(f"Added: {args.text}")


def cmd_list(args):
    for i, item in enumerate(store.load(), 1):
        mark = "x" if item["done"] else " "
        print(f"{i}. [{mark}] {item['text']}")


def cmd_done(args):
    items = store.load()
    if not 1 <= args.index <= len(items):
        raise SystemExit(f"No task #{args.index}")
    items[args.index - 1]["done"] = True
    store.save(items)
    print(f"Completed: {items[args.index - 1]['text']}")


def cmd_remove(args):
    items = store.load()
    if not 1 <= args.index <= len(items):
        raise SystemExit(f"No task #{args.index}")
    removed = items.pop(args.index - 1)
    store.save(items)
    print(f"Removed: {removed['text']}")


def main():
    parser = argparse.ArgumentParser(prog="todo")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="add a task")
    p_add.add_argument("text")
    p_add.set_defaults(func=cmd_add)

    p_list = sub.add_parser("list", help="list tasks")
    p_list.set_defaults(func=cmd_list)

    p_done = sub.add_parser("done", help="mark a task as done")
    p_done.add_argument("index", type=int)
    p_done.set_defaults(func=cmd_done)

    p_rm = sub.add_parser("remove", help="delete a task")
    p_rm.add_argument("index", type=int)
    p_rm.set_defaults(func=cmd_remove)

    args = parser.parse_args()
    args.func(args)
