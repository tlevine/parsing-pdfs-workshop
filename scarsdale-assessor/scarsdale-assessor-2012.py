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

def parse_line_3(line):
    return {
        'name': line[:27],
        'acreage': line[27:71],
        'village-tax': line[71:],
    }

for row in rows(fp):
    print(parse_line_3(row[3]))
