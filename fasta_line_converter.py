#!/usr/bin/env python

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="convert .fasta having sequence on multiple lines to .fasta \
    having 1 header line and 1 sequence line.")
    parser.add_argument("-f", "--file", help="Input .fasta file to read from", type=str)
    return parser.parse_args()
args = get_args()

IN_FILE = args.file
OUT_FILE = IN_FILE[:((len(IN_FILE))-5)]+".fasta"

with open(OUT_FILE, "w") as outfile:
    with open(IN_FILE, "r") as infile:
        count = 0
        for line in infile:
            if count < 1:
                outfile.write(line)
                count += 1
            else:
                if ">" in line:
                    outfile.write("\n")
                    outfile.write(line)
                else:
                    outfile.write(line.strip())
