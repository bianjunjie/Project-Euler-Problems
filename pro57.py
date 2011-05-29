#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro57.py
# Description: 


m=3
n=2

r=0
for i in range(2,1001):
    new_m=m+2*n
    new_n=m+n

    if len(str(new_m)) > len(str(new_n)):
	r+=1
    m=new_m
    n=new_n

print r

    

