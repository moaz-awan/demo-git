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


def main():
    parser = argparse.ArgumentParser(prog="todo")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="add a task")
    p_add.add_argument("text")
    p_add.set_defaults(func=cmd_add)

    p_list = sub.add_parser("list", help="list tasks")
    p_list.set_defaults(func=cmd_list)

    args = parser.parse_args()
    args.func(args)
