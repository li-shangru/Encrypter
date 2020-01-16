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

def testNumber():
	"""
	Test 16 random generated numbers, each number in range (-x^128, x^128)
	"""
	for x in range(16):
		importlib.reload(ED)
		randomNumber = str(random.randint(-x**128, x**128))
		encryptedResult = ED.encrypt(randomNumber, False)
		decryptedResult = ED.decrypt(encryptedResult, False)
		assert randomNumber == decryptedResult

def testString():
	"""
	Test 16 random generated letters, length of each letter is in range (0, x^4)
	"""
	for x in range(16):
		importlib.reload(ED)
		letters = string.ascii_letters
		randomLetters = ''.join(random.choice(letters) for i in range(random.randint(0, x**4)))
		encryptedResult = ED.encrypt(randomLetters, False)
		decryptedResult = ED.decrypt(encryptedResult, False)
		assert randomLetters == decryptedResult

def testCharacter():
	"""
	Test 16 random generated special characters, length of each character is in range (0, x^4)
	"""
	for x in range(16):
		importlib.reload(ED)
		characters = string.punctuation
		randomCharacter = ''.join(random.choice(characters) for i in range(random.randint(0, x**4)))
		encryptedResult = ED.encrypt(randomCharacter, False)
		decryptedResult = ED.decrypt(encryptedResult, False)
		assert randomCharacter == decryptedResult

def testCharactersLettersNumbers():
	"""
	Test 16 random generated string consist of special characters, letters and digits,
	Of length in range 0 to x^4
	"""
	for x in range(16):
		importlib.reload(ED)
		mixedInput = string.ascii_letters + string.digits + string.punctuation
		randomInput = ''.join(random.choice(mixedInput) for i in range(random.randint(0, x**4)))
		encryptedResult = ED.encrypt(randomInput, False)
		decryptedResult = ED.decrypt(encryptedResult, False)
		assert randomInput == decryptedResult