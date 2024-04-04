#!/usr/bin/env python
# This script separates an EFTEM tilt series with two images per
# tilt into two tilt series.
# Mike Strauss, April 8th, 2010, modified Nov 22, 2023

from EMAN2 import *
from sparx import *
import os
import shlex
import sys
from numpy import *


input_file1='phosphorus/P-a_preali.mrc'
input_file2=['phosphorus/P-b_preali.mrc','nitrogen/N-a_preali.mrc','nitrogen/N-b_preali.mrc']


img1=EMData()
img1.read_image(input_file1)
for ifx in input_file2:
	img2=EMData()
	img2.read_image(ifx)
	nx=img2.get_attr('nx')
	ny=img2.get_attr('ny')
	# number of images
	n=img2.get_attr('nz')
	print(n)

	mask_ccf = model_circle(12,nx,ny,1)
	all_peaks=[]
	xf=[]

	for i in range(n):
		reg=Region(0,0,i,nx,ny,1)
		print(reg)
		s1=EMData.get_clip(img1,reg)
		s2=EMData.get_clip(img2,reg)
		s1f=filt_btwl(s1,0.06,0.15,pad=True)
		s2f=filt_btwl(s2,0.06,0.15,pad=True)
		ccf=ccfnpl(s2f,s1f,center=True)
		m_ccf = Util.muln_img(mask_ccf,ccf)
		peak = peak_search(m_ccf,1, 1, 0)
		print(peak)
		xf.append(peak[0][4:])
		all_peaks.append(peak[0])
		print(i,peak[0][4:])

	f_ifx=ifx.replace('_preali.mrc','.prexg')
	print(ifx,f_ifx)
	f = open(f_ifx)
	ob1=[]
	for line in f:
		l=line.split()
		li=[]
		for a in l:
			li.append(float(a))
		ob1.append(li)
	corr_xf=[]
	for j in range(len(ob1)):
		k=[ob1[j][0],ob1[j][1],ob1[j][2],ob1[j][3],ob1[j][4]-xf[j][0],ob1[j][5]-xf[j][1]]
		corr_xf.append(k)
		#print k

	savetxt(f_ifx, corr_xf,fmt="%9.6G", delimiter='  ')
	inp=ifx.replace('_preali.mrc','.st')
	os.system("newstack -input "+inp+" -output "+ifx+" -mo 0 -xform "+f_ifx+" -fl 2")
