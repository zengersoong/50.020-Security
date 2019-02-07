#!/usr/bin/env python3
# SUTD 50.020 Security Lab 1
# Simple file read in/out
# Quyen, 2014

# Import libraries
import sys
import argparse
def encrypt(inbytes, shift):
    if not 255>= shift >=0:
        raise ValueError("Key value not within acceptable range:" ,shift)
    outbytes = bytearray()
    for ic in inbytes:
        # Get rid of overflow.
        oc = ( ic + shift ) & 0xff
        outbytes.append(oc)
    return bytes(outbytes)

def decrypt(inbytes, shift):
    if  not 255 >= shift >= 0:
        raise ValueError("key value not within range:", shift)

    outbytes = bytearray()
    for ic in inbytes:
        oc = ic -  shift
        # Account the previous overflow.
        if oc < 0:
            oc += 0x100
        outbytes.append(oc)
    return bytes(outbytes)



def doStuff(filein,fileout):
    # open file handles to both files
    fin_b = open(filein, mode='rb')  # binary read mode
    fout_b = open(fileout, mode='wb')  # binary write mode
    c    = fin_b.read()         # read in file into c as a str
    # # and write to fileout
    if modeType.lower() == 'e':
        encryptedC = encrypt(c,int(encryptionKey))
        fout_b.write(encryptedC)
    elif modeType.lower() == 'd':
        decryptedC = decrypt(c,int(encryptionKey))
        fout_b.write(decryptedC)

    # close all file streams
    
    fin_b.close()
    fout_b.close()



def checkValidKey(key):
    if int(key) > 255 or int(key)<0:
        return False
    else: return True

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


