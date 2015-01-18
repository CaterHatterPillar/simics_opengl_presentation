#!/bin/bash

cat bib/bibliography.bib bib/references.bib bib/web.bib > mascots.bib

pdflatex mascots

bibtex mascots

pdflatex mascots
pdflatex mascots
