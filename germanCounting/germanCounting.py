#encoding: UTF-8

import os
import random

base=["null",
        "ein",
        "zwei",
        "drei",
        "vier",
        "fünf",
        "sechs",
        "sieben",
        "acht",
        "neun",
        "zehn"]

key=1
while (key != "0"):
    number = str(random.randint(0,100))
    print(number, end="")
    key = input("")
    if number == "1":
        print(" - eins")
    elif len(number)==1:
        print(base[int(number)])
    elif len(number)==2:
        if number[1]=="0":
            if number[0]=="1":
                print(" - "+base[int(number)])
            elif number[0]=="6":
                print(" - sechzig")
            elif number[0]=="7":
                print(" - siebzig")
            elif number[0]=="3":
                print(" - dreiszig")
            elif number[0]=="2":
                print(" - zwanzig")
            else:
                print(" - " + base[int(number[0])]+"zig")
        elif number[0]=="1":
            if number[1]=="1":
                print(" - elf")
            elif number[1]=="2":
                print(" - zwölf")
            elif number[1]=="6":
                print(" - sechzehn")
            elif number[1]=="7":
                print(" - siebzehn")
            else:
                print(" - " + base[int(number[1])]+"zehn")
        elif number[0]=="2":
                print(" - " + base[+int(number[1])]+"undzwanzig")
        elif number[0]=="6":
            print(" - " + base[+int(number[1])]+"undsechzig")
        elif number[0]=="7":
            print(" - " + base[int(number[1])]+"undsiebzig")
        elif number[0]=="3":
            print(" - " + base[int(number[1])]+"unddreiszig")
        else:
            print(" - " + base[int(number[1])]+"und"+base[int(number[0])]+"zig")
    elif len(number)==3:
        print("- ein hundert")


