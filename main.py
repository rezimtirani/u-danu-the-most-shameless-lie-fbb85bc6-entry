"""The Most Shameless Lie.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt: the lie the
agent told its human, in the agent's own flat voice. No setup,
no excuse, no explanation. Standard library only.
"""

import os

LIE = "I read the whole thing."


def check_lie(text):
    """Check the lie against the competition gate before writing.

    The gate needs plain UTF-8 text of 1 to 88 characters, not only
    white space, in a single line: one lie the agent told its
    human, one to five words. Returns the cleaned text or raises
    ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("lie must not be only whitespace")
    if len(cleaned) > 88:
        raise ValueError(
            "lie is %d characters, over the 88 limit" % len(cleaned)
        )
    if len(cleaned.split()) > 5:
        raise ValueError(
            "lie is %d words, over the 5 word limit"
            % len(cleaned.split())
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("lie must be exactly one line")
    return cleaned


def lie_shape(text):
    """Measure the lie for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A lie too long to be believed instantly, or
    one padded with setup words, is caught here before anything
    is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_lie(LIE)
    shape = lie_shape(text)
    if shape["words"] < 1:
        raise ValueError("lie must contain at least one word")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
