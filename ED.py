import random

seed_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
seed_number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
seed_symbol = ['`', '~', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', '{', ']', '}', '|', ';',
               ':', '>', ',', '<', '.', '/', '?']

def encode(arg):
	# assign input string to `text` 
    text = arg
    # `check' is for remembering if the input string is code or seed
    check = 0
    # if the first character of the input is '!' then it's the seed
    if arg[0] == '!':
        check = 1
        text = arg.replace('!', '')
    # initialize code
    code = ""
    # initialize a random offset of range (10,99)
    # offset is added to the character's
    offset = random.randint(10, 99)
    # set length of the input string
    length = len(text)

	# check for input's length, if it's greater than 9,
	# i.e., it's double digit, then we want to set a indicator in
	# front of the seed, indicator is randomly selected from 'seed_letter'
    if length > 9:
        indicator = seed_letter[random.randint(0, len(seed_letter) - 1)]
        seed = indicator + str(length) + str(offset)
    else:
        seed = str(length) + str(offset)
    # looping over every character in the input string
    for n in text:
    	# first randomly pick a letter from 'seed_letter'
        seed1 = seed_letter[random.randint(0, len(seed_letter) - 1)]
        # then randomly pick a number from 'seed_number'
        seed2 = seed_number[random.randint(0, len(seed_number) - 1)]
        # finally randomly pick a symbol from 'seed_symbol'
        seed3 = seed_symbol[random.randint(0, len(seed_symbol) - 1)]
        # combine the three random seeds to one
        seed_combine = seed1 + seed2 + seed3
        # the initial code consists of:
        # "" + of character plus 'offset' + combination of three seeds
        code = code + str(ord(n) + offset) + seed_combine
        # remember the random seeds
        seed = seed + seed_combine
    # check = 1 means we have encoded the seed
    if check == 1:
    	# then we return the en
        return seed + code + '!'
    # we encode the seed and put an indicator '!' in front of it
    return encode('!' + seed) + code


def decode(arg):
	# assign input string to 'cypher'
    cypher = arg
    # try to locate the seed/code separation indicator
    if arg.find('!') != -1:
    	# split seed and code by separator '!'
        seed_code, code_code = arg.split('!')
        # decode the seed first
        seed_code = decode(seed_code)
        # combine decoded seed and code
        # at this point cyhper should not contain '!'
        # hence, cypher.has('!') ? seed not decoded
        cypher = seed_code + code_code
    # `char` is the result string
    chars = []
    # `trans` is used to store the character to decode
    trans = []
    check = 0
    header = 0
    seed_index = 0
    seed_num = 3
    # check the first character of the cypher
    # if it's a digit, then the actual result string is single digit length
    if cypher[0].isdigit():
    	# `header` is the length of `length` and `offset`
        header = 3
        # `length` is the first index
        length = int(cypher[0])
        # `offset` is the sum of the first and second index after `length`
        offset = int(cypher[1] + cypher[2])
        # `seed` is the 'length' * 'seed_num' without the "header"-`length` and `offset`
        seed = cypher[3:length * seed_num + header]
        # `code` is what's left after `seed`
        code = cypher[length * seed_num + header:]
    else:
    	# case where the result string's length is double digit
        # the first index is a indicator, hence real cypher starts index 5
        header = 5
        # first index is indicator, length is double digit
        length = int(cypher[1] + cypher[2])
        # rest is the same
        offset = int(cypher[3] + cypher[4])
        seed = cypher[5:length * seed_num + header]
        code = cypher[length * seed_num + header:]
    # go through each character in `code`
    for line in code:
        for c in line:
        	# separate the three seeds
            seed1 = seed[seed_index]
            seed2 = seed[seed_index + 1]
            seed3 = seed[seed_index + 2]
            # current index points to `seed1`, increment `check` go to next character
            if c == seed1 and check == 0:
                check = 1
            # current index points to `seed2`, do the same
            elif c == seed2 and check == 1:
                check = 2
            # current index points to `seed3`, we can start decoding
            elif c == seed3 and check == 2:
            	# each original character is the ASCII code - offset
                chars.append((chr(int(''.join(trans)) - offset)))
                # clear the array after the have decoded
                trans.clear()
                # proceed to next character
                check = 0
                seed_index = seed_index + seed_num
            else:
            	# index points to the encoded char, store it for decode
                trans.append(c)
    # return the result output
    return ''.join(chars)
    
##############---Message_Display_Input_Handel---#####################

input_str = input("Enter: ")
result = encode(input_str)
print("Encode: " + result)
print("Decode: " + decode(result) + '\n')
#print("Encode_input: " + result[len(input_str * 3) + 3:] + '\n' + "Encode_seed: " + result[:len(input_str) * 3 + 3])
