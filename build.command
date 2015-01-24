#!/bin/bash

# Clean the bin.
rm -rf bin/*

# Copy build utilities, sources, images, and IEEE resources into bin.
cp mascots.tex bin/
cp build_dat.py bin/
cp build_gnu.py bin/
cp pseudo* bin/
cp dat/* bin/
cp -r gnu bin/
cp -r src bin/
cp -r img bin/
cp tex/* bin/

# Concatenate sources into single bibliography file in bin.
cat bib/*.bib > bin/mascots.bib

# Build the paper.
cd bin/
python build_dat.py
python build_gnu.py

pdflatex mascots
bibtex mascots
pdflatex mascots
pdflatex mascots

# Read back paper.
cp mascots.pdf ../
cd ../
