import hashlib
import string
from timeit import default_timer as timer
# text = 'Some text'

# m = hashlib.md5()
# m.update(b"Some text") # OR
# m.update(text.encode('UTF-8'))
# print(m.hexdigest())
key = tuple(string.ascii_lowercase+string.digits)
with open('hash5.txt', 'r') as myfile:
  data = myfile.read()
# print(data)
#Bruteforce attack Find the correpesoning input by computing the hash values for each possible combination. 
#You need only to consider passwords with 5 lowercase and or numeric characters

# m = hashlib.md5()

# 48 - 58 0-9
# 97 - 122 a-z

def createFileFromList(fname,listPass):
	with open(fname, 'w') as f:
	    for item in listPass:
	        f.write("%s\n" % item)

hashlist = []
with open("hash5.txt", "r") as my_file:
  for line in my_file:
      h = line.strip("\n")
      hashlist.append(h)

# print(hashlist)
counter=0
tried=[0,0,0,0,0]

def bruteforce():
	ans={}
	counter=0
	for a in range(len(key)):
		tried[0] = key[a]
		for b in range(len(key)):
			tried[1] = key[b]
			for c in range(len(key)):
				tried[2] = key[c]
				for d in range (len(key)):
					tried[3] =key[d]
					for e in range (len(key)):
						tried[4] = key[e]
						new_try = ''.join(tried)
						new_try_code = hashlib.md5(new_try.encode('utf-8')).hexdigest()
						print(new_try_code)
						if new_try_code in hashlist:
							print("====================================")
							print("{} : {}".format(new_try,new_try_code))
							print("====================================")
							ans[new_try]=new_try_code
							counter+=1
							if counter>=15:
								# Return a dictionary of the unciphered clear password and its cipher.
								print(ans)
								createFileFromList("ans.txt",list(ans.keys()))
								return 0
start = timer()
bruteforce()
end = timer()
print("The time it takes to run is {} seconds.".format(end-start))




