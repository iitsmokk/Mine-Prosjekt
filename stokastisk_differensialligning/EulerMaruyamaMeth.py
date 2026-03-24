# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 08:15:22 2025

@author: leivoy

Endret på for Prosjekt 2 av: Ellay Bryan Beckstrøm
"""

# Import av moduler:
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Oppgave 2 a)
#hvor jeg skulle finne hvor stort intervallet var
oppg2a = np.linspace(0,20,10) 
#print(oppg2a)
# Høyre side i ODE y'=f(x,y) (må justeres):
    #Endrer på formelen til funksjonen med å legge til leddet sP for jakt i bestanden(s=0.5)
    #slik jeg har forstått funksjonen så er y det samme som P i oppgaven
def f(x,y):
    return y*(1-y)-0.5*y

# Euler-Maruyamas metode (ikke nødvendig å justere):
    #Skriver hvilke ledd i funksjonen som er ledd i oppgaven slik at jeg forstår koden lettere
    #f = P(1-P)*sP
    #a, b og n er intervallet [0 - 20, 10 intervall]
    #yinit er startverdien P0
    #xs = t (tid)
    #ys = P(t)
def EulerMaruyama(f,a,b,n,yinit,sig):
    h = (b-a)/n
    xs = a + np.arange(n+1)*h
    ys = np.zeros(n+1)
    y = yinit
    for j,x in enumerate(xs):
        ys[j] = y
        z = np.random.normal(0,1)
        y += h*f(x, y) + sig*y*np.sqrt(h)*z
    return xs, ys

# Sett parametere (må justeres):
    #Byttet plass på n og yinit siden de sto på feil plass og endret på sigma fra 0.5 til 0.02
    #endret på variablene slik som de skulle være i oppgaven
a, b, n, yinit, sig = 0, 20, 10, 0.02, 0.1
# Løs numerisk ved Euler-Maruyamas metode:
xs, ys = EulerMaruyama(f,a,b,n,yinit,sig);  


    
#plotter funksjon:
    #plotter funksjonen med punkter ved å bruke scatter siden den ikke skulle være sammenhengende
plt.scatter(xs, ys)
plt.xlabel("Tid")
plt.ylabel("Bærekapasitet")
plt.show()

# Tilpass funksjon til data:
    #legger inn funksjonen som skal bli tilpasset til
def f1(x, A, B, c):
    return A/(1+B*(np.e)**(-c*x))

#Når jeg fitter funksjonen får jeg 3 verdier den siste verdien er x1 arrayen
popt, _ = curve_fit(f1 ,xs, ys)
A, B, c = popt
print("A:", round(A,3), "B:", round(B,3), "c", round(c, 3))
#lager en ny x akse med samme x verdier fra eulermaruyama slik at jeg kan
#plotte den nye curve_fit funksjonen
x1 = np.linspace(a, b, 10)

y1 = f1(x1, A, B, c)
#plotter funksjonene sammen:
    #plotter funksjonen med punkter ved å bruke scatter siden den ikke skulle være sammenhengende
plt.scatter(xs, ys, linewidth=1, color="blue", label="Original funksjon")
plt.plot(x1, y1, linewidth=2, color="red", label="Fitted funksjon")
plt.xlabel("Tid")
plt.ylabel("Bærekapasitet")
plt.title("Sigma=0.02")
plt.legend(); plt.grid(True, which="both", linestyle="--", alpha=0.4)
plt.show()

# Definer objektiv-funksjon:

# Estimer parametere i objektiv-funksjon:

# Definer funksjonen med disse verdiene for a og b:

# Plott beste tilpasning sammen med dataene beregnet ovenfor: 