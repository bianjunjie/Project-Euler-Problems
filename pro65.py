#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro65.py
# Description: 

def sumdigit(m):
    s=0
    while m>0:
	s+=(m%10)
	m/=10
    return s

def solve(k):
    r=[2]

    for i in range(k-1):
	if i%3==0 or i%3==2:
	    r.append(1)
	else:
	    t=(i-1)/3
	    r.append( 2*(t+1))


    r.reverse()
    m=0
    n=0
    for i in r:
	if m==0 and n==0:
	    m=1;n=i
	else:
	    (m,n)=(n,n*i+m)

    (m,n)=(n,m)
    return (m,n)


(m,n)=solve(100)
print 'The answer is %d\n' %(sumdigit(m))

