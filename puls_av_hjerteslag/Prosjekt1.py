#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 21:52:17 2025

@author: ellaybeckstrom
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def plotta():
    #Leser inn data fra csv-fil inn i arrayet "array":
    #Csv filene er tid mellom hver syklus. Hver syklus er når hjertet slår, så da kan vi si at csv-filene har perioden til hjerteslagene.
    #ved å ta den inverse av perioden så får vi frekvens som i dette tilfellet er hjerteslag i sekundet. Dette får vi bruk for senere i oppgaven
    hs = np.loadtxt('HS7a.csv', delimiter=',')
    print("Her er fil a informasjon\n")
    #Her definerer jeg funksjonen ved et ekstra ledd "e" slik at sinus-funksjonen vokser over tid
    def objective1(x, a, b, d, e):
        return a * np.sin(b*x) + d*x + e 
    
    #Her brukte jeg curve fit slik som den ble brukt i plot puls
    #verdiene 2, 0.02, 1 og 00 er bare startverdier som curve_fit bruker som utgangspunk
    #ved å ta 1/hs så får jeg frekvensen til hjerteslagene(hvor mye hjerte slår i sekundet)
    popt, _ = curve_fit(objective1,np.cumsum(hs),1/hs,[2, 0.02, 1, 00])
    a, b, d, e = popt
    
    #Her skrives ligningen ut, men jeg endret på den fra plot puls ved å legge til de ekstra leddene som var i funksjonen
    print("HS7a funksjon:",'y = %.5f * sin(%.5f * x) + %.5f * x + %.5f' % (a, b, d, e))
    
    #I denne koden vil jeg bruke np.cumsum for x-aksen siden ved å addere alle leddene fra HS-filene så vil du få en lineær funksjon av tid.
    #her lager jeg y-verdiene i til plotten ved å legge verdier inn i objective1 funksjonen som ble definert tidligere
    #np.cumsum for alle x-verdiene, og legger inn   a, b, d, og e som er verdier tilpasset sinusfunksjonen i popt.
    y1 = objective1(np.cumsum(hs),a, b, d, e)
    
    #Her definerer jeg x-aksen
    x1 = np.cumsum(hs)
    
    #Under her legger jeg inn koden for gjennomsnitt
    
    #Antall ledd i array
    y1_size = y1.size
    
    #sum av ledd
    y1_sum = np.sum(y1)
    
    #Gjennomsnitt
    y1_gsnitt = y1_sum/y1_size
    print("Gjennomsnittet =", y1_gsnitt)
    
    #Filtrerte arrays
    #filtered = data[data >= 3], bruker denne linjen som utgangspunkt i koden min
   
    #filter 1, blå, -5% til 5% avvik fra gjennomsnitt
    f1 = (y1<=y1_gsnitt*1.05) & (y1>=y1_gsnitt*0.95)
    print(f1)
    #filter 2, magenta, mer enn -5% avvik fra gjennomsnittet
    f2 = (y1<=y1_gsnitt*0.95)
    #filter 3, cyan, avviker mellom 5% og 10% fra gjennomsnittet
    f3 = (y1>=y1_gsnitt*1.05) & (y1<=y1_gsnitt*1.10)
    #filter 4, red, avviker mer enn 10% fra gjennomsnittet
    f4 = (y1>=y1_gsnitt*1.10)
    #plott for referanse
    plt.plot(x1, y1, linewidth=1, color="pink")
    #plott for f1
    plt.plot(x1[f1], y1[f1],linewidth=1, color="blue", label="-5% til +5% avvik")
    #plott for f2
    plt.plot(x1[f2], y1[f2],linewidth=1, color="magenta",label="-5% avvik" )
    #plott for f3
    plt.plot(x1[f3], y1[f3],linewidth=1, color="cyan", label="+5% til +10% avvik")
    #plott for f4
    plt.plot(x1[f4], y1[f4],linewidth=1, color="red", label="over +10% avvik")
    
    plt.legend(); plt.grid(True, which="both", linestyle="--", alpha=0.4)
    
    #Gir plotten tittel og legger inn navn på aksene.
    plt.title("HS7a filtrert fil")
    plt.xlabel("Tid/sekunder")
    plt.ylabel("puls")
    plt.show()
    
    #Over ligger koden for gjennomsnitt
    
    #plotter den tilpassede sinusfunksjonen Objective 1.
    plt.plot(x1, y1, linewidth=2, label="Curve fit")
    
    #i tillegg til å plotte den tilpassede sinusfunksjonen så plotter jeg frekvensen til hjerteslag ved å ta den inverse av hvert hjerteslag
    #jeg gjør dette slik at jeg kan se hvor nøyaktig curve_fit har laget grafen.
    plt.plot(x1, 1/hs, linewidth=1, label="Invers")
    
    #bruker plt.legend til å lage grids og å gi mer informasjon ut ifra plotten.
    plt.legend(); plt.grid(True, which="both", linestyle="--", alpha=0.4)
    
    #Gir plotten tittel og legger inn navn på aksene.
    plt.title("HS7a fil")
    plt.xlabel("Tid/sekunder")
    plt.ylabel("puls")
    
    #Viser plotten
    plt.show()
    
plotta()


def plottb():
    #Leser inn data fra csv-fil inn i arrayet "array":
    #Csv filene er tid mellom hver syklus. Hver syklus er når hjertet slår, så da kan vi si at csv-filene har perioden til hjerteslagene.
    #ved å ta den inverse av perioden så får vi frekvens som i dette tilfellet er hjerteslag i sekundet. Dette får vi bruk for senere i oppgaven
    hs = np.loadtxt('HS7b.csv', delimiter=',')
    print("\nHer er fil b informasjon\n")
    #Her definerer jeg funksjonen ved et ekstra ledd "e" slik at sinus-funksjonen vokser over tid
    def objective1(x, a, b, d, e):
        return a * np.sin(b*x) + d*x + e 
    
    #Under er koden fra iqr-metoden
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
    y_size = yi_f.size
    print("antall elementer i y-array =",y_size)
    #Her bruker jeg antall elementer i y arrayen til å få like mye elementer i x-aksen
    x1_f = np.linspace(0, 480, y_size)
    #x verdier for det filtrerte vekk verdiene
    yf_size = yi_f1.size
    print("antall elementer i y-array filtrert vekk = ", yi_f1.size)
    x2_f = np.linspace(0, 480, yf_size)
    #Over er IQR-metoden jeg limte inn fra den andre koden jeg lagde i prosjektet
    
    
    #Her brukte jeg curve fit slik som den ble brukt i plot puls
    #verdiene 2, 0.02, 1 og 00 er bare startverdier som curve_fit bruker som utgangspunk
    #legger inn y fra iqr
    popt, _ = curve_fit(objective1,x1_f ,yi_f ,[2, 0.02, 1, 00])
    a, b, d, e = popt
    
    #Her skrives ligningen ut, men jeg endret på den fra plot puls ved å legge til de ekstra leddene som var i funksjonen
    print("HS7b funksjon:",'y = %.5f * sin(%.5f * x) + %.5f * x + %.5f' % (a, b, d, e))
    
    #I denne koden vil jeg bruke np.cumsum for x-aksen siden ved å addere alle leddene fra HS-filene så vil du få en lineær funksjon av tid.
    #her lager jeg y-verdiene i til plotten ved å legge verdier inn i objective1 funksjonen som ble definert tidligere
    #np.cumsum for alle x-verdiene, og legger inn   a, b, d, og e som er verdier tilpasset sinusfunksjonen i popt.
    y1 = objective1(x1_f,a, b, d, e)
    
    #Under her legger jeg inn koden for gjennomsnitt
    
    #Antall ledd i array
    y1_size = y1.size
    
    #sum av ledd
    y1_sum = np.sum(y1)
    
    #Gjennomsnitt
    y1_gsnitt = y1_sum/y1_size
    print("Gjennomsnittet =", y1_gsnitt)
    
    #Filtrerte arrays
    #filtered = data[data >= 3], bruker denne linjen som utgangspunkt i koden min
   
    #filter 1, blå, -5% til 5% avvik fra gjennomsnitt
    f1 = (y1<=y1_gsnitt*1.05) & (y1>=y1_gsnitt*0.95)
    print(f1)
    #filter 2, magenta, mer enn -5% avvik fra gjennomsnittet
    f2 = (y1<=y1_gsnitt*0.95)
    #filter 3, cyan, avviker mellom 5% og 10% fra gjennomsnittet
    f3 = (y1>=y1_gsnitt*1.05) & (y1<=y1_gsnitt*1.10)
    #filter 4, red, avviker mer enn 10% fra gjennomsnittet
    f4 = (y1>=y1_gsnitt*1.10)
    #plott for referanse
    plt.plot(x1_f, y1, linewidth=1, color="pink")
    #plott for f1
    plt.plot(x1_f[f1], y1[f1],linewidth=1, color="blue", label="-5% til +5% avvik")
    #plott for f2
    plt.plot(x1_f[f2], y1[f2],linewidth=1, color="magenta",label="-5% avvik" )
    #plott for f3
    plt.plot(x1_f[f3], y1[f3],linewidth=1, color="cyan", label="+5% til +10% avvik")
    #plott for f4
    plt.plot(x1_f[f4], y1[f4],linewidth=1, color="red", label="over +10% avvik")
    #bruker plt.legend til å lage grids og å gi mer informasjon ut ifra plotten.
    plt.legend(); plt.grid(True, which="both", linestyle="--", alpha=0.4)
    
    #Gir plotten tittel og legger inn navn på aksene.
    plt.title("HS7b filtrert fil")
    plt.xlabel("Tid/sekunder")
    plt.ylabel("puls")
    plt.show()
    
    #Over ligger koden for gjennomsnitt
    
    #plotter den tilpassede sinusfunksjonen Objective 1.
    plt.plot(x1_f, y1, linewidth=2, label="Curve fit")
    #plotter den funksjonen som ble filtrert ved bruk av 
    plt.plot(x1_f, yi_f, linewidth=2, label="Filtrert kurve")
    
    
    #bruker plt.legend til å lage grids og å gi mer informasjon ut ifra plotten.
    plt.legend(); plt.grid(True, which="both", linestyle="--", alpha=0.4)
    
    #Gir plotten tittel og legger inn navn på aksene.
    plt.title("HS7b fil")
    plt.xlabel("Tid/sekunder")
    plt.ylabel("puls")
    
    #Viser plotten
    plt.show()
    
plottb()

def plottc():
    #Leser inn data fra csv-fil inn i arrayet "array":
    #Csv filene er tid mellom hver syklus. Hver syklus er når hjertet slår, så da kan vi si at csv-filene har perioden til hjerteslagene.
    #ved å ta den inverse av perioden så får vi frekvens som i dette tilfellet er hjerteslag i sekundet. Dette får vi bruk for senere i oppgaven
    hs = np.loadtxt('HS7c.csv', delimiter=',')
    print("\nHer er fil c informasjon\n")
    #Her definerer jeg funksjonen ved et ekstra ledd "e" slik at sinus-funksjonen vokser over tid
    def objective1(x, a, b, d, e):
        return a * np.sin(b*x) + d*x + e 
    
    #Under er koden fra iqr-metoden
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
    y_size = yi_f.size
    print("antall elementer i y-array =",y_size)
    #Her bruker jeg antall elementer i y arrayen til å få like mye elementer i x-aksen
    x1_f = np.linspace(0, 480, y_size)
    #x verdier for det filtrerte vekk verdiene
    yf_size = yi_f1.size
    print("antall elementer i y-array filtrert vekk = ", yi_f1.size)
    x2_f = np.linspace(0, 480, yf_size)
    #Over er IQR-metoden jeg limte inn fra den andre koden jeg lagde i prosjektet
    
    
    #Her brukte jeg curve fit slik som den ble brukt i plot puls
    #verdiene 2, 0.02, 1 og 00 er bare startverdier som curve_fit bruker som utgangspunk
    #legger inn y fra iqr
    popt, _ = curve_fit(objective1,x1_f ,yi_f ,[2, 0.02, 1, 00])
    a, b, d, e = popt
    
    #Her skrives ligningen ut, men jeg endret på den fra plot puls ved å legge til de ekstra leddene som var i funksjonen
    print("HS7c funksjon:",'y = %.5f * sin(%.5f * x) + %.5f * x + %.5f' % (a, b, d, e))
    
    #I denne koden vil jeg bruke np.cumsum for x-aksen siden ved å addere alle leddene fra HS-filene så vil du få en lineær funksjon av tid.
    #her lager jeg y-verdiene i til plotten ved å legge verdier inn i objective1 funksjonen som ble definert tidligere
    #np.cumsum for alle x-verdiene, og legger inn   a, b, d, og e som er verdier tilpasset sinusfunksjonen i popt.
    y1 = objective1(x1_f,a, b, d, e)
    
    #Under her legger jeg inn koden for gjennomsnitt
    x1 = np.cumsum(hs)
    #Antall ledd i array
    y1_size = y1.size
    
    #sum av ledd
    y1_sum = np.sum(y1)
    
    #Gjennomsnitt
    y1_gsnitt = y1_sum/y1_size
    print("Gjennomsnittet =", y1_gsnitt)
    
    #Filtrerte arrays
    #filtered = data[data >= 3], bruker denne linjen som utgangspunkt i koden min
   
    #filter 1, blå, -5% til 5% avvik fra gjennomsnitt
    f1 = (y1<=y1_gsnitt*1.05) & (y1>=y1_gsnitt*0.95)
    print(f1)
    #filter 2, magenta, mer enn -5% avvik fra gjennomsnittet
    f2 = (y1<=y1_gsnitt*0.95)
    #filter 3, cyan, avviker mellom 5% og 10% fra gjennomsnittet
    f3 = (y1>=y1_gsnitt*1.05) & (y1<=y1_gsnitt*1.10)
    #filter 4, red, avviker mer enn 10% fra gjennomsnittet
    f4 = (y1>=y1_gsnitt*1.10)
    #plott for referanse
    plt.plot(x1_f, y1, linewidth=1, color="pink")
    #plott for f1
    plt.plot(x1_f[f1], y1[f1],linewidth=1, color="blue", label="-5% til +5% avvik")
    #plott for f2
    plt.plot(x1_f[f2], y1[f2],linewidth=1, color="magenta",label="-5% avvik" )
    #plott for f3
    plt.plot(x1_f[f3], y1[f3],linewidth=1, color="cyan", label="+5% til +10% avvik")
    #plott for f4
    plt.plot(x1_f[f4], y1[f4],linewidth=1, color="red", label="over +10% avvik")
    #bruker plt.legend til å lage grids og å gi mer informasjon ut ifra plotten.
    plt.legend(); plt.grid(True, which="both", linestyle="--", alpha=0.4)
    
    #Gir plotten tittel og legger inn navn på aksene.
    plt.title("HS7c filtrert fil")
    plt.xlabel("Tid/sekunder")
    plt.ylabel("puls")
    plt.show()
    
    #Over ligger koden for gjennomsnitt
    
    #plotter den tilpassede sinusfunksjonen Objective 1.
    plt.plot(x1_f, y1, linewidth=2, label="Curve fit")
    #plotter den funksjonen som ble filtrert ved bruk av 
    plt.plot(x1_f, yi_f, linewidth=2, label="Filtrert kurve")
    
    
    #bruker plt.legend til å lage grids og å gi mer informasjon ut ifra plotten.
    plt.legend(); plt.grid(True, which="both", linestyle="--", alpha=0.4)
    
    #Gir plotten tittel og legger inn navn på aksene.
    plt.title("HS7c fil")
    plt.xlabel("Tid/sekunder")
    plt.ylabel("puls")
    
    #Viser plotten
    plt.show()
    
plottc()




