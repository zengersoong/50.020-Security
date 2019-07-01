#!/usr/bin/python3

import hashlib
import itertools
from timeit import default_timer as timer
dgts = set()
f5 =open('hash5.txt')
for d in f5:
    dgts.add(d.strip())
f5.close()

fout = open('FOUND.txt', 'w')
foundCount = 0
digits = '0123456789'
fin = open('words5.txt')
checkedCharSet = set()
alreadyChecked = set()
wc = 0

start = start = timer()
for w in fin:
    wc += 1
    print(wc)
    w = w.strip()
    sortedchars = tuple(sorted(w))  # If the character are the same, skip
    if sortedchars in checkedCharSet:
        continue
    else:
        checkedCharSet.add(sortedchars)

    for t in itertools.permutations(w+digits, 5):
        ww = ''.join(t)
        if ww in alreadyChecked:
            continue
        md5 = hashlib.md5(ww.encode('ascii')).hexdigest()
        if md5 in dgts:
            print('------>found:', ww)
            print(ww, '-->', md5, file=fout, flush=True)
            foundCount += 1
            if foundCount == 15:
                break
        alreadyChecked.add(ww)

end = timer()
print("The time it takes to run is {} seconds.".format(end-start))