#!/bin/bash

# Clean the bin.
rm -rf bin/*

# Copy build utilities, sources, images, and IEEE resources into bin.
cp beamerthemeIntel.sty bin/
cp footline_background.png bin/
cp title_background.png bin/
cp simics_opengl_presentation.tex bin/
cp build_dat.py bin/
cp build_gnu.py bin/
cp histogram2x3.gnu bin/
cp dat/* bin/
cp src/* bin/
cp img/* bin/

# Build the paper.
cd bin/
python build_dat.py
python build_gnu.py

pdflatex simics_opengl_presentation
pdflatex simics_opengl_presentation
pdflatex simics_opengl_presentation

# Read back paper.
cp simics_opengl_presentation.pdf ../
cd ../
