#!/usr/bin/env python3
# ECB wrapper skeleton file for 50.020 Security
# Oka, SUTD, 2014
# 2019
import binascii
from present import *
import argparse


nokeybits=80
blocksize=64


def ecb(infile,outfile,key,mode):
    # Checking the mode of the command
    if mode == 'e':
        print('Encrypting "' + infile + '" saved as "' + outfile + '"')
    elif mode == 'd':
        print('Decrypting "' + infile + '" saved as "' + outfile + '"')
    else:
        return print('Wrong Mode Entry! Only "e" and "d"')
 
    #Open the 2 files
    inputs = open(infile, mode = 'rb')
    keystream = open(key, mode = 'r')


    key = int(keystream.read(), 16)
    outputByte = []
    inputblock = inputs.read(8)
    #Read it block by block as long as input still not empty...
    while (inputblock != b''):
        block = ''
        for i in inputblock:
            block += format(i,'08b')
        block = int(block, 2)
        # Either decrypt or encrypt based on the command. 
        if mode == 'e':
            outputByte.append(binascii.unhexlify('%016x' % present(block, key)))
        elif mode == 'd':
            outputByte.append(binascii.unhexlify('%016x' % present_inv(block, key)))
        inputblock = inputs.read(8)

    # Write output to output file
    output = open(outfile, mode = 'wb')
    for i in outputByte:
        output.write(i)
    if mode == 'e':
            print('encryption Completed!')
    elif mode == 'd':
        print('Decryption Completed!')

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Block cipher using ECB mode.')
    parser.add_argument('-i', dest='infile',help='input file')
    parser.add_argument('-o', dest='outfile',help='output file')
    parser.add_argument('-k', dest='keyfile',help='key file')
    parser.add_argument('-m', dest='mode',help='mode')

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    keyfile=args.keyfile
    mode=args.mode

    ecb(infile, outfile, keyfile, mode)