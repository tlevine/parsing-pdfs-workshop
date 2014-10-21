#!/usr/bin/env python3
import os
import sys
from functools import partial

def main():
    sys.stdout.write(header)
    for directory in ['public-notice','scarsdale-assessor','prizren-zoning']:
        sys.stdout.write('\sectionslide{%s}\n' % directory)
        makefile = os.path.join('..', directory, 'Makefile')
        with open(makefile) as fp:
            for title, command in makefile_to_slides(fp):
                sys.stdout.write('\slide{%s}{%s}\n' % (title, command))
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
\newcommand\sectionslide[1] {
  \newpage
  \section{#1}
}
\newcommand\slide[2] {
  \newpage
  \subsection{#1}
  \texttt{#2}
}
\begin{document}
'''

footer = r'''
\end{document}
'''

if __name__ == '__main__':
    main()
