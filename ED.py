#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A simple script to encrypt and decrypt strings.
"""

import random
import argparse

__author__ = "Shangru Li"
__copyright__ = "Copyright 2020, Shangru Li"
__credits__ = "Shangru Li"
__license__ = "MIT"
__version__ = "2.8"
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
###############################___Args___#######################################
parser = argparse.ArgumentParser()
parser.add_argument('-d', "--decrypt", help="Decrypt an encrypted string", type=str)
parser.add_argument('-e', "--encrypt", help="Encrypt an input string", type=str)
################################################################################

def main():
	# Program info
	print("Encrypter " + __version__ + '\n')
	args = parser.parse_args()
	if args.decrypt is not None:
		try:
			print("Decrypting: " + args.decrypt)
			decryptedInput = decrypt(args.decrypt, False)
			print("Decrypted: " + decryptedInput + '\n')
		except SyntaxError:
			print("Decryption failed, please make sure the encrypted text is correct." + '\n')
	elif args.encrypt is not None:
		print("Encrypting: " + args.encrypt)
		encryptedInput = encrypt(args.encrypt, False)
		print("Encrypted: " + encryptedInput + '\n')
	else:
		# Encrypt
		textToEncrypt = input("Enter text to encrypt : ")
		print("Encrypting: " + textToEncrypt)
		encryptedText = encrypt(textToEncrypt, False)
		print("Encrypted: " + encryptedText + '\n')
		# Decrypt
		textToDecrypt = input("Enter text to decrypt : ")
		try:
			decryptedText = decrypt(textToDecrypt, False)
			print("Decrypting: " + textToDecrypt)
			print("Decrypted: " + decryptedText + '\n')
		except SyntaxError:
			print("Decryption failed, please make sure the encrypted text is correct." + '\n')
	userCommand = input('Enter R to run the program again, or anything else to exit: ')
	if userCommand == 'R' or userCommand == 'r' :
		print('\n')
		main()

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

def encrypt(textToEncrypt, isSeed):
	if isSeed == False:
		# Pick a random seedIndicator
		seedIndicator = generateSeedIndicator()
	else:
		seedIndicator = textToEncrypt[0]
		# Remove the `seedIndicator`
		textToEncrypt = textToEncrypt.replace(seedIndicator, '')
	code = ""
	# Initialize a random offset to be added to the character's ASCII code
	offset = random.randint(10, 99)
	# The first two characters of the `seed` is the `offset`
	seed = str(offset)
	for n in textToEncrypt:
		# Randomly pick a letter from 'seed_letter', upper or lower case
		randomLetter = getRandomCaseSeedLetter()
		# Randomly pick a number from 'seed_number'
		randomNumber = seedNumber[random.randint(0, len(seedNumber) - 1)]
		# Randomly pick a symbol from 'seed_symbol'
		randomSymbol = seedSymbol[random.randint(0, len(seedSymbol) - 1)]
		# Appending to the seed
		seed_combine = randomLetter + randomNumber + randomSymbol
		# Appending to the seed
		seed = seed + seed_combine
		# The code is:
		# ASCII code of character plus 'offset' + combination of three seeds
		code = code + str(ord(n) + offset) + seed_combine
	if isSeed == True:
		# We have encrypted the seed. Return the full encrypted input.
		return seed + seedIndicator + code
	else:
		# Else we encode the seed
		return encrypt(seedIndicator + seed, True) + seedIndicator + code + seedIndicator

def decrypt(textToDecrypt, isSeed):
	try:
		# The last character is the `seedIndicator`
		seedIndicator = textToDecrypt[len(textToDecrypt) - 1]
		# Removing the `seedIndicator` from input
		textToDecrypt = textToDecrypt[:-1]
		# The `textToDecrpt` should looks like this:
		# {seedForEncryptedSeed + seedIndicator + encryptedSeed} +
		# {seedIndicator + encryptedInput + seedIndicator}
		if isSeed == False:
			# Splitting the seed and input
			seedForEncryptedSeed, encryptedSeed, encryptedInput = textToDecrypt.split(seedIndicator)
			# Decrpt the seed for user input
			decryptedSeed = decrypt(seedForEncryptedSeed + seedIndicator + encryptedSeed + seedIndicator, True)
			# Combine the decrypted seed with encrypted input for further encrypt
			textToDecrypt = decryptedSeed + seedIndicator + encryptedInput
		# The first three characters of seed is the `offset`
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
	except:
		raise SyntaxError("Input " + textToDecrypt + " is invalid.")

if __name__ == "__main__":
	main()
