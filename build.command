#!/bin/bash

# Clean the bin.
rm -rf bin/*

# Copy build utilities, sources, images, and IEEE resources into bin.
cp simics_opengl_presentation.tex bin/
cp build_dat.py bin/
cp build_gnu.py bin/
cp histogram2x3.gnu bin/
cp dat/* bin/
cp -r src bin/

# Build the paper.
cd bin/
python build_dat.py
python build_gnu.py

pdflatex simics_opengl_presentation
bibtex simics_opengl_presentation
pdflatex simics_opengl_presentation
pdflatex simics_opengl_presentation

# Read back paper.
cp simics_opengl_presentation.pdf ../
cd ../
