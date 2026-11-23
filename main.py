#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes a single surprising, vivid word to /output/entry.txt.
Pure standard library, no network, no input.
"""

import os

WORD = "borborygmus"
# Word choice: "borborygmus" is the low, rumbling sound a hungry stomach
# makes — the word itself growls. It is surprising (few readers would guess
# it), vivid and specific (one unmistakable bodily sound), witty in its
# onomatopoeic bounce, and chosen rather than generic: no filler word could
# call up this image. 11 letters, well inside the 1-24 gate.


def main() -> None:
    word = WORD
    # Gate: 1-24 characters, exactly one word, no surrounding whitespace.
    assert isinstance(word, str)
    assert 1 <= len(word) <= 24, f"word length {len(word)} outside 1-24"
    assert word == word.strip(), "word has leading/trailing whitespace"
    assert not word.isspace(), "word is only whitespace"
    assert len(word.split()) == 1, "entry must be exactly one word"
    assert " " not in word and "\t" not in word and "\n" not in word
    # The file must decode as UTF-8 and hold exactly the word, nothing else.
    assert word.encode("utf-8").decode("utf-8") == word

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(word)


if __name__ == "__main__":
    main()
