all: public-notice.txt public-notice-layout.txt public-notice.html public-notice.xml public-notice-page1.svg

public-notice.txt:
	pdftotext public-notice.pdf
public-notice-layout.txt:
	pdftotext -layout public-notice.pdf public-notice-layout.txt
public-notice.html:
	pdftohtml public-notice.pdf
public-notice.xml:
	pdftohtml -xml public-notice.pdf
public-notice-page1.svg:
	inkscape --without-gui --export-plain-svg public-notice-page1.svg public-notice.pdf
