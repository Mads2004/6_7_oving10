# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 18:04:52 2025

@author: simen
"""

# Anta at dette er i filen din, eller importert fra Oving10_Main_Meny
class Emne:
    def __init__(self, emnekode, navn):
        self.emnekode = emnekode
        self.navn = navn

    def __str__(self):
        return f"{self.emnekode} - {self.navn}"

# Eksempeldata (erstatt med import fra Oving10_Main_Meny)
emner = [
    Emne("MAT100", "Matematikk 1"),
    Emne("DAT101", "Innføring i programmering"),
    Emne("DAT102", "Objektorientert programmering"),
    Emne("DAT103", "Datamaskiner og operativsystemer"),
]

# Studieplan-klassen
class Studieplan:
    def __init__(self, id, tittel):
        self.id = id
        self.tittel = tittel
        self.emner_per_semester = {}
        self.opprett_semestre()

    def opprett_semestre(self, antall=6):
        for i in range(1, antall + 1):
            self.emner_per_semester[i] = []

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

    def vis_plan(self):
        print(f"\nStudieplan: {self.tittel}")
        for semester in self.vis_semestre():
            print(f"Semester {semester}:")
            for emne in self.emner_per_semester[semester]:
                print(f"  - {emne}")

    def __str__(self):
        return f"{self.id} - {self.tittel}"

# Menybasert testfunksjon
def meny():
    studieplan = Studieplan("SP1", "Min studieplan")
    while True:
        print("\n--- MENY ---")
        print("1. Legg til emne")
        print("2. Vis studieplan")
        print("3. Avslutt")
        valg = input("Velg et alternativ: ")

        if valg == "1":
            try:
                sem = int(input("Velg semester (1-6): "))
                if sem not in range(1, 7):
                    print("Ugyldig semester.")
                    continue

                print("\nTilgjengelige emner:")
                for i, e in enumerate(emner):
                    print(f"{i}: {e}")

                emne_valg = int(input("Velg emne ved nummer: "))
                if emne_valg < 0 or emne_valg >= len(emner):
                    print("Ugyldig valg.")
                    continue

                valgt_emne = emner[emne_valg]
                studieplan.legg_til_emne(valgt_emne, sem)
            except ValueError:
                print("Ugyldig input. Prøv igjen.")
        elif valg == "2":
            studieplan.vis_plan()
        elif valg == "3":
            print("Avslutter programmet.")
            break
        else:
            print("Ugyldig valg. Prøv igjen.")

# Start programmet
if __name__ == "__main__":
    meny()
