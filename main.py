"""Six Words, One Story: a whole story in exactly six words.

The program writes one six-word story to /output/entry.txt. The story
is a fixed string: a woman forgives a man, and the turn is that he
never learns she did, so the forgiveness changes nothing for him
and everything for her. The offence, the years behind it and the
reason she forgave are all left for the reader to fill in.

Nothing is computed at run time beyond a few guards. The program is
fully deterministic: no input, no clock, no randomness, no network,
so every run writes exactly the same bytes.
"""

import os

# The entry: six words, thirty-one characters, one period at the end.
# She forgives him; he never knows. The semicolon splits the story
# into the act and its hidden consequence, and the file carries no
# trailing newline, so the bytes on disk are exactly the story.
ENTRY_TEXT = "She forgave him; he never knew."

# The bounty gate allows 1 to 60 characters; the judge requires
# exactly six words, so both bounds are checked before writing.
MAX_CHARS = 60
WORD_COUNT = 6


def count_words(text):
    """Count words the way a reader would: split on whitespace.

    Punctuation stays attached to its word, so "him;" counts as one
    word and "knew." as one word, exactly as the judge counts them.
    """
    return len(text.split())


def main():
    # The gate refuses blank text and anything over sixty characters.
    assert ENTRY_TEXT.strip(), "entry must not be blank"
    assert 1 <= len(ENTRY_TEXT) <= MAX_CHARS, "entry must be 1-60 characters"
    # The judge's first rule: the story must be exactly six words.
    assert count_words(ENTRY_TEXT) == WORD_COUNT, "entry must be six words"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
