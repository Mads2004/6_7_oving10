# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 00:53:25 2025

@author: madsj
"""

class Emne:
    def __init__(self, emnekode, navn, semester, studiepoeng):
        self.emnekode = emnekode
        self.navn = navn
        self.semester = semester
        self.studiepoeng = studiepoeng

    def __str__(self):
        return f"{self.emnekode} - {self.navn} ({self.semester}, {self.studiepoeng} SP)"
