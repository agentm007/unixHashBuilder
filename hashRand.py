#!/usr/bin/python3
import random
import os
import subprocess
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-l", "--length", type=int, default=8, help="An integer setting the length of password hash")
parser.add_argument("-c", "--charset", default="let", choices=["let", "num", "spc"], help="The character set that you wish to use. let for upercase and lowercase letters, num for letters and numbers, and spc for special characters")  
parser.add_argument("-v", "--verbose", action="store_true", help="Displays the length and character set used for the hash.")
args = parser.parse_args()

SELECTION = args.charset
LENGTH = args.length


def generateHash(charset, length):
    nums = range(48,58)
    lowerCase = range(65,91)
    upperCase = range(97,123)

    if(charset == "let"):
        value = ""
        for i in range(length):
            value += chr(random.randint(48,57))
        subprocess.call(["mkpasswd", "-m", "sha-512", value])
    elif(charset == "num"):
        value = ""
        characterset = []
        characterset.extend(nums)
        characterset.extend(lowerCase)
        characterset.extend(upperCase)
        for i in range(length):
            value += chr(random.choice(characterset))
        subprocess.call(["mkpasswd", "-m", "sha-512", value])
    elif(charset == "spc"):
        value = ""
        characterset = []
        characterset.extend(range(32,127))
        for i in range(length):
            value += chr(random.choice(characterset))
        subprocess.call(["mkpasswd", "-m", "sha-512", value])
    else:
        print("Option not Valid")

if(args.verbose):
    char_set = {"let":"uppercase and lowercase letters", "num":"letters and numbers", "spc":"letters, numbers and special characters"}
    if(args.length > 0):
        print("The hash was made using " + char_set[args.charset] + " and is " + str(args.length) + " characters long.")
    else:
        print("The hash was made using " + char_set[args.charset] + " and is 0 characters long.")

generateHash(SELECTION, LENGTH)
