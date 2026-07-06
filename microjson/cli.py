import json
import os
import sys

def banner():
    print()
    print("MicroJSON")
    print("=" * 40)

def usage():
    print("Usage:")
    print("  python3 -m microjson <file.json>")

def main():
    args = sys.argv[1:]

    banner()

    if len(args) != 1:
        usage()
        return

    filename = args[0]

    if not os.path.isfile(filename):
        print("File not found:", filename)
        return

    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        print("Status : VALID JSON")
        print("File   :", filename)
        print()

        print(json.dumps(data, indent=4, sort_keys=True))

    except json.JSONDecodeError as e:
        print("Status : INVALID JSON")
        print(e)
