#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test file for ED.py
"""

import pytest # type: ignore
import random
import string
import importlib
import ED


def test_number():
    """
    Test 16 random generated numbers, each number in range (-x^128, x^128).
    """
    for x in range(16):
        importlib.reload(ED)
        random_number: str = str(random.randint(-(x ** 128), x ** 128))
        encrypted_result: str = ED.encrypt(random_number)
        decrypted_result: str = ED.decrypt(encrypted_result)
        assert random_number == decrypted_result


def test_string():
    """
    Test 16 random generated letters, length of each letter is in range (1, x^4).
    """
    for x in range(2, 16):
        importlib.reload(ED)
        letters: str = string.ascii_letters
        random_letters: str = "".join(
            random.choice(letters) for i in range(random.randint(1, x ** 4))
        )
        encrypted_result: str = ED.encrypt(random_letters)
        decrypted_result: str = ED.decrypt(encrypted_result)
        assert random_letters == decrypted_result


def test_character():
    """
    Test 16 random generated special characters, length of each character is in range (1, x^4).
    """
    for x in range(2, 16):
        importlib.reload(ED)
        characters: str = string.punctuation
        random_character: str = "".join(
            random.choice(characters) for i in range(random.randint(1, x ** 4))
        )
        encrypted_result: str = ED.encrypt(random_character)
        decrypted_result: str = ED.decrypt(encrypted_result)
        assert random_character == decrypted_result


def test_characters_letters_numbers():
    """
    Test 16 random generated string consist of special characters, letters and digits,
    Of length in range 1 to x^4.
    """
    for x in range(2, 16):
        importlib.reload(ED)
        mixed_input: str = string.ascii_letters + string.digits + string.punctuation
        random_input: str = "".join(
            random.choice(mixed_input) for i in range(random.randint(1, x ** 4))
        )
        encrypted_result: str = ED.encrypt(random_input)
        decrypted_result: str = ED.decrypt(encrypted_result)
        assert random_input == decrypted_result


def test_error_input():
    """
    Test 100 random generated string consist of special characters, letters and digits,
    Of length in range 1 to x. As input to the decrypt function, which should fail.
    """
    for x in range(2, 100):
        importlib.reload(ED)
        mixed_input: str = string.ascii_letters + string.digits + string.punctuation
        random_input: str = "".join(
            random.choice(mixed_input) for i in range(random.randint(1, x))
        )
        with pytest.raises(SyntaxError):
            ED.decrypt(random_input)


def test_empty_input():
    """
    Test empty input on encrypt function, which return an error message.
    """
    with pytest.raises(SyntaxError):
        ED.encrypt('')
