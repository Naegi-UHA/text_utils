from text_utils.functions.transformations.shuffle_words import shuffle_words


def test_shuffle_words_reorders_words_and_keeps_punctuation(monkeypatch):
    monkeypatch.setattr(
        "text_utils.functions.transformations.shuffle_words.random.shuffle",
        lambda words: words.reverse(),
    )

    assert shuffle_words("Hello, world! This is text.") == "text. is This world! Hello,"


def test_shuffle_words_normalizes_whitespace(monkeypatch):
    monkeypatch.setattr(
        "text_utils.functions.transformations.shuffle_words.random.shuffle",
        lambda words: None,
    )

    assert shuffle_words("  one\t two\nthree  ") == "one two three"


def test_shuffle_words_empty_text():
    assert shuffle_words("") == ""


def test_shuffle_words_whitespace_only_text():
    assert shuffle_words(" \t\n ") == ""
