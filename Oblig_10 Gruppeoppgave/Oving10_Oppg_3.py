# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 17:38:27 2025

@author: madsj
"""

# ============ OPPGAVE 3: Fjern emne fra studieplan ============
def oppgave3(studieplaner):
    plans = list(studieplaner.values()) if isinstance(studieplaner, dict) else list(studieplaner)
    if not plans:
        print("Ingen studieplaner. Lag med menyvalg_5() først."); return

    print("\n=== Oppgave 3 ===")
    for i, p in enumerate(plans, 1):
        print(f"{i}. {p['id']} - {p['tittel']}")
    try:
        pi = int(input("Velg studieplan (nummer): ")) - 1
        if pi not in range(len(plans)): print("Ugyldig nummer."); return
    except ValueError:
        print("Ugyldig input."); return
    plan = plans[pi]

    flat = [(sn, e) for sn in sorted(plan["emner_per_semester"])
                    for e in plan["emner_per_semester"][sn]]
    if not flat:
        print("Denne studieplanen har ingen emner å fjerne."); return

    for i, (sn, e) in enumerate(flat, 1):
        print(f"{i}. [Sem {sn}] {e}")
    try:
        xi = int(input("Velg nummer som skal fjernes: ")) - 1
        if xi not in range(len(flat)): print("Ugyldig nummer."); return
    except ValueError:
        print("Ugyldig input."); return

    sn, emne = flat[xi]
    try:
        plan["emner_per_semester"][sn].remove(emne)
        print(f"🗑️ Fjernet {emne.emnekode} fra '{plan['tittel']}' (semester {sn}).")
    except ValueError:
        print("Fant ikke emnet (uventet).")
