from text_utils.functions import character_count


def test_character_count_normal_text():
    assert character_count("Hello, world!") == 13


def test_character_count_empty_text():
    assert character_count("") == 0


def test_character_count_counts_spaces_and_unicode():
    assert character_count("é 🙂") == 3
