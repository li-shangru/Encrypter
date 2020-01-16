#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test file for ED.py
"""

import pytest
import random
import math
import string
import ED

def testNumber():
    """
    Test a random generated number within range -2^256 to 2^256
    """
    randomNumber = str(random.randint(-2**256, 2**256))
    encryptedResult = ED.encrypt(randomNumber, False)
    decryptedResult = ED.decrypt(encryptedResult, False)
    print(randomNumber)
    assert randomNumber == decryptedResult

def testString():
    """
    Test a random generated string of length in range 0 to 2^16
    """
    letters = string.ascii_letters
    randomString = ''.join(random.choice(letters) for i in range(random.randint(0, 2**16)))
    encryptedResult = ED.encrypt(randomString, False)
    decryptedResult = ED.decrypt(encryptedResult, False)
    print(randomString)
    assert randomString == decryptedResult

def testCharacter():
    """
    Test a random generated special character of length in range 0 to 2^16
    """
    characters = string.punctuation
    randomString = ''.join(random.choice(characters) for i in range(random.randint(0, 2**16)))
    encryptedResult = ED.encrypt(randomString, False)
    decryptedResult = ED.decrypt(encryptedResult, False)
    print(randomString)
    assert randomString == decryptedResult

def testCharactersLettersNumbers():
    """
    Test a random generated string consist of special characters, letters and digits
    Of length in range 0 to 2^16
    """
    mixedInput = string.ascii_letters + string.digits + string.punctuation
    randomString = ''.join(random.choice(mixedInput) for i in range(random.randint(0, 2**16)))
    encryptedResult = ED.encrypt(randomString, False)
    decryptedResult = ED.decrypt(encryptedResult, False)
    print(randomString)
    assert randomString == decryptedResult