#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro29.py
# Description: 


d={}
for a in range(2,101):
    for b in range(2,101):
	d[a**b]=1

print len(d.keys())
