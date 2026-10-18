from functions import reverse


def test_reverse_normal_text():
    assert reverse("hello") == "olleh"


def test_reverse_empty_text():
    assert reverse("") == ""


def test_reverse_unicode_text():
    assert reverse("é🙂") == "🙂é"
