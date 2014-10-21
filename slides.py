#!/usr/bin/env python3
import sys
from functools import partial

def main():
    sys.stdout.write(header)
    for directory in ['public-notice','scarsdale-assessor','prizren-zoning']:
        makefile = os.path.join(directory, 'Makefile')
        with open(makefile) as fp:
            for title, command in makefile_to_slides(fp):
                sys.stdout.write('\slide{%s}{%s}' % (title, command))
    sys.stdout.write(footer)

def makefile_to_slides(fp):
    for line in fp:
        if line.startswith('all') or line == '\n':
            pass
        if not line.startswith('\t'):
            title = line.split(':')[0]
        else:
            yield title, line.strip()

header = r'''
\documentclass[a4paper,landscape]{article}
\newcommand\slide
\begin{document}
'''

footer = r'''
\end{document}
'''
