
import os
for k in range(256):
  os.system('python3 ex2.py -i flag -o flagout.png -k {} -m d'.format(k))
  ret = os.system('file flagout.png | grep -q PNG')
  if ret == 0:
     print("Found, key =", k)
     break

