def skriv_ut_studieplan(studieplaner):
    if not studieplaner:
        print("Ingen studieplaner å vise.")
        return

    print("\nRegistrerte studieplaner:")
    for i, plan in enumerate(studieplaner):
        print(f"{i + 1}. {plan.tittel}")

    try:
        valg = int(input("Velg studieplan (nummer): ")) - 1
        valgt_plan = studieplaner[valg]
    except (ValueError, IndexError):
        print("Ugyldig valg.")
        return

    print(f"\nStudieplan: {valgt_plan.tittel}")
    semestre = valgt_plan.vis_semestre()
    if not semestre:
        print("Ingen semestre definert i denne planen.")
        return

    for sem in semestre:
        emner_i_sem = valgt_plan.emner_per_semester.get(sem, [])
        print(f"\nSemester {sem}:")
        if not emner_i_sem:
            print("  Ingen emner.")
        else:
            for emne in emner_i_sem:
                print(f"  - {emne.emnekode}: {emne.studiepoeng} stp ({emne.semester})")
