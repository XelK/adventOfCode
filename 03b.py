#!/usr/bin/env python
#FILE="./03_test.txt"
FILE="./03.txt"
with open(FILE) as f:
    l=f.read().splitlines()

gamma=""
epsilon=0

print("---- OXYGEN ----")
list_ok=l.copy()
for bit in range(12):
    NumberOne=0
    list_one=[]
    list_zero=[]
    #print(f"### {bit}: {list_ok} ###\n")
    for n in list_ok:
        if n[bit] == "1":
            NumberOne+=1
            list_one.append(n)
        else:
            list_zero.append(n)

    if NumberOne>=len(list_ok)/2:
        list_ok=list_one.copy()
    else:
        list_ok=list_zero.copy()

print(list_ok)
oxygen=int(list_ok[0],2)
print(oxygen)

print("---- CO2 ----")
list_ok=l.copy()
for bit in range(12):
    NumberOne=0
    list_one=[]
    list_zero=[]

    if len(list_ok)==1:
        break

    print(f"### {bit}: {list_ok}###\n")
    for n in list_ok:
        if n[bit] == "1":
            NumberOne+=1
            list_one.append(n)
        else:
            list_zero.append(n)

    if NumberOne<len(list_ok)/2:
        list_ok=list_one.copy()
    else:
        list_ok=list_zero.copy()

#    if len(list_ok)==1:
#        break


print(list_ok)
co2=int(list_ok[0],2)
print(co2)

print(oxygen*co2)
