#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro42.py
# Description: 

from math import *

wordList=[w[1:-1] for w in open('words.txt').read().strip().split(',')]
print wordList

def calword(word):
    w=0
    for i in word:
	w=w+ord(i)-ord('A')+1
    return w


num=0
for word in wordList:
    w=calword(word)
    s=1+8*w
    if int(sqrt(s))*int(sqrt(s))==s:
	num+=1

print num

