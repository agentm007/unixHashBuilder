#!/usr/bin/python2.7
import random
import os
import subprocess


NUMBERS = 1
LETTERS = 2
SPECIAL = 3

def generateHash(charset, length):
    nums = range(48,58)
    lowerCase = range(65,91)
    upperCase = range(97,123)

    if(charset == 1):
        value = ""
        for i in range(length):
            value += chr(random.randint(48,57))
        subprocess.call(["mkpasswd", "-m", "sha-512", value])
    elif(charset == 2):
        value = ""
        characterset = []
        characterset.extend(nums)
        characterset.extend(lowerCase)
        characterset.extend(upperCase)
        for i in range(length):
            value += chr(random.choice(characterset))
        subprocess.call(["mkpasswd", "-m", "sha-512", value])
    elif(charset == 3):
        value = ""
        characterset = []
        characterset.extend(range(32,127))
        for i in range(length):
            value += chr(random.choice(characterset))
        subprocess.call(["mkpasswd", "-m", "sha-512", value])
    else:
        print "Option not Valid"


generateHash(NUMBERS, 8)
