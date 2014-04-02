#!/bin/sh
fn="scarsdale-assessor-2012.txt"

sed -n 's/^\**\([ 0-9.]\{8,10\}\) \**$/\1/p' "$fn"
#   data['ACCT'] = int(re.findall(r'ACCT\: ([0-9]+)', text)[0])
#   data['CD'] = re.findall(r'\n([A-Z]{2})\n', text)[0]
