#!/usr/bin/env python
# This script separates an EFTEM tilt series with two images per
# tilt into two tilt series.
# Mike Strauss, April 8th, 2010, modified for python 3, Nov 7th, 2023

import os
import shlex
import sys
from io import StringIO


class WritableObject:
    def __init__(self):
        self.content = []
    def write(self, string):
        self.content.append(string)



input_file='p.mrc'
output_file1='155a120b-a.st'
output_file2='155a120b-b.st'

# number of images
head=str('header -size '+input_file)
s=os.popen(head).read()
sargs = shlex.split(s)
n=int(sargs[2])


even=''
odd=''
# first image 155eV loss, second image 120eV loss
r=range(n)

for a in r:
   if a%2==0:
      even+=str(a)
      if a<n-2: even+=","
   else:
      odd+=str(a)
      if a<n-1: odd+=","

sys.stdout=com1=StringIO()

print('newstack -secs ',even,' ',input_file,' ',output_file1,' ')
print('newstack -secs ',odd,' ',input_file,' ',output_file2)

sys.stdout=sys.__stdout__

a=com1.getvalue()
os.system(a)
