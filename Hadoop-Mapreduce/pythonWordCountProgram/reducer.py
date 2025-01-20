#!/usr/bin/env python3
import sys

last_key, count = None, 0
for line in sys.stdin:
    key, value = line.strip().split("\t")
    if last_key and last_key != key:
        print(f"{last_key}\t{count}")
        last_key, count = key, int(value)
    else:
        last_key, count = key, count + int(value)

# Don't forget to output the last key-value pair
if last_key:
    print(f"{last_key}\t{count}")

