#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro125.py
# Description: 

from commonFunc import *
from datetime import *

t1=datetime.now()

max_n=8000


pali=set()
for n in range(1,max_n):
    m=n-2
    while m>=0:
	r=n*(n+1)*(2*n+1)/6-m*(m+1)*(2*m+1)/6
	if r<1e8 and isPali(r):
	    pali.add(r)
	if r>1e8:
	    break
	m-=1

print sum(pali)
print datetime.now()-t1
