.PHONY: slides.tex

view: slides.pdf
	evince --presentation slides.pdf
intermediary-format.eps:
	inkscape -z --export-eps=intermediary-format.eps intermediary-format.svg
slides.tex: intermediary-format.eps
	./slides.py > slides.tex
slides.pdf: slides.tex
	pdflatex slides
