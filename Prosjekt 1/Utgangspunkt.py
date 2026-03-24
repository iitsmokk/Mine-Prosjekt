#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 18:29:25 2025

Oblig 1 prosjekt, mamo1100

@author: ellaybeckstrom
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Leser inn data fra csv-fil inn i arrayet "array":
hs = np.loadtxt('HS7a.csv', delimiter=',')

# Regn ut beste sinus-tilpasning (merk: ikke det som skal bestemmes i obligen):
def objective1(x, a, b, d, e):
    return a * np.sin(b*x) + d*x + e #plusset på e slik at jeg får en sinus funksjon som vokser.

# curve fitting av funksjon til data
popt, _ = curve_fit(objective1,np.cumsum(hs),1/hs,[2, 0.02, 1, 00])
a, b, d, e = popt
# Skriv ligning til skjerm:
print('y = %.5f * sin (%.5f x ) + %.5f' % (a, b, d))
# Definer den rettelinja med disse verdiene for a og b:
y1 = objective1(np.cumsum(hs),a, b, d, e)
plt.plot(np.cumsum(hs), 1/hs)
plt.plot(np.cumsum(hs), y1, 'ro-')
plt.show()
 