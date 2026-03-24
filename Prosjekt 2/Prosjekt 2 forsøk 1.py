#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 09:49:51 2025

Prosjekt 2, Forsøk 1

@author: ellaybeckstrom
"""

#import av moduler
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#importerer sympy slik at jeg kan derivere
import sympy as sp

#Begynner med oppgave 1  hvor jeg skal legge inn funksjon 1 inn i startverdi problemet
#Lager funksjonen

def Oppgave1a():
    #legger inn alle variablene jeg ser fra oppgaven
    def P(t, K, P0, r):
        #Deler funksjonen inn i seksjoner
        #teller
        a = K
        #nevner
        b = 1 + (K/P0-1)*(np.e)**(-r*K*t)
        #teller delt på nevner
        c = a/b
        return c
        
    #Parameter for tid
    tid = 3
    #Parameter for bærekapasitet med input
    K1 = float(input("Hva er bærekapasiteten til dyrebestanden\n"))
    #Parameter for r med input slik at jeg kan teste koden enkelt med forskjellige verdier
    r1 = float(input("Skriv inn ett positivt tall\n"))
    #Parameter for P0 med input
    P01 = float(input("Skriv inn en startverdi for P0\n"))
    
    #tester funksjonen 
    P1 = P(tid, K1, P01, r1)
    
    print(P1)
    
    #Legger inn venstre side av Startverdiproblemet
    venstre = r1*P1*(K-P1)
    
    #Høyre side av Startverdiproblemet(den deriverte av funksjonen P(t))
    Høyre = 

    
    
Oppgave1a()