import random


def shuffle_words(text):
    """Return the words in a string in random order.

    Words are separated by whitespace, and punctuation remains attached to
    the word it follows. Whitespace is normalized to single spaces.

    Parameters
    ----------
    text : str
        The text to transform.

    Returns
    -------
    str
        The words in random order, separated by single spaces.
    """
    words = text.split()
    random.shuffle(words)
    return " ".join(words)
