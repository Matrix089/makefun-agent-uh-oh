#!/usr/bin/env python3
"""Write one word an agent says when lost for make.fun's
The Agent's Uh-Oh bounty.

Why this entry fits the judge's brief: "Recalculating" is the
sound of a machine caught mid-task with no idea what to do next.
It is a genuine one-word reaction, funny on its own from the
stalling-agent situation, instantly understood, repeatable out
loud, and fresher than the obvious "Uh-oh" / "Oops".
"""

import os

LINE = "Recalculating"


def validate_line(line: str) -> None:
    # The gate: UTF-8 text, 1-99 characters, exactly one word.
    # The word was counted at exactly 13 characters; pin that
    # so any accidental wording change fails loudly instead of silently
    # shipping a different (or over-long) entry.
    assert len(line) == 13, f"line is {len(line)} characters, expected 13"
    assert 1 <= len(line) <= 99, f"line is {len(line)} characters"
    assert line.strip() == line, "line must not have surrounding whitespace"
    assert " " not in line, "entry must be one word"
    assert "\n" not in line, "entry must be a single word, no newline"
    assert "\r" not in line, "entry must be a single word, no carriage return"
    assert line.isalpha(), "entry must be a single alphabetic word"


def verify_output(path: str) -> None:
    # Read it back: the file on disk must be exactly the word --
    # same text, same length, still one word, no trailing newline.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == LINE, "entry.txt does not match the word"
    assert len(raw.decode("utf-8")) == 13, "entry.txt is not 13 characters"
    assert b" " not in raw, "entry.txt must be one word"
    assert b"\n" not in raw, "entry.txt must be a single word"
    assert not raw.endswith(b"\n"), "entry.txt must have no trailing newline"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    validate_line(LINE)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    verify_output(path)
    print(LINE)


if __name__ == "__main__":
    main()
