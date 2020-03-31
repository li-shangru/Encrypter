#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test file for ED.py
"""

import pytest
import random
import math
import string
import importlib
import ED


def test_number():
    """
    Test 16 random generated numbers, each number in range (-x^128, x^128)
    """
    for x in range(16):
        importlib.reload(ED)
        random_number = str(random.randint(-(x ** 128), x ** 128))
        encrypted_result = ED.encrypt(random_number, False)
        decrypted_result = ED.decrypt(encrypted_result, False)
        assert random_number == decrypted_result


def test_string():
    """
    Test 16 random generated letters, length of each letter is in range (0, x^4)
    """
    for x in range(16):
        importlib.reload(ED)
        letters = string.ascii_letters
        random_letters = "".join(
            random.choice(letters) for i in range(random.randint(0, x ** 4))
        )
        encrypted_result = ED.encrypt(random_letters, False)
        decrypted_result = ED.decrypt(encrypted_result, False)
        assert random_letters == decrypted_result


def test_character():
    """
    Test 16 random generated special characters, length of each character is in range (0, x^4)
    """
    for x in range(16):
        importlib.reload(ED)
        characters = string.punctuation
        random_character = "".join(
            random.choice(characters) for i in range(random.randint(0, x ** 4))
        )
        encrypted_result = ED.encrypt(random_character, False)
        decrypted_result = ED.decrypt(encrypted_result, False)
        assert random_character == decrypted_result


def test_characters_letters_numbers():
    """
    Test 16 random generated string consist of special characters, letters and digits,
    Of length in range 0 to x^4
    """
    for x in range(16):
        importlib.reload(ED)
        mixed_input = string.ascii_letters + string.digits + string.punctuation
        random_input = "".join(
            random.choice(mixed_input) for i in range(random.randint(0, x ** 4))
        )
        encrypted_result = ED.encrypt(random_input, False)
        decrypted_result = ED.decrypt(encrypted_result, False)
        assert random_input == decrypted_result


def test_error_input():
    """
    Test 100 random generated string consist of special characters, letters and digits,
    Of length in range 0 to x. As input to the decrypt function, which should fail.
    """
    for x in range(100):
        importlib.reload(ED)
        mixed_input = string.ascii_letters + string.digits + string.punctuation
        random_input = "".join(
            random.choice(mixed_input) for i in range(random.randint(0, x))
        )
        with pytest.raises(SyntaxError):
            ED.decrypt(random_input, False)
