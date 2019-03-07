##################################
#####   I decided to write   #####
#####  this code while i'm   #####
#####   drunk on a saturday  #####
#####   night. I'm sorry     #####
#####   for any mistake :)   #####
##################################

#
# I noticed it is not being able
#to evaluate names where there is a
#letter that appears more than one
#time. :(
#
#I'm going to try to fix it soon :)
# FIXED!! :D

# Also, as it is a stochastic algorithm
#it may take some time untill it find
#all the possible anagrams.
# Hence, sometimes it reach the time
#limit of the soloLearn interpretator.
#just run it again and it'll' converge
#sometime. I tested names until 6
#characters and with no repetition.

import random

name=input("What's your name?\n")

def facto(n):
    result=1
    for k in range(n):
        result*=(k+1)
    return result
        
nPoss = facto(len(name))

nameCount = name[:]

for k in name:
    nRep = nameCount.count(k)
    if k != '@':
        nPoss /= facto(nRep)
    nameCount = nameCount.replace(k, '@')

print("there are {0:d} possible anagrams using  {1}\n".format(int(nPoss), name))

print("All the possible are:")

poss=""
allPoss=[]
while len(allPoss) != nPoss:
    while len(poss) != len(name):
        new=random.randint(0,len(name)-1)
        c = name[new]
        if poss.count(c) < name.count(c):
            poss+=name[new]
    if poss not in allPoss:
        allPoss.append(poss)
    poss=""
        
print(allPoss)