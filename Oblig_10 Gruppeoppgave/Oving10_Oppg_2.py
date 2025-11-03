# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 17:06:21 2025

@author: madsj
"""
from Oving10_Oppg_1 import emner

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
    
emne = legg_til_emne()
print(emne)