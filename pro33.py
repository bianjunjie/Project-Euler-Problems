#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro33.py
# Description: 

for a in range(1,10):
    for b in range(1,10):
	for d in range(1,10):
	    if (10*a+b)*d == (10*b+d)*a and a!=d:
		print 10*a+b,10*b+d
	    if (10*a+b)*d == (10*d+a)*b and b!=d:
		print 10*a+b,10*d+a

