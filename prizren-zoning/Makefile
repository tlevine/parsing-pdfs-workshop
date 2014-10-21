all: prizren-zoning.txt prizren-zoning-layout.txt prizren-zoning.html prizren-zoning.xml prizren-zoning.svg

prizren-zoning.pdf:
	wget -O prizren-zoning.pdf http://ia700404.us.archive.org/12/items/Prizren_City_Data/FIL6.PDF
prizren-zoning.txt: prizren-zoning.pdf
	pdftotext prizren-zoning.pdf
prizren-zoning-layout.txt: prizren-zoning.pdf
	pdftotext -layout prizren-zoning.pdf prizren-zoning-layout.txt
prizren-zoning.html: prizren-zoning.pdf
	pdftohtml prizren-zoning.pdf
prizren-zoning.xml: prizren-zoning.pdf
	pdftohtml -xml prizren-zoning.pdf
prizren-zoning.svg: prizren-zoning.pdf
	inkscape --without-gui --export-plain-svg prizren-zoning.svg prizren-zoning.pdf
