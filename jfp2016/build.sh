#!/bin/sh
pdflatex fp-jfp.tex
bibtex fp-jfp
pdflatex fp-jfp.tex
pdflatex fp-jfp.tex
