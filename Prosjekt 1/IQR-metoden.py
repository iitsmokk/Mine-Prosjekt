#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 14:53:08 2025

IQR-metoden for å fjerne outliers.
Dette er en del av oppgave 1 b) men programmet blir brukt igjennom hele oppgaven
@author: ellaybeckstrom
"""
import numpy as np
import matplotlib.pyplot as plt


hs = np.loadtxt("HS7c.csv", delimiter=",")

x1 = np.cumsum(hs)

yi = 1/hs

Q1 = np.percentile(yi, 25)
Q3 = np.percentile(yi, 75)

IQR = Q3 - Q1

nedre = Q1 - 1.5 * IQR
øvre = Q3 + 1.5 * IQR
#y-arrayen som har blitt filtrert
yi_f = yi[(yi >= nedre) & (yi <= øvre)]
#y-verdiene som ble filtrert vekk
yi_f1 = yi[(yi <= nedre) | (yi >= øvre)]



print("puls filtrert " , yi_f)
print("puls filtrert vekk ", yi_f1)

y_size = yi_f.size
print("antall elementer i y-array =",y_size)
#Her bruker jeg antall elementer i y arrayen til å få like mye elementer i x-aksen
x1_f = np.linspace(0, 480, y_size)
#x verdier for det filtrerte vekk verdiene
yf_size = yi_f1.size
print("antall elementer i y-array filtrert vekk")
x2_f = np.linspace(0, 480, yf_size)
"""
Alt under her tar jeg ikke med meg til hoved koden
#samlet scatter
plt.scatter(x1_f, yi_f, label="filtrert")
plt.scatter(x2_f, yi_f1, label="filtrert vekk")
#Estetiske ting
plt.xlabel("Tid/minutter")
plt.ylabel("Puls/Hjerteslag i minuttet")
plt.title("Hjerteslag fil b scatter")
plt.legend(); plt.grid(True, which="both", linestyle="--", alpha=0.4)
plt.show()

#Samlet plott
plt.plot(x1_f, yi_f, label="filtrert")
plt.plot(x2_f, yi_f1, label="filtrert vekk")
#Estetiske ting
plt.title("Hjerteslag fil b linje")
plt.xlabel("Tid/minutter")
plt.ylabel("Puls/Hjerteslag i minuttet")
plt.legend(); plt.grid(True, which="both", linestyle="--", alpha=0.4)
plt.show()

#Filtrert egen plott
plt.plot(x1_f, yi_f, label="filtrert")
#Estetiske ting
plt.title("Hjerteslag fil b linje")
plt.xlabel("Tid/minutter")
plt.ylabel("Puls/Hjerteslag i minuttet")
plt.legend(); plt.grid(True, which="both", linestyle="--", alpha=0.4)
plt.show()

#ikke Filtrert egen plott
plt.plot(x1, yi, label="ikke filtrert")
#Estetiske ting
plt.title("Hjerteslag fil b linje")
plt.xlabel("Tid/minutter")
plt.ylabel("Puls/Hjerteslag i minuttet")
plt.legend(); plt.grid(True, which="both", linestyle="--", alpha=0.4)
plt.show()
"""



