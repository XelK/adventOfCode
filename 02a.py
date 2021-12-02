#!/usr/bin/env python
with open("./02.txt") as f:
    l=f.read().splitlines()

x=y=0
for n in l:
    command,value=n.split()
    if command == "forward":
        x+=int(value)
    if command == "down":
        y+=int(value)
    if command == "up":
        y-=int(value)
    
print(x*y)
