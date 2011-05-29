#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro97.py
# Description: 

base=1e10;

def mypow(a,b,base):
    if (b==0):
	return 1
    if (b==1):
	return a%base
    
    if (b%2==1):
	return (a*mypow(a,b-1,base))%base
    return (mypow(a,b/2,base)*mypow(a,b/2,base))%base

print mypow(2,10,1e2)
print (28433*mypow(2,7830457,base)+1)%base
