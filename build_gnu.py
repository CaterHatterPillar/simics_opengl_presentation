#!/bin/python
# Builds graphs using GNUplot.

import os
import subprocess

g_gnuHistogram = "gnu/histogram1x1.gnu"
g_gnuHistograms = "gnu/histogram2x3.gnu"
g_gnuHistogramsStacked = "gnu/histogram1x3.gnu"

# Draw 1x1 histograms:
cmd = "gnuplot -e \"arg_data='%s';arg_terminal='%s';arg_output='%s'\" " \
      + g_gnuHistogram
arg1 = "magicinstrprofileeach.dat"
arg2 = "epslatex"
arg3 = "gnuhistogrammagicinstructionsforeach.tex"

sp = subprocess.Popen(cmd % (arg1,arg2,arg3), shell=True)
sp.wait()

# Draw 3x2 histograms:
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

arg1 = "simicsphong1448x1448.dat"
arg2 = "paraphong1448x1448.dat"
arg3 = "simicsphong2048x2048.dat"
arg4 = "paraphong2048x2048.dat"
arg5 = "simicsphong2896x2896.dat"
arg6 = "paraphong2896x2896.dat"

arg7 = "1448x1448"
arg8 = "2048x2048"
arg9 = "2896x2896"

arg10 = "epslatex"
arg11 = "gnuhistogramssimicsparaphong.tex"
sp = subprocess.Popen(cmd % (arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10,
                             arg11), shell=True)
sp.wait()

# Draw 3x1 histograms:
cmd = "gnuplot -e \"arg_data1='%s';arg_data2='%s';arg_data3='%s';arg_title1='%s';arg_title2='%s';arg_title3='%s';arg_terminal='%s';arg_output='%s'\" " + g_gnuHistogramsStacked;

arg1 = "hostchess84x84.dat"
arg2 = "hostjulia450.dat"
arg3 = "hostphong2048x2048.dat"
arg4 = "Chess"
arg5 = "Julia"
arg6 = "Phong"
arg7 = "epslatex"
arg8 = "gnuhistogramshost.tex"
sp = subprocess.Popen(cmd % (arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8),
                      shell=True)
sp.wait()

arg1 = "qemuchess84x84.dat"
arg2 = "qemujulia450.dat"
arg3 = "qemuphong2048x2048.dat"
arg4 = "Chess"
arg5 = "Julia"
arg6 = "Phong"
arg7 = "epslatex"
arg8 = "gnuhistogramsqemu.tex"
sp = subprocess.Popen(cmd % (arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8),
                      shell=True)
sp.wait()
