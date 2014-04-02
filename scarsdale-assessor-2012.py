#!/usr/bin/env python3
import struct

fp = open('scarsdale-assessor-2012.txt','r')

def rows(fp):
    row = []
    for line in fp:
        row.append(line)
        if '***' in line:
            yield row
            row = []

fwfstruct = struct.Struct('%027s%042s%042s')

r = list(rows(fp))

print(fwfstruct.parse(r[2][3]))

