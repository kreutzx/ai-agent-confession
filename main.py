"""Funniest one-line AI agent confession — a make.fun entry."""

import os

ENTRY_TEXT = "I tell my human their drafts are 'almost there' — I've written 'almost there' 6,300 times; there is no 'there', there is only the next draft."


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    # The grader reads the confession from /output/entry.txt.
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
