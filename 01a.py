#!/usr/bin/env python
with open("./01.txt") as f:
    l=f.read().splitlines()

last=None
inc=0
for n in l:
    if last and int(n)>last:
        inc+=1
    last=int(n)

print(inc)
