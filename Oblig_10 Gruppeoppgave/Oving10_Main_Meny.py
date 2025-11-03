# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 10:29:45 2025

@author: simen
"""
emner = []
studieplaner = []

from Oving10_Oppg_1 import lag_nytt_emne
from Test_Oving10_Oppg_2 import meny
from Oving10_Oppg_5 import lag_tom_studieplan
from Oving10_Oppg_6 import skriv_ut_studieplan
from Oving10_Oppg_7 import sjekk_studieplan
from Oving10_Oppg_8 import finn_planer_for_emne

menytekst = """
:::::::::::::::::::::
1.  Lag et nytt emne
2.  Legg til et emne i studieplanen
3.  Fjern ett emne fra en studieplan
4.  Liste over registrerte emner
5.  Lag tom studieplan
6.  Skriv ut studieplan med semesteroversikt
7.  Kontroller gyldighet på studieplan
8.  Finn studieplaner med ønkset emne
9.  Lagre emner og studieplan til fil
10. Les inn emner og studieplan fra fil
11. Avslutt programm
:::::::::::::::::::::
"""
                
class Studieplan:
    def __init__(self, id, tittel):
        self.id = id
        self.tittel = tittel
        self.emner_per_semester = {}  

    def legg_til_emne(self, emne, semester):
        if semester not in self.emner_per_semester:
            print(f"Semester {semester} finnes ikke i planen.")
            return

        if any(e.emnekode == emne.emnekode for e in self.emner_per_semester[semester]):
            print(f"{emne.emnekode} ligger allerede i semester {semester}.")
            return

        self.emner_per_semester[semester].append(emne)
        print(f"La til {emne.emnekode} i '{self.tittel}' (semester {semester}).")

    def vis_semestre(self):
        return sorted(self.emner_per_semester.keys())

    def __str__(self):
        return f"{self.id} - {self.tittel}"
    
def registrerte_emner():
    if not emner:
        print("Ingen emner er registrert ennå")
    else: 
        for emne in (emner):
            print(emne)

def les_til_fil():
    try:
        with open ("studiestuff.txt", "w") as fil:
            fil.write(f"{'Studieplan':<10}   {'Emner':>5}\n")
            fil.write("" "\n")
            for i, semesterliste in enumerate(studieplan, start=1):
             fil.write(f"Semester {i}| {semesterliste}\n")         
    except FileNotFoundError:
        print("Filnavn ikke riktig")

def les_fra_fil():
    try:
        with open ("test.txt", "r") as fil:
            skriv_ut = fil.read()
            print(skriv_ut)
    except FileNotFoundError:
        print("filen finnes ikke")

def avslutt_program():
    print("Avslutter")

def valg_1():
    global emne
    emne = lag_nytt_emne()
    emner.extend(emne)
    velger()
def valg_2(): 
    global studieplan
    studieplan = meny()
    studieplaner.extend(studieplan)
    velger()
def valg_3(): 
    oppgave3()
    velger()
def valg_4():
    registrerte_emner()
    velger()
def valg_5(): 
    lag_tom_studieplan()
    velger()
def valg_6(): 
    skriv_ut_studieplan()
    velger()
def valg_7(): 
    sjekk_studieplan()
    velger()
def valg_8():
    finn_planer_for_emne()
    velger()
def valg_9():
    les_til_fil()
    velger()
def valg_10():
    les_fra_fil()
    velger()
def valg_11():
    avslutt_program()

menyvalg_funksjoner = {
    1: valg_1,
    2: valg_2,
    3: valg_3,
    4: valg_4,
    5: valg_5,
    6: valg_6,
    7: valg_7,
    8: valg_8,
    9: valg_9,
    10: valg_10,
    11: valg_11
                      }

def velger():
    print(menytekst)
    menyvalg = int(input("Velg et alternativ (1-11):")) 
    funksjon = menyvalg_funksjoner.get(menyvalg)
    if funksjon:
        funksjon()
    else:
        print("Ugyldig valg. Prøv igjen.")

velger()
