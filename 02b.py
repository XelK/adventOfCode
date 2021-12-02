#!/usr/bin/env python
#FILE="./02_test.txt"
FILE="./02.txt"
with open(FILE) as f:
    l=f.read().splitlines()

x=y=aim=0
for n in l:
    command,value=n.split()
    if command == "forward":
        x+=int(value)
        y+=aim*int(value)
    if command == "down":
        aim+=int(value)
    if command == "up":
        aim-=int(value)
    
print(x*y)
