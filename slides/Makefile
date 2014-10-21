.PHONY: slides.tex

view: slides.pdf
	evince slides.pdf
slides.tex:
	./slides.py > slides.tex
slides.pdf: slides.tex
	pdflatex slides
