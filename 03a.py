#!/usr/bin/env python
#FILE="./03_test.txt"
FILE="./03.txt"
with open(FILE) as f:
    l=f.read().splitlines()

gamma=""
epsilon=0

for bit in range(12):
    NumberOne=0
    for n in l:
        if n[bit] == "1":
            NumberOne+=1

    if NumberOne>len(l)/2:
        gamma+="1"
    else:
        gamma+="0"

epsilon=gamma.replace("1","2")
epsilon=epsilon.replace("0","1")
epsilon=epsilon.replace("2","0")

print(int(gamma,2)*int(epsilon,2))
