#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A simple script to encrypt and decrypt strings.
"""

import random

__author__ = "Shangru Li"
__copyright__ = "Copyright 2020, Shangru Li"
__credits__ = "Shangru Li"
__license__ = "MIT"
__version__ = "2.0"
__maintainer__ = "Shangru Li"
__email__ = "max.shangru.li@gmail.com"
__status__ = "Stable"

###############################___Seeds___######################################
seedLetter =[
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
	'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z'
	]
seedNumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
seedSymbol = [
	'`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+',
	'=', '[', '{', ']', '}', '|', ';', ':', '>', ',', '<', '.', '/', '?'
	]
################################################################################

def main():
	seedIndicator = generateSeedIndicator()
	textToEncrypt = input("Enter: ")
	encryptedText = encrypt(textToEncrypt, seedIndicator)
	print("Encrypt: " + encryptedText)
	print("Decrypt: " + decrypt(encryptedText, seedIndicator) + '\n')

def generateSeedIndicator():
	"""
	Generate a special character to separate the seed and code from the `seed_symbol`
	"""
	seedIndicator = seedSymbol[random.randint(0, len(seedSymbol) - 1)]
	seedSymbol.remove(seedIndicator)
	return seedIndicator

def getRandomCaseSeedLetter():
	"""
	Randomly pick a either uppercase or lowercase letter from `seedLetter`
	"""
	seed = random.randint(0, 1)
	if seed == 0:
		return seedLetter[random.randint(0, len(seedLetter) - 1)]
	else:
		return str.capitalize(seedLetter[random.randint(0, len(seedLetter) - 1)])

def countNumOfOccurrences(list, x):
	"""
	Count the number of occurrences of `x` in `list`
	"""
	return list.count(x)

def encrypt(textToEncrypt, seedIndicator):
	# If the first character of the input is `seedIndicator` then it's the seed
	if textToEncrypt[0] == seedIndicator:
		# Remove the `seedIndicator`
		inputText = textToEncrypt.replace(seedIndicator, '')
	else:
		inputText = textToEncrypt
	code = ""
	# Initialize a random offset to be added to the character's ASCII code
	offset = random.randint(10, 99)
	# The first two characters of the `seed` is the `offset`
	seed = str(offset)
	for n in inputText:
		# Randomly pick a letter from 'seed_letter', upper or lower case
		randomLetter = getRandomCaseSeedLetter()
		# Randomly pick a number from 'seed_number'
		randomNumber = seedNumber[random.randint(0, len(seedNumber) - 1)]
		# Randomly pick a symbol from 'seed_symbol'
		randomSymbol = seedSymbol[random.randint(0, len(seedSymbol) - 1)]
		seed_combine = randomLetter + randomNumber + randomSymbol
		# Appending to the seed
		seed = seed + seed_combine
		# The result is:
		# ASCII code of character plus 'offset' + combination of three seeds
		code = code + str(ord(n) + offset) + seed_combine
	if textToEncrypt[0] == seedIndicator:
		# If the first character is the `seedIndicator`, then we just
		# encrypted the seed. Hence we return the full encrypted input.
		return seed + seedIndicator + code + seedIndicator
	else:
		# Else we encode the seed and put an indicator seedIndicator in front of it
		return encrypt(seedIndicator + seed, seedIndicator) + code

def decrypt(textToDecrypt, seedIndicator):
	# There should be 2 occurrences of `seedIndicator` in the `textToDecrypt`
	# The `textToDecrpt` should looks like this:
	# {seed + seedIndicator + encryptedSeed} + {seedIndicator + encryptedInput}
	if countNumOfOccurrences(textToDecrypt, seedIndicator) == 2:
		# Split the input by `seedIndicator` to three parts
		seedForEncryptedSeed, encryptedSeed, encryptedInput = textToDecrypt.split(seedIndicator)
		# Decrpt the seed for user input
		decryptedSeed = decrypt(seedForEncryptedSeed + seedIndicator + encryptedSeed, seedIndicator)
		# Combine the decrypted seed with encrypted input for further encrypt
		textToDecrypt = decryptedSeed + seedIndicator + encryptedInput
	# The first two characters of seed is the `offset`
	offset = int(textToDecrypt[0] + textToDecrypt[1])
	# Remove the `offset` from `textToDecrpt`
	textToDecrypt = textToDecrypt[2:len(textToDecrypt)]
	# Split the textToDecrypt by seedIndicator to get the seed and code
	seed, code = textToDecrypt.split(seedIndicator)
	result = []
	# This is to remember the ASCII code for a paticular character
	# For example, ASCII code 102, in this list: ['1', '0', '2']
	asciiList = []
	# Check which seed the index is pointing at
	check = 0
	# The index for seed list
	seedIndex = 0
	for i in range(len(code)):
		# separate the three seeds
		seed1 = seed[seedIndex]
		seed2 = seed[seedIndex + 1]
		seed3 = seed[seedIndex + 2]
		# current index points to `seed1`, increment `check` go to next character
		if code[i] == seed1 and check == 0:
			check = 1
		# current index points to `seed2`, do the same
		elif code[i] == seed2 and check == 1:
			check = 2
		# current index points to `seed3`, we can start decrypting
		elif code[i] == seed3 and check == 2:
			# each original character is the ASCII code - offset
			result.append((chr(int(''.join(asciiList)) - offset)))
			# clear the array after the have decrypted
			asciiList.clear()
			# Go to the next set of seed
			seedIndex += 3
			check = 0
		else:
			# index points to the encrypted char, store it for decrypt
			asciiList.append(code[i])
	return ''.join(result)

if __name__ == "__main__":
	main()
