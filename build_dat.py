#!/bin/python
# Build script compiling and copying results .dat-segments into build directory

import os
import glob
import numpy
import shutil
import fileinput
from decimal import *

class Keyval:
    def __init__(self, p_min, p_max, p_avg, p_std):
        self.m_min = p_min
        self.m_max = p_max
        self.m_avg = p_avg
        self.m_std = p_std

def avg(p_filename):
    file = open(p_filename, 'r')

    mss = []
    for line in file:
        ms = float(line)
        mss.append(ms)
    msavg = numpy.average(mss)
    msstd = numpy.std(mss)
    msmin = numpy.min(mss)
    msmax = numpy.max(mss)

    file.close()
    return Keyval(msmin, msmax, msavg, msstd)
    return msavg

def correct_profiling(p_filename, p_offset):
    mss = []

    avgBefore = avg(p_filename)

    file = open(p_filename, 'r+')
    for line in file:
        ms = float(line)
        mss.append(ms)
    file.truncate() # Clear file contents.
    file = open(p_filename, 'w')
    for ms in mss:
        ms = ms + p_offset
        file.write(str(ms) + '\n')
    file.close()

    avgAfter = avg(p_filename)

    print('Offset profiling measurements in ' + p_filename + ' with '
          + str(p_offset) + ', effectively reducing the average from '
          + str(avgBefore.m_avg) + ' to ' + str(avgAfter.m_avg) + '.')

def sort_file(p_filename):
    mss = []

    file = open(p_filename, 'r+')
    for line in file:
        ms = float(line)
        mss.append(ms)
    file.truncate() # Clear file contents.

    mss = sorted(mss)
    msMax = max(mss)
    msMin = min(mss)

    file = open(p_filename, 'w')
    for ms in mss:
        file.write(str(ms) + '\n')
    file.close()

    print('Sorted file ' + p_filename + ' with minimum entry '
          + str(msMin) + ' and maximum entry ' + str(msMax) + '.')
    
def keyval_create(p_filename, p_val):
    val_rounded = Decimal(str(p_val)).quantize(Decimal(10) ** -0)
    print('Creating keyval file ' + p_filename + ' with value '
          + str(val_rounded) + '...')
    file = open(p_filename, 'w')
    file.write(str(val_rounded)) # No endline.
    file.close()

def keyval_extract(p_filename):
    keyval = avg(p_filename)
    keyval_create(p_filename + '.min', keyval.m_min)
    keyval_create(p_filename + '.max', keyval.m_max)
    keyval_create(p_filename + '.avg', keyval.m_avg)
    keyval_create(p_filename + '.std', keyval.m_std)

# The profiling method used to measure elapsed time on the Simics
# platform, that is the platform used to collect results for the
# simics- and para- prefixes, is expected to carry with it some
# measurement overhead (see thesis.pdf). We compile the expected
# outcome of this overhead, and compile new results, from the raw
# results based off of this overhead.
profiling_overhead = avg('profile.dat')

# Sort profiling overhead analysis for the purposes of visualizing
# error deviations minimum and maximum:
sort_file('profile.dat')

files_need_correcting = glob.glob('simics*.dat')
files_need_correcting += glob.glob('para*.dat')
files_need_correcting += glob.glob('magicinstrprofile*.dat')
for filename in files_need_correcting:
    correct_profiling(filename, -profiling_overhead.m_avg)

files_need_keyval_extract = glob.glob('*.dat')
for filename in files_need_keyval_extract:
    keyval_extract(filename)
