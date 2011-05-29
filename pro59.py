#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro59.py
# Description: 


def solve(s,i,j,k):
    ans=[0]*len(s)
    for (idx,w) in enumerate(s):
	if idx%3==0:
	    ans[idx]=w ^ i
	elif idx%3==1:
	    ans[idx]=w ^ j
	else:
	    ans[idx]=w ^ k
	if ans[idx]<ord(' ') or ans[idx]>ord('z'):
	    return False
	ans[idx]=chr(ans[idx])
    ans_str=''.join(ans)

    if ans_str.find('the')!=-1:
	print ans_str
	print sum([ord(i) for i in ans])
    return True

		    


s=[int(i) for i in open('cipher1.txt').read().strip().split(',')]
r=range(ord('a'), ord('z')+1)

for i in r:
    for j in r:
	for k in r:
	    solve(s,i,j,k)

