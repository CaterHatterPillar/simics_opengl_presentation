#!/bin/bash

# Clean the bin.
rm -rf bin/*

# Copy build utilities, sources, images, and IEEE resources into bin.
cp simics_opengl.tex bin/
cp build_dat.py bin/
cp build_gnu.py bin/
cp histogram2x3.gnu bin/
cp dat/* bin/
cp -r src bin/
cp tex/* bin/

# Concatenate sources into single bibliography file in bin.
cat bib/*.bib > bin/simics_opengl.bib

# Build the paper.
cd bin/
python build_dat.py
python build_gnu.py

pdflatex simics_opengl
bibtex simics_opengl
pdflatex simics_opengl
pdflatex simics_opengl

# Read back paper.
cp simics_opengl.pdf ../
cd ../
