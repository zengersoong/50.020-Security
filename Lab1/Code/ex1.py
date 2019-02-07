#!/usr/bin/env python3
# SUTD 50.020 Security Lab 1
# Simple file read in/out
# Quyen, 2014

# Import libraries
import sys
import argparse
import string
import numbers
import os



def encrypt(string, shift):
	cipher = ''
	for char in string:
		# Dealing with Spaces.
		if char ==' ' or char =='\n':
			cipher = cipher + char
		# Dealing with Uppercase.
		elif char.isupper():
			cipher = cipher + chr((ord(char) + shift - 65)%26+65)
		# Dealing with Lowercase.
		elif char.islower():
			cipher = cipher + chr((ord(char) + shift -97)%26+97)
		# Dealing with Symbols.
		elif  set('!"#$%&\'()*+,-./:;<=>?@').intersection(char) or set('1234567890').intersection(char):
			cipher = cipher + chr((ord(char) + shift - 33)%32+33)
		# Dealing with the rest.
		else:
			cipher = cipher + chr((ord(char) + shift - 91)%6+91)
	return cipher

def decrypt(string, shift):
	cipher = ''
	for char in string:
		# Dealing with Spaces and newline.
		if char ==' ' or char =='\n':
			cipher = cipher + char
		# Dealing with Uppercase.
		elif char.isupper():
			cipher = cipher + chr((ord(char) - shift - 65)%26+65)
		# Dealing with Lowercase.
		elif char.islower():
			cipher = cipher + chr((ord(char) - shift -97)%26+97)
		# Dealing with Symbols.
		elif  set('!"#$%&\'()*+,-./:;<=>?@').intersection(char) or set('1234567890').intersection(char) or set().intersection(char):
			cipher = cipher + chr((ord(char) - shift - 33)%32+33)
		# Dealing with the rest.
		else:
			cipher = cipher + chr((ord(char) - shift - 91)%6+91)
	return cipher


def doStuff(filein,fileout):
    # open file handles to both files
    fin  = open(filein, mode='r', encoding='utf-8', newline='\n')       # read mode
    fout = open(fileout, mode='w', encoding='utf-8', newline='\n')      # write mode
    c    = fin.read()         # read in file into c as a str

    # and write to fileout
    if modeType.lower() == 'e':
    	encryptedC = encrypt(c,int(encryptionKey))
    	fout.write(encryptedC)
    elif modeType.lower() == 'd':
    	decryptedC = decrypt(c,int(encryptionKey))
    	fout.write(decryptedC)

    # close all file streams
    fin.close()
    fout.close()

    # PROTIP: pythonic way
        # file will be closed automatically when interpreter reaches end of the block

def checkValidKey(key):
	boolInt=True
	try:
		keyInteger = int(key)
	except ValueError:
		print("Key is not a valid integer key!")
		boolInt = False
	return (all(c in string.printable for c in key) and boolInt)

def checkValidMode(mode):

	if mode.lower() == 'd' or mode.lower() =='e':
		return True
	else:
		return False


# our main function
if __name__=="__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='filein',help='input file')
    parser.add_argument('-o', dest='fileout', help='output file')
    parser.add_argument('-k', dest='key',help='encryption key')
    parser.add_argument('-m', dest='mode',help='mode e for encode, d for decode')

    # parse our arguments
    args = parser.parse_args()
    filein=args.filein
    fileout=args.fileout
    encryptionKey=args.key
    modeType = args.mode

    if (checkValidKey(encryptionKey) and checkValidMode(modeType)):
    	print("Arguments entry are correct, key used: %s mode: %s"%(encryptionKey,modeType))
    	doStuff(filein,fileout)

    else:
    	print('Please re-enter, parsed arguments may be incorrect.')


    

    # all done


