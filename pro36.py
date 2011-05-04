#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro36.py
# Description: 

def isPali(s):
    l=len(s)

    for index,v in enumerate(s):
	if v!=s[l-1-index]:
	    return False
    return True

s=0
for i in range(1000000):
    if isPali(str(i)) and isPali(bin(i)[2:]):
	s +=i

print s
