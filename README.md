# text_utils
This package provides basic functions for manipulating strings and text.

## Installation

```bash
python -m pip install text-utils-lucas-runser
```

## Usage

Import the functions from `text_utils.functions`:

```python
from text_utils.functions import (
    capitalize_words,
    character_count,
    reverse,
    shuffle_words,
    word_count,
)
```

Available functions:

- word_count
- character_count
- reverse
- capitalize_words
- shuffle_words

`shuffle_words(text)` returns the words in a random order. Words are separated by
whitespace, punctuation stays attached to its word, and whitespace in the result
is normalized to single spaces.
