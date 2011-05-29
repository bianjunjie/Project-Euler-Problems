#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: commonFunc.py
# Description: 

'''
Check if a number is  a palindromic number
'''
def isPali(num):
    n=str(num)
    while len(n)>1:
	if n[0]!=n[-1]:
	    return False
	n=n[1:-1]
    return True
