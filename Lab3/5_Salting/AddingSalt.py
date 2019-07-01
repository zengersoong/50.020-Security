import random
import string
import hashlib


def txtToList(fname):
	with open(fname, "r") as filer:
		hashlist=[]
		for line in filer:
			h = line.strip("\n")
			hashlist.append(h)
		return hashlist

def generateFileFromString(fname, strInput):
	file = open(fname, mode = 'w', encoding = 'utf-8', newline = '\n')
	file.write(strInput)
	return
#Generate a lowercase alphabet as single salt
def pourSalt():
	salt = random.choice(string.ascii_lowercase)
	return salt



def mixSalt():
	passwords = txtToList('ans.txt')
	saltedPassword = []
	passWithSalt = ''
	md5passWithSalt = ''
	for pw in passwords:
		salt = pourSalt()
		saltedPassword.append((pw, salt))
		newPassword = pw + salt
		passWithSalt += newPassword + '\n'
		md5passWithSalt += hashlib.md5(newPassword.encode('utf-8')).hexdigest() + '\n'
	generateFileFromString('md5passWithSalt.txt', md5passWithSalt)
	generateFileFromString('passWithSalt.txt', passWithSalt)

# passwords = txtToList('ans.txt')
# print(passwords)
mixSalt()