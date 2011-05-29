#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro53.py
# Description: 

def make_matrix(m,n,init=0):
    s=[init]*m;
    for i in range(m):
	s[i]=[init]*n
    return s

s=make_matrix(120,120,1);

MAX=1000000
t=0
for n in range(1,101):
    for r in range(1,n):
	s[n][r]=s[n-1][r-1]+s[n-1][r]
	if s[n][r]>MAX:
#	    print n,r
	    t+=1

for n in range(1,10):
    print n,s[n][0:n+1]
print t



