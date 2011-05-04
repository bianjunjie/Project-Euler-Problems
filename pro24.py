#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Junjie Bian
# File Name: pro24.py
# Description: 

from copy import copy

def _initProduct(digits):
    _product=[1]
    for i in range(len(digits)):
        _product.append(_product[i]*(i+1))
    return _product

def _nth_permutation(nth, digit,product):
    if len(digit)==1:
	return digit
    if nth==1:
	return digit

    _digit=copy(digit)
    index = (nth - 1) / product[len(_digit)-1]
    nth -= (index+1) * product[len(_digit)-1]
    value=_digit[index]
    del _digit[index]

    return [value]+_nth_permutation(nth,_digit,product)

def nth_permutation(nth, digit):
    product=_initProduct(digit)
    return _nth_permutation(nth,digit,product)

digit=[0,1,2,3]
print nth_permutation(11,digit)



