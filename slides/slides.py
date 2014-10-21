#!/usr/bin/env python3
import os
import sys
from functools import partial

from sliding_window import window

def main():
    sys.stdout.write(header)
    for directory in ['public-notice','scarsdale-assessor','prizren-zoning']:
        sys.stdout.write('\\newslide{%s}\n' % directory)
        makefile = os.path.join('..', directory, 'Makefile')
        with open(makefile) as fp:
            for title, command in makefile_to_slides(fp):
                sys.stdout.write('\\newslide{%s}\n' % title)
                sys.stdout.write('\\begin{verbatim}\n%s\n\\end{verbatim}' % command)
    sys.stdout.write(footer)

def makefile_to_slides(fp):
    for line in fp:
        if line.startswith('all') or line == '\n':
            continue
        if 'wget' in line:
            continue

        if not line.startswith('\t'):
            title = line.split(':')[0]
        else:
            tokens = line.strip().split()
            lines = tokens[0]

            for prevtoken, thistoken in window(tokens, 2):
                if prevtoken.startswith('--') and not thistoken.startswith('--'):
                    lines += ' \\\n  %s %s' % (prevtoken, thistoken)
                elif prevtoken.startswith('--') and thistoken.startswith('--'):
                    pass
                elif not prevtoken.startswith('--') and not thistoken.startswith('--'):
                    if len(lines.split('\n')[-1] + thistoken) < 15:
                        lines += ' %s' % thistoken
                    else:
                        lines += ' \\\n  %s' % thistoken
                    
            yield title, lines

header = r'''
\documentclass[12pt]{article}
\usepackage{hyperref}
\usepackage[a6paper,landscape]{geometry}
\usepackage{svg}
\newcommand\newslide[1] {
  \newpage
  \section*{#1}
}
\begin{document}
\newslide{How I parse PDF files}
\noindent Thomas Levine

\noindent \url{http://thomaslevine.com}

\newslide{Data can be represented in many ways}


\newslide{I don't know how PDFs work.}
So I convert PDFs to formats that I understand better.

\includegraphics[width=\textwidth]{intermediary-format.eps}

\newslide{Questions to ask}
\begin{itemize}
\item Do we need to read the file contents at all?
\item Do we only need to extract the text and/or images?
\item Do we care about the layout of the file?
\end{itemize}

'''

footer = r'''
\end{document}
'''

if __name__ == '__main__':
    main()
