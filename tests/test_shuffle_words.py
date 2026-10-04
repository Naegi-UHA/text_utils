import unittest
from unittest.mock import patch

from functions.transformations.shuffle_words import shuffle_words


class ShuffleWordsTests(unittest.TestCase):
    @patch("functions.transformations.shuffle_words.random.shuffle")
    def test_shuffles_words_and_preserves_attached_punctuation(self, shuffle):
        shuffle.side_effect = lambda words: words.reverse()

        result = shuffle_words("Hello, world! This is text.")

        self.assertEqual(result, "text. is This world! Hello,")

    @patch("functions.transformations.shuffle_words.random.shuffle")
    def test_normalizes_whitespace(self, shuffle):
        shuffle.side_effect = lambda words: None

        self.assertEqual(shuffle_words("  one\t two\nthree  "), "one two three")

    def test_empty_text_returns_empty_text(self):
        self.assertEqual(shuffle_words(""), "")


if __name__ == "__main__":
    unittest.main()
