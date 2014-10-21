.PHONY: slides.tex

view: slides.pdf
	evince --presentation slides.pdf

weird-text:
	firefox --new-tab /home/tlevine/git/federal-treasury-api/tests/fixtures/13020500.txt
spreadsheet:
	libreoffice /home/tlevine/git/federal-treasury-api/tests/fixtures/13020500_t6.csv
video:
	mplayer ~/git/gastronomification-big-data-talk/fms-symphony.webm

intermediary-format.eps:
	inkscape -z --export-eps=intermediary-format.eps intermediary-format.svg
slides.tex: intermediary-format.eps
	./slides.py > slides.tex
slides.pdf: slides.tex
	pdflatex slides
