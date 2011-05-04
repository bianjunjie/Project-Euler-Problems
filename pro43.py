#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro43.py
# Description: 
import math
import copy

def Unique(l):
    if len(set(l))==len(l):
	return True
    return False

digits=range(0,10)

s=0

for p17 in range(int(math.ceil(100./17)), int(math.floor(999./17))+1):
    d890=p17*17;
    d8=d890/100;d9=(d890-d8*100)/10;d0=d890%10;
    if d8==d9 or d9==d0 or d0==d8:
	continue;
    digits.remove(d8);
    digits.remove(d9);
    digits.remove(d0);

    for d7 in digits:
	num13=d7*100+d8*10+d9;
	if num13%13==0:
	    for d6 in digits:
		num11=d6*100+d7*10+d8
		if num11%11==0:
		    for d5 in digits:
			num7=d5*100+d6*10+d7
			if num7%7==0:
			    for d4 in digits:
				num5=d4*100+d5*10+d6
				if num5%5==0 and Unique([d7,d6,d5,d4]):
				    NewDigits=copy.copy(digits)
				    NewDigits.remove(d7)
				    NewDigits.remove(d6)
				    NewDigits.remove(d5)
				    NewDigits.remove(d4)
				    for d3 in NewDigits:
					for d2 in NewDigits:
					    for d1 in NewDigits:
						if d3==d2 or d2==d1 or d1==d3:
						    continue
						num3=d3*100+d4*10+d5
						num2=d2*100+d3*10+d4
						if num3%3==0 and num2%2==0:
						    if Unique([d1,d2,d3,d4,d5,d6,d7]):
							s=s+d1*1e9+d2*1e8+d3*1e7+d4*1e6+d5*1e5+d6*1e4+d7*1e3+d8*1e2+d9*1e1+d0
    digits.append(d8) 
    digits.append(d9) 
    digits.append(d0) 
print int(s)


