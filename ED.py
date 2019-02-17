import random

input_str = input("Enter: ")

seed_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
seed_number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
seed_symbol = ['`', '~', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', '{', ']', '}', '|', ';',
               ':', '>', ',', '<', '.', '/', '?']


def encode(arg):
    text = arg
    check = 0
    if arg[0] == '!':
        check = 1
        text = arg.replace('!', '')
    code = ""
    offset = random.randint(10, 99)
    length = len(text)

    if length > 9:
        indicator = seed_letter[random.randint(0, len(seed_letter) - 1)]
        seed = indicator + str(length) + str(offset)
    else:
        seed = str(length) + str(offset)
    for n in text:
        seed1 = seed_letter[random.randint(0, len(seed_letter) - 1)]
        seed2 = seed_number[random.randint(0, len(seed_number) - 1)]
        seed3 = seed_symbol[random.randint(0, len(seed_symbol) - 1)]
        seed_combine = seed1 + seed2 + seed3
        code = code + str(ord(n) + offset) + seed_combine
        seed = seed + seed_combine
    if check == 1:
        return seed + code + '!'
    return encode('!' + seed) + code


def decode(arg):
    cypher = arg
    if arg.find('!') != -1:
        seed_code, code_code = arg.split('!')
        seed_code = decode(seed_code)
        cypher = seed_code + code_code
    chars = []
    trans = []
    check = 0
    header = 0
    seed_index = 0
    seed_num = 3
    if cypher[0].isdigit():
        header = 3
        length = int(cypher[0])
        offset = int(cypher[1] + cypher[2])
        seed = cypher[3:length * seed_num + header]
        code = cypher[length * seed_num + header:]
    else:
        header = 5
        length = int(cypher[1] + cypher[2])
        offset = int(cypher[3] + cypher[4])
        seed = cypher[5:length * seed_num + header]
        code = cypher[length * seed_num + header:]
    for line in code:
        for c in line:
            seed1 = seed[seed_index]
            seed2 = seed[seed_index + 1]
            seed3 = seed[seed_index + 2]
            if c == seed1 and check == 0:
                check = 1
            elif c == seed2 and check == 1:
                check = 2
            elif c == seed3 and check == 2:
                chars.append((chr(int(''.join(trans)) - offset)))
                trans.clear()
                check = 0
                seed_index = seed_index + seed_num
            else:
                trans.append(c)
    return ''.join(chars)


result = encode(input_str)
#print("Encode_input: " + result[len(input_str * 3) + 3:] + '\n' + "Encode_seed: " + result[:len(input_str) * 3 + 3])
print("Encode: " + result)
print("Decode: " + decode(result) + '\n')
