#!/bin/sh

grep '[ 0-9.]{8,10}\*\**$' "$1"
#   data['ACCT'] = int(re.findall(r'ACCT\: ([0-9]+)', text)[0])
#   data['CD'] = re.findall(r'\n([A-Z]{2})\n', text)[0]
