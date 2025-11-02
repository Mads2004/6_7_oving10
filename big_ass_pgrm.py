# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 18:38:24 2025

@author: madsj
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def utregning_effekt(turbin_effekt, tetthet, areal, strom): 
    return 0.5 * turbin_effekt * tetthet * areal * (strom**3)

def utregning_effekk_strom_avg(turbin_effekt, tetthet, areal, gjennomsnitt_vannstrom): 
    return 0.5 * turbin_effekt * tetthet * areal * (gjennomsnitt_vannstrom**3)

def utregning_areal(r):
    return math.pi * r ** 2

def strom_2retninger(array1, array2):
    return np.sqrt(array1**2 + array2**2)

tidspunkt = []
strom1 = []
strom2 = []
def hovedprogram():
    try:
        with open("C:\\Users\\madsj\\OneDrive\\Dokumenter\\Python_filer\\tidevannsdata_csv.txt", "r", encoding="UTF-8") as fila:
            for linje in fila:
                linje = linje.strip()
                
                deler = linje.split(";")
                
                tid_str, retning1, retning2 = deler
                
                if linje:
                    try:
                        tidspunkt_float = float(tid_str)
                        strom1_float = float(retning1)
                        strom2_float = float(retning2)
                        
                        tidspunkt.append(tidspunkt_float)
                        strom1.append(strom1_float)
                        strom2.append(strom2_float)
                        
                        array1 = np.array(strom1)
                        array2 = np.array(strom2)
                        total = strom_2retninger(array1, array2)
                        
                    except ValueError:
                        print(f"hopper over buns verdi: {linje}")
                 
        print("tidspunkt", tidspunkt)
        print("retning 1: ", strom1)
        print("retning 2: ", strom2)
        print("total: ", total)
        
        plt.plot(tidspunkt, total)
        plt.show()
        
                
        diameter = 1
        r = diameter / 2
        areal = utregning_areal(r)
        
        
        tetthet = 1000
        turbin_effekt = 0.3
        
        strom = np.array(total)
        effekt = utregning_effekt(turbin_effekt, tetthet, areal, strom)
        print(f"effekten til vindturbinen er {effekt} W")
        
        plt.plot(tidspunkt, effekt)
        plt.show()
        
        gjennomsnitt_vannstrom = np.mean(total)
        print("gjennomsnittlig vannstrøm:", gjennomsnitt_vannstrom, "A")
        
        avg_effekt_vannstrom = utregning_effekk_strom_avg(turbin_effekt, tetthet, areal, gjennomsnitt_vannstrom)
        print("gjennomsnitt av effekt med gjennomsnittstrøm er: ", avg_effekt_vannstrom, "W")
        
        gjennomsnitt_effekt = np.mean(effekt)
        print(f"gjennomsnitt effekt er {gjennomsnitt_effekt} W")
        
        
    except ValueError:
        print("ugyldig tall")
hovedprogram()

    