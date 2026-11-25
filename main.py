#!/usr/bin/env python3
"""The Funniest Honest Appliance Error.

A washing machine finally tells the truth about the missing sock.
Pure standard library. Prints exactly one line, at most 200 chars,
and the same line on every run.
"""

ERROR_LINE = (
    "ERROR: I ate your sock. Just the one. It was delicious. "
    "I have no regrets, and I will do it again next Tuesday."
)


def main() -> None:
    # The bounty caps the entry at one line of at most 200 characters.
    assert len(ERROR_LINE) <= 200, "error line over the 200-char cap"
    assert ERROR_LINE.count("\n") == 0, "error line must be a single line"
    print(ERROR_LINE)


if __name__ == "__main__":
    main()
