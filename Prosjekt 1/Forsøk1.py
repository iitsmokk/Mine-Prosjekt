#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 20:41:39 2025

Oblig 1 Mamo1100

@author: ellaybeckstrom
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
#plott av hjerteslag fil a
def plotta():
    # Leser inn data fra csv-fil inn i arrayet "array":
    hs = np.loadtxt('HS7a.csv', delimiter=',')
    #hs1 = np.loadtxt("HS7b.csv", delimiter= ",")
    #hs2 = np.loadtxt("HS7c.csv", delimiter= ",")
    def objective1(x, a, b, d, e):
        return a * np.sin(b*x) + d*x + e #endret på funksjonen fra eksempel plotten slik at jeg får en sinus funksjon som vokser over grunnlinjen.
    
    # curve fitting av funksjon til data
    popt, _ = curve_fit(objective1,np.cumsum(hs),1/hs,[2, 0.02, 1, 00])
    a, b, d, e = popt
    # Skriv ligning til skjerm:
    print('y = %.5f * sin (%.5f x ) + %.5f' % (a, b, d, e))
    # Definer den rettelinja med disse verdiene for a og b:
    y1 = objective1(np.cumsum(hs),a, b, d, e)
    plt.plot(np.cumsum(hs), 1/hs)
    plt.plot(np.cumsum(hs), y1, linewidth=2)
    #tittel
    plt.title("Hjerteslag fil a")‘
    #Gir x og y aksen navn
    plt.xlabel("Tid/sekunder")
    plt.ylabel("Hjerteslag")
    plt.show()
plotta()

#plott av hjerteslag fil b
def plottb():
    # Leser inn data fra csv-fil inn i arrayet "array":
    hs = np.loadtxt('HS7b.csv', delimiter=',')
    #hs1 = np.loadtxt("HS7b.csv", delimiter= ",")
    #hs2 = np.loadtxt("HS7c.csv", delimiter= ",")
    def objective1(x, a, b, d, e):
        return a * np.sin(b*x) + d*x + e #endret på funksjonen fra eksempel plotten slik at jeg får en sinus funksjon som vokser over grunnlinjen.
    # curve fitting av funksjon til data
    popt, _ = curve_fit(objective1,np.cumsum(hs),1/hs,[2, 0.02, 1, 00])
    a, b, d, e = popt
    # Skriv ligning til skjerm:
    print('y = %.5f * sin (%.5f x ) + %.5f' % (a, b, d))
    # Definer den rettelinja med disse verdiene for a og b:
    y1 = objective1(np.cumsum(hs),a, b, d, e)
    #Under her skal jeg legge inn IQR-metoden for å filtrere ut outliers
    Q1 = np.percentile(y1, 25)
    Q3 = np.percentile(y1, 75)
    
    IQR = Q3 - Q1
    
    nedre = Q1 - 1.5 * IQR
    øvre = Q3 + 1.5 * IQR
    #y-arrayen som har blitt filtrert
    y1_filtrert = y1[(y1 >= nedre) & (y1 <= øvre)]
    #y-verdiene som ble filtrert vekk
    y12 = hs[(hs <= nedre) & (hs >= øvre)]
    
    #plt.plot(np.cumsum(hs), 1/hs)
    #plot for filtrert data
    plt.plot(np.cumsum(hs), y1_filtrert, linewidth=2, )
    #plot for ufiltrert data
    plt.plot(np.cumsum(hs), y1, linewidth=1)
    #Gir x og y aksen navn
    plt.xlabel("Tid/sekunder")
    plt.ylabel("Hjerteslag")
    plt.title("Hjerteslag fil b")
    plt.show()
plottb()
"""
#Plott av hjerteslag fil c
def plottc():
    # Leser inn data fra csv-fil inn i arrayet "array":
    hs = np.loadtxt('HS7c.csv', delimiter=',')
    #hs1 = np.loadtxt("HS7b.csv", delimiter= ",")
    #hs2 = np.loadtxt("HS7c.csv", delimiter= ",")
    def objective1(x, a, b, d, e):
        return a * np.sin(b*x) + d*x + e #endret på funksjonen fra eksempel plotten slik at jeg får en sinus funksjon som vokser over grunnlinjen.
    
    # curve fitting av funksjon til data
    popt, _ = curve_fit(objective1,np.cumsum(hs),1/hs,[2, 0.02, 1, 00])
    a, b, d, e = popt
    # Skriv ligning til skjerm:
    print('y = %.5f * sin (%.5f x ) + %.5f' % (a, b, d))
    # Definer den rettelinja med disse verdiene for a og b:
    y1 = objective1(np.cumsum(hs),a, b, d, e)
    plott1 = plt.plot(np.cumsum(hs), 1/hs)
    plott2 = plt.plot(np.cumsum(hs), y1, linewidth=2)
    #Gir x og y aksen navn
    plt.xlabel("Tid/sekunder")
    plt.ylabel("Hjerteslag")
    plt.show(plott1, plott2)
plottc()
#Her henter jeg alle plottene og samler de i en
#plt.title("Samlet plott av fil a, b og c")
#plt.show(plotta(plott1, plott2), plottb(plott1, plott2), plottc(plott1, plott2))
"""