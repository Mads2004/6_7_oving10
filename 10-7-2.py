def sjekk_studieplan(plan):
    gyldig = True
    print(f"\nSjekker studieplan: {plan.tittel}")
    print("-" * 50)

    for i in range(1, 7):
        emner = getattr(plan, f"sem{i}", [])
        total_sp = sum(e.studiepoeng for e in emner)
        forventet_sem = "H" if i % 2 == 1 else "V"

        if total_sp != 30:
            gyldig = False
            print(f"Semester {i}: {total_sp} SP (skal være 30)")
        for e in emner:
            if e.semester != forventet_sem:
                gyldig = False
                print(f"  {e.kode} ligger i feil termin ({e.semester}), skal være {forventet_sem}")

    if gyldig:
        print("Studieplanen er gyldig!")
    else:
        print("Studieplanen er ikke gyldig.")
