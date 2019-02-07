#!/bin/bash

k=0
while (( k < 256 ))
do
  python3 ex2.py -i flag -o flagout.png -k $k -m d
  if file flagout.png | grep PNG; then
     echo key = $k
     break
  fi
  (( k += 1 ))
done
