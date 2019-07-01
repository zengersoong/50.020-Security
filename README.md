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

## Lab 2 
### Introduction to substitution ciphers
Instructor(s): Professor Tang Zhaohui
### 1. Decipher a substition ciphered text
Write a python program or script to analyse the ciphered text. (E.g Frequency analysis) etc  
### 2. OTP messages Integrity 
1. Extend the python script to call option 2 "OTP". You will obtain a ciphertext again, encrypted
with an OTP.
2. Try simply returning the ciphertext to the API, you should see a message about the decrypted
and parsed content of the message.
3. Implement a solution to manipulate the ciphertext to change the message decrypted by the
API. In particular, use the techniques discussed in class to change the student ID to your
own student ID, and the points reported to 4.

## Lab 3  
### MD5 and Rainbow Tables  
Instructor(s): Professor Tang Zhaohui  
## 1. Hashing Password using MD5  
Generate the MD5 hash using python and bash commands.  
## 2. Brute-force and dictionary attack  
Write a python script named md5fun to break 15 ciphered text passwords, they only contain 5 lowercase and or numeric characters.  
## 4. Creating Rainbow Tables  
Using rainbowcrack program to generate and crack the 15 hashed passwords.  
## 5. Salting  
Appending one random lowercase character as salt value to all the elements of the list of passwords cracked in the previous part of this exercise.  
1. Generate a new rainbow table using rtgen (with new parameters) to break the hash values.
As before, sort the table using rtsort.
2. Compare the timing of the new table generation and lookup vs the previous values
3. Try to break as many salted hashes as possible.  
## 6. Hash breaking compeition . 
1. Try to break as many salted hashes as possible, difficulty separated to three different categories, easy intermediate and hard. 

## Lab 4  
### Web Security
Instructor(s): Professor Tang Zhaohui  
## 0. Solutions  
All solutions will be in my pdf file, and code used is in the same folder.
## 1. SQL injection 
Break into alice@alice.com's account without password using SQL injection. The server is provided lab4server.py.  
Change the code such that you can stop the same SQL injection form happening.
## 2. Cross-site scripting  
1. Your goal is to inject some code on a page that the admin user will look at
2. Your injected code (HTML or .js) should make the admin disclose his cookie to you
3. In particular, assume that the admin sees a list of all news when he logs in
Some suggested steps of conducting a persistent XSS attack:
4. Find a way to inject a simple XSS string into the database
5. Exploit this to obtain a victim’s session cookie and disclose the cookie as a public news.
Some hints (assume the victim is admin):
– Update your XSS to trick the admin’s browser to do an HTTP GET to a URL of the
attacker’s choice
– Make the admin visit http://localhost:5005/news?text=<adminsessioncookie>
– This will create a public news entry with the admin’s session cookie displayed.
• Test the persistent XSS works (again, assume the victim is admin):
– Login as admin: use the second password from the secrets to log in.
– Logout (as admin) after displaying the main site.
– Login as alice again.
– Your XSS attack works if you (alice) are able to see a news item with admin’s cookie
displayed!
### 3. Persistent (Second-order) attack using XSS
### 4. Reflected (First-order) attack using XSS
### 5. Command Injection  
### 6. Reverse Shell  
1. Get a local shell on the target server
2. A "reverse shell" is a program started on the victim machine, that connects to the attacker
(to pass through firewalls and similar).
3. We need a program waiting on your machine to accept incoming connections. Netcat can
be a good tool for you: use Netcat on your machine (attacker) to open a listener
4. Find a suitable command to run on the victim (the webserver, in this case, also localhost)
to connect a shell to your machine. After the victim connects to you, you should be able
to type commands, which will be executed on the victim’s machine.
