#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro93.py
# Description: 


from copy import *
from datetime import datetime

def operation(a,b):
    s=[]
    s.append(a+b)
    s.append(a-b)
    s.append(b-a)
    s.append(a*b)
    if (abs(b)>1e-10):
	s.append(a*1.0/b)
    if (abs(a)>1e-10):
	s.append(b*1.0/a)
    s=list(set(s))
    return s


def list_exist(r, subr):
    for er in r:
	max_sub=-1
	for i in range(len(er)):
	    if abs(er[i]-subr[i])>max_sub:
		max_sub=abs(er[i]-subr[i])
	if max_sub<1e-5:
	    return True
    return False
'''
[[1,2,3,4]]-->[[1],[2],..,[36]]
'''
def shrink(in_list):
    if len(in_list[0])==1:
	return in_list

    r=[]
    for l in in_list:
	length=len(l)

	for i in range(length):
	    for j in range(length):
		if i==j:
		    continue
		t=copy(l)
		t.remove(l[i]);t.remove(l[j])

		m=operation(l[i], l[j])
		for em in m:
		    shrink_l=[em]
		    shrink_l+=t
		    shrink_l=sorted(shrink_l)
#		    if not list_exist(r, shrink_l):
                    r.append(shrink_l)
    
#    print r
#    print '--------------\n\n'
    return shrink(r)



t1=datetime.now()
R= shrink([[1,2,3,4]])
result=[]
for each_r in R:
    if abs(int(each_r[0])-each_r[0])<1e-5 and int(each_r[0])>0:
	result.append(int(each_r[0]))
result=sorted(set(result))
print result
print datetime.now()-t1
