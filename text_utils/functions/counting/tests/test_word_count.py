from text_utils.functions import word_count


def test_word_count_normal_text():
    assert word_count("one two three") == 3


def test_word_count_empty_text():
    assert word_count("") == 0


def test_word_count_whitespace_only_text():
    assert word_count(" \t\n ") == 0
