# 50.020-Security

## Lab 1
### Introduction to Shiftciphers
Instructor(s): Professor Tang Zhaohui
#### 1. Shift Cipher for printable input
Writing a code that can run from command prompt or shell as the following.  
  
__*./shiftcipher.py -i [input filename] -o [output filename] -k [key]*__
-m [mode]  
Code is in file ex1.py
Contains code for both encoding and decoding.

#### 2.Part II: Shift Cipher for binary input
1. Similar to part 1 however now using binary inputs and have to account for bit overflow.  
2. Strategy was to remove the extra bit when it overflows past 255 when shifting/encoding. Using "AND" operator to remove the overflow.     
__*oc = ( ic + shift ) & 0xff*__   
3. Strategy for decoding, minus away the key, if it is negative, add back 0x100 that was removed from overflow during encoding.


#### 3. Part III: Break Shift Cipher of flag
1. Given a encoded flag that has been shifted, use the decoder written in part II to decipher it.  
2. Since key can be from 0-255, just run the decoder until the file becomes a PNG recognisable file using command line tool "file" to check after each run.
3. This I have done in 3 ways, using bash shell scripting in two different forms, ex3.sh, ex3v2.sh as well as writing a script in python3 using the Os library, to run shell commands.
4. Pipe the output of the File command line tool to check for PNG using GREP, repeat the decoding by incrementing the key until Flag.png is decoded to a PNG format.

### Check the LAB1REPORT.PDF for more information on how to run the codes.

