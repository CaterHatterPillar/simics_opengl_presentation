#!/bin/bash

cat bib/*.bib > mascots.bib

pdflatex mascots

bibtex mascots

pdflatex mascots
pdflatex mascots
