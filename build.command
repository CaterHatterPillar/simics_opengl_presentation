#!/bin/bash

# Clean the bin.
rm -rf bin/*

# Copy sources, images, and IEEE resources into bin.
cp mascots.tex bin/
cp -r src bin/
cp -r img bin/
cp tex/* bin/

# Concatenate sources into single bibliography file in bin.
cat bib/*.bib > bin/mascots.bib

# Build the paper.
cd bin/
pdflatex mascots
bibtex mascots
pdflatex mascots
pdflatex mascots

# Read back paper.
cp mascots.pdf ../
cd ../
