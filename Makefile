pdf:
	cp /home/moorepants/Manuscripts/inverted-pendulum-sys-id-paper/figures/trajectory-comparison.pdf figures/
	cp /home/moorepants/Manuscripts/inverted-pendulum-sys-id-paper/figures/free-body-diagram.* figures/
	cp /home/moorepants/Manuscripts/inverted-pendulum-sys-id-paper/tables/sample-relative-error.tex tables/
	cp /home/moorepants/Manuscripts/inverted-pendulum-sys-id-paper/references.bib .
	pdflatex abstract.tex
	bibtex abstract.aux
	pdflatex abstract.tex
	pdflatex abstract.tex
clean:
	(rm -rf *.ps *.log *.dvi *.aux *.*% *.lof *.lop *.lot *.toc *.idx *.ilg *.ind *.bbl *.blg *.cpt)
