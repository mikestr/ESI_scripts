#!/usr/bin/env python3
# This script separates an EFTEM tilt series with two images per
# tilt into two tilt series.  It requires IMOD to be installed.
# Mike Strauss, April 10th, 2012, modified Nov 4, 2023

""" This script requires an image stack named "p.mrc".  The output files
should be in the same order as the images in the stack.  (ie, if 4 images at 4 different
energies were recorded at each tilt, then 4 output files should follow the name of the input
stack.
Usage:  split-stack.py """

import os
import shlex
import sys
from io import StringIO


class WritableObject:
    def __init__(self):
        self.content = []
    def write(self, string):
        self.content.append(string)

if os.path.exists('phosphorus')==0: os.mkdir('phosphorus')
if os.path.exists('nitrogen')==0: os.mkdir('nitrogen')

""" Change the input file name and output file names if you don't want the default."""

input_file='p.mrc'
output_files=['phosphorus/P-a.st','phosphorus/P-b.st','nitrogen/N-a.st','nitrogen/N-b.st']


#output_files=sys.argv[2::]

# number of images
head=str('header -size '+input_file)
s=os.popen(head).read()
sargs = shlex.split(s)
n=int(sargs[2])

#n_out=len(sys.argv)-2
n_out=len(output_files)
if n_out >= 2 :
    if n%n_out !=0:
        com3="There are "+str(n)+" images in the stack, and "+str(n_out)+" output files given."
        sys.exit(com3)


# first image 155eV loss, second image 120eV loss
for ea in range(n_out):
	r=range(ea,n,n_out)
	sections=''
	for a in r:
	    sections+=str(a)
	    if a<n-n_out: sections+=","


	sys.stdout=com1=StringIO()

	print('newstack -secs ',sections,' ',input_file,' ',output_files[ea],' ' )

	sys.stdout=sys.__stdout__

	a=com1.getvalue()
	os.system(a)
