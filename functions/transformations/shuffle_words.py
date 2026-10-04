import random


def shuffle_words(text):
    """Return the text with its words in a random order.

    Words are separated by whitespace, and punctuation remains attached to
    the word it follows. Whitespace is normalized to single spaces.

    Args:
        text (str): The input text to be transformed.
    Returns:
        str: The text with its words shuffled.
    """
    words = text.split()
    random.shuffle(words)
    return " ".join(words)
