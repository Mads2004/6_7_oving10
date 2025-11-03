# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 17:06:21 2025

@author: madsj
"""
# ============ OPPGAVE 2: Legg til emne i studieplan ============
def oppgave2(emner, studieplaner):
    plans = list(studieplaner.values()) if isinstance(studieplaner, dict) else list(studieplaner)
    if not emner:
        print("Ingen registrerte emner. Kjør oppgave1() først."); return
    if not plans:
        print("Ingen studieplaner. Lag med menyvalg_5() først."); return

    print("\n=== Oppgave 2 ===")
    for i, e in enumerate(emner, 1):
        print(f"{i}. {e}")
    try:
        ei = int(input("Velg emne (nummer): ")) - 1
        if ei not in range(len(emner)): print("Ugyldig nummer."); return
    except ValueError:
        print("Ugyldig input."); return
    emne = emner[ei]

    print("\nTilgjengelige studieplaner:")
    for i, p in enumerate(plans, 1):
        print(f"{i}. {p['id']} - {p['tittel']}")
    try:
        pi = int(input("Velg studieplan (nummer): ")) - 1
        if pi not in range(len(plans)): print("Ugyldig nummer."); return
    except ValueError:
        print("Ugyldig input."); return
    plan = plans[pi]

    sem_keys = sorted(plan["emner_per_semester"])
    print("Semestre i planen:", sem_keys)
    try:
        s = int(input("Hvilket semesternummer? ").strip())
    except ValueError:
        print("Ugyldig semesternummer."); return
    if s not in plan["emner_per_semester"]:
        print(f"Semester {s} finnes ikke i denne planen."); return

    lst = plan["emner_per_semester"][s]
    if any(e.emnekode == emne.emnekode for e in lst):
        print(f"{emne.emnekode} ligger allerede i semester {s}."); return

    lst.append(emne)
    print(f"✅ La til {emne.emnekode} i '{plan['tittel']}' (semester {s}).")
