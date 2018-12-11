#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 00:11:53 2017

@author: Xianan
"""

from numpy import random,sort
from pylab import plot,xlabel,ylabel
from math import log2
N = 1000

tau = 3.053
T = []
for k in range(1,1001):
    x = random.random()
    t = -tau * log2(1-x)
    T.append(t)
T = sort(T)
n = range(1000,0,-1)

plot(T,n)
xlabel('Time/min')
ylabel('Number of undecayed Tl atom')