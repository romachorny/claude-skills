#!/usr/bin/env python3
"""Wrap every Hebrew or Arabic line in RLE (U+202B) ... PDF (U+202C).

Usage: python rtl_wrap.py < in.txt > out.txt
Empty lines and lines that are only a link are left as they are.
Lines that are already wrapped are not wrapped twice.
"""
import re
import sys

RLE, PDF = "\u202b", "\u202c"
RTL = re.compile(r"[\u0590-\u05FF\u0600-\u06FF]")
LINK_ONLY = re.compile(r"^\s*(https?://\S+|www\.\S+|\S+\.\S+/\S*)\s*$")


def wrap(line: str) -> str:
    body = line.rstrip("\n")
    if not body.strip() or LINK_ONLY.match(body) or not RTL.search(body):
        return body
    if body.startswith(RLE) and body.endswith(PDF):
        return body
    return f"{RLE}{body.strip(RLE + PDF)}{PDF}"


def main() -> None:
    lines = sys.stdin.read().split("\n")
    sys.stdout.write("\n".join(wrap(l) for l in lines))


if __name__ == "__main__":
    main()
