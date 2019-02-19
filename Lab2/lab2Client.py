#!/usr/bin/python3
# -*- coding: utf-8 -*-
# DA+Nils 2018
# Andrei + Z.TANG, 2019

"""
Lab2: Breaking Ciphers

Pwntool client for python3

Install: see install.sh

Documentation: https://python3-pwntools.readthedocs.io/en/latest/
"""

from pwn import remote

# pass two bytestrings to this function
def XOR(a, b):
    r = b''
    for x, y in zip(a, b):
        r += (x ^ y).to_bytes(1, 'big')
    return r





def sol2():
    conn = remote(URL, PORT)
    message = conn.recvuntil('-Pad')  # receive TCP stream until end of menu
    conn.sendline("2")  # select challenge 2

    dontcare = conn.recvuntil(':')
    challenge = conn.recvline()
    # some all zero mask.
    # TODO: find the magic mask!
    mask = int(0).to_bytes(len(message), 'big')
    print(challenge)
    # b'\x16\x1d\x0cV\x13\x0b\x17I>!EbX\x00QEUYkR\x14\x01\x16EyB\x11],\x0b\x07\x1b\n'
    challenge = b'\x16\x1d\x0cV\x13\x0b\x17I>!EbX\x00SER]kR\x14\x01\x16E}B\x11],\x0b\x07\x1b\n'
    message = XOR(challenge, mask)
    conn.send(message)
    message = conn.recvline()
    message = conn.recvline()
    if b'exact' in message:
        print(message)
    conn.close()



def sol1():
    conn = remote(URL, PORT)
    message = conn.recvuntil('-Pad')  # receive TCP stream until end of menu
    conn.sendline("1")  # select challenge 1

    dontcare = conn.recvuntil(':')
    challenge = conn.recvline()
    # print(challenge)
    # decrypt the challenge here
    frequency_analysis(challenge)

    # print(challenge)
    decrypted_1=remap(challenge)
    solution = decrypted_1.encode('utf-8')


    # solution = ans1.to_bytes(7408, 'big')
    # solution = bytes(decrypted_1, encoding='ascii')
    print(solution)
    conn.send(solution)
    message = conn.recvline()
    message = conn.recvline()
    if b'Congratulations' in message:
        print(message)
    conn.close()



def frequency_analysis(challenge):

    freqDict={}
    for char in challenge:
        # if char != 13 or char != 9:
        if chr(char) not in freqDict:
            freqDict[chr(char)]=1
        else:
            freqDict[chr(char)]+=1
    #Order the Dictionary by frequency of occurences.
    sortedFreqDict=sorted(freqDict, key=freqDict.get, reverse=True)
    print("Number of unique chars in the ciphered text is : {0}".format(len(freqDict)))
    print(sortedFreqDict)

def remap(challenge):
    new_string = ""
    f= open('unciphered_text.txt','w')
    for char in challenge:
        #Change all J to spaces
        if char == 74:
            char = 32
        #Change all [ to e
        elif char == 91:
            char = 101
        #change 7 to t
        elif char == 55:
            char = 116
        #change - to a
        elif char == 45:
            char = 97
        elif char == 50:
            char = 108
        #change ^ to i 
        elif char == 94:
            char = 105
        # change space to d
        elif char == 32:
            char = 100
        # change w to r
        elif char == 119:
            char = 114
        #change y to o
        elif char ==121:
            char = 111
        #change i to h
        elif char == 105:
            char = 104
        # change ; to n
        elif char == 59:
            char = 110
        # change \r to 
        elif char == 13:
            char = 115
        # change m to w
        elif char == 109:
            char = 119
        # change ] to \n
        elif char == 93:
            char = 10
        # change C to g
        elif char == 67:
            char = 103
        # change 9 to comma
        elif char == 57:
            char = 44
        # chnage F to u
        elif char==70:
            char = 117
        # change n to c
        elif char == 110:
            char =99
        # change u to m 
        elif char == 117:
            char = 109
        #change ( to y
        elif char == 40:
            char = 121
        # change @ to f
        elif char == 64:
            char = 102
        # change q to p 
        elif char == 113:
            char =112
        # Change R to .
        elif char == 82:
            char = 46
        # change \t to !
        elif char == 9:
            char = 98
        # change a to k
        elif char == 97:
            char =107
        # change c to v
        elif char == 99:
            char =118
        # change _ to \
        elif char == 99:
            char =95
        # change _ to -
        elif char == 95:
            char = 34
        # change 3 to f 
        elif char == 51:
            char = 63
        # change B to q
        elif char == 66:
            char = 113
        # change : to '
        elif char == 58:
            char = 39
        # change ? to q
        elif char == 63:
            char = 113
        # change j to '
        elif char == 106:
            char = 39
        # change e to -
        elif char == 101:
            char = 45
        # change 8 to j
        elif char == 56:
            char = 106
        # change z to \n
        elif char == 122:
            char = 10

        new_string = new_string+chr(char)
    with f as out:
        out.write(new_string)
    return new_string



if __name__ == "__main__":

    # NOTE: UPPERCASE names for constants is a (nice) Python convention
    URL = '157.230.47.126'
    PORT = 1337

    sol1()
    sol2()
