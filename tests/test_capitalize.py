from functions import capitalize_words


def test_capitalize_words_normal_text():
    assert capitalize_words("hello WORLD") == "Hello World"


def test_capitalize_words_empty_text():
    assert capitalize_words("") == ""


def test_capitalize_words_keeps_punctuation():
    assert capitalize_words("hello, world!") == "Hello, World!"
