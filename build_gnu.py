#!/bin/python
# Builds graphs using GNUplot.

import os
import subprocess

g_gnuHistograms = "histogram2x3.gnu"
cmd = "gnuplot -e \"arg_data1='%s';arg_data2='%s';arg_data3='%s';arg_data4='%s';arg_data5='%s';arg_data6='%s';arg_ylabel1='%s';arg_ylabel2='%s';arg_ylabel3='%s';arg_terminal='%s';arg_output='%s'\" " + g_gnuHistograms;

arg1 = "simicschess60x60.dat"
arg2 = "parachess60x60.dat"
arg3 = "simicschess84x84.dat"
arg4 = "parachess84x84.dat"
arg5 = "simicschess118x118.dat"
arg6 = "parachess118x118.dat"

arg7 = "60x60"
arg8 = "84x84"
arg9 = "118x118"

arg10 = "epslatex"
arg11 = "gnuhistogramssimicsparachess.tex"
sp = subprocess.Popen(cmd % (arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10,
                             arg11), shell=True)
sp.wait()

arg1 = "simicsjulia225.dat"
arg2 = "parajulia225.dat"
arg3 = "simicsjulia450.dat"
arg4 = "parajulia450.dat"
arg5 = "simicsjulia900.dat"
arg6 = "parajulia900.dat"

arg7 = "225"
arg8 = "450"
arg9 = "900"

arg10 = "epslatex"
arg11 = "gnuhistogramssimicsparajulia.tex"
sp = subprocess.Popen(cmd % (arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10,
                             arg11), shell=True)
sp.wait()
