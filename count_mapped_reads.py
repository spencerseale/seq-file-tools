#!/usr/bin/env python

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Count number of mapped reads vs unmapped reads in .sam file.")
    parser.add_argument("-f", "--file", help="Input .sam file to read from", type=str)
    return parser.parse_args()
args = get_args()

FILE = args.file

with open(FILE, "r") as openfile:
    LN = 0
    mapped = 0
    unmapped = 0
    for line in openfile:
        line = line.strip()
        LN += 1
        if "@" not in line[0]:
            FLAG = line.split()[1]
            #print(FLAG)
            if((int(FLAG) & 4) != 4):
                if((int(FLAG) & 256) != 256):
                    mapped += 1
            else:
                unmapped += 1

print("reads mapped:", mapped)
print("reads unmapped:", unmapped)
