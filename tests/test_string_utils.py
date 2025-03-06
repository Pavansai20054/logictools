import pytest
from logictools import string_utils

def test_convert_to_uppercase():
    assert string_utils.convert_to_uppercase("hello") == "HELLO"

def test_reverse_string():
    assert string_utils.reverse_string("hello") == "olleh"

def test_character_count():
    assert string_utils.character_count("Hello") == 5
