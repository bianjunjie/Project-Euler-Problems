#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro52.py
# Description: 

def sameInteger(x,y):
    if set(str(x))==set(str(y)):
	return True
    return False
def solve():
    x=1
    while True:
	x2=x*2
	if sameInteger(x,x2):
	    x3=x*3
	    if sameInteger(x,x3):
		x4=x*4
		if sameInteger(x,x4):
		    x5=x*5
		    if sameInteger(x,x5):
			x6=x*6
			if sameInteger(x,x6):
			    print x
			    return
        x=x+1
	

solve()
