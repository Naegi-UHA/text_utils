def word_count(text):
    """Count the whitespace-separated words in a string.

    Parameters
    ----------
    text : str
        The text to analyze.

    Returns
    -------
    int
        The number of words in ``text``.
    """
    return len(text.split())
