prizren-zoning.pdf:
	wget -O prizren-zoning.pdf http://ia700404.us.archive.org/12/items/Prizren_City_Data/FIL6.PDF
prizren-zoning.txt:
	pdftotext prizren-zoning.pdf
prizren-zoning-layout.txt:
	pdftotext -layout prizren-zoning.pdf prizren-zoning-layout.txt
prizren-zoning.html:
	pdftohtml prizren-zoning.pdf
prizren-zoning.xml:
	pdftohtml -xml prizren-zoning.pdf
prizren-zoning.svg:
	inkscape --without-gui --export-plain-svg prizren-zoning.svg prizren-zoning.pdf
