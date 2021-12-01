#!/bin/env python
with open("./01.txt") as f:
    l=f.read().splitlines()

last=None
inc=0
for n in range(len(l)-2):
    s=int(l[n])+int(l[n+1])+int(l[n+2])
    if last:
        #s=sum(l[n],l[n+1],l[n+2])
        if s>last:
            inc+=1
    last=s
print(inc)
