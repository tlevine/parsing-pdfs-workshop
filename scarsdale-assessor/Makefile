all: scarsdale-assessor-2012.txt scarsdale-assessor-2012-layout.txt scarsdale-assessor-2012.html scarsdale-assessor-2012.xml scarsdale-assessor-2012-page1.svg

scarsdale-assessor-2012.txt:
	pdftotext scarsdale-assessor-2012.pdf
scarsdale-assessor-2012-layout.txt:
	pdftotext -layout scarsdale-assessor-2012.pdf scarsdale-assessor-2012-layout.txt
scarsdale-assessor-2012.html:
	pdftohtml scarsdale-assessor-2012.pdf
scarsdale-assessor-2012.xml:
	pdftohtml -xml scarsdale-assessor-2012.pdf
scarsdale-assessor-2012-page1.svg:
	inkscape --without-gui --export-plain-svg scarsdale-assessor-2012-page1.svg scarsdale-assessor-2012.pdf
scarsdale-assessor-2012-page88.pdf:
	pdftk scarsdale-assessor-2012.pdf cat 88 output scarsdale-assessor-2012-page88.pdf
scarsdale-assessor-2012-page88.svg: scarsdale-assessor-2012-page88.pdf
	inkscape --without-gui --export-plain-svg scarsdale-assessor-2012-page88.svg scarsdale-assessor-2012-page88.pdf
