#!/usr/bin/env python3
import os
import sys
from functools import partial

from sliding_window import window

def main():
    sys.stdout.write(header)
    for directory in ['public-notice', 'prizren-zoning']:
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
\newslide{How I get information out of PDF files}
\noindent Thomas Levine

\noindent \url{http://thomaslevine.com}

% You just heard a lot about some wonderful things people are doing
% in relation to sharing information. There are a lot of ways we can
% store information in computer files, so we often need to convert
% data between different formats. So I'm going to give you a little
% taste of that process.

% PDF files are very popular. My slides, for example, are in PDF format.
% PDF files are nice for printing out on paper. They're not very helpful
% if you want to make graphs from the information in the PDF. I'm going
% to show you how I take information out of PDF format files so I can
% use it for other purposes.

% The first thing we need to realize is that
\newslide{Data can be represented in many ways}
Three representations of the same data (from \url{http://treasury.io})
\begin{itemize}
\item Weird text files: \url{http://www.fms.treas.gov/dts/index.html}
\item SQL: \url{http://treasury.io}
\item \href{http://small.dada.pink/gastronomification-big-data-talk/fms-symphony.webm}{Music video}
\end{itemize}

\newslide{We can read PDFs in many ways.}
Your program will be different depending on the data you want.

\newslide{I don't know how PDFs work.}
So I convert PDFs to formats that I understand better.

\includegraphics[width=\textwidth]{intermediary-format.eps}

\newslide{Which program do I use for the first step?}
It depends on the data I want.

\newslide{What data do I want?}
\begin{itemize}
\item Do we need to read the file contents at all?
\item Do we only need to extract the text and/or images?
\item Do we care about the layout of the file?
\end{itemize}

\newslide{I like to sleep.}
I choose try to do things the easiest or fastest way possible
because I would rather have time to sleep.

\newslide{Do we need to read the file at all?}
Some filenames
\begin{itemize}
\item 06072900.txt
\item 06073000.txt
\item 06080100.txt
\item 13020400.txt 
\item 13020500.txt 
\item 13020600.txt 
\end{itemize}
The filenames are dates (\texttt{yymmdd00.txt}).

If I just want the date, I don't need to look into the file.
'''

footer = r'''
\newslide{One thing to remember}
If you remember nothing else, remember this.
\begin{quotation}
\LARGE\bfseries\centering\noindent
You have the power to take things apart and make new things.
\end{quotation}
PDF files are complicated, but they are not magic. You can take
them apart and make something new with them. (It might just take a while.)

It's not just PDFs files; everything in the world (even atoms)
can be broken up into smaller pieces and turned into something new.

\newslide{Hands-on section}
Now you're going to try running these programs!

\end{document}
'''

if __name__ == '__main__':
    main()
