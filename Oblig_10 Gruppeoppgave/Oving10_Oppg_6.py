def skriv_ut_studieplan(plan):
    print(f"\nStudieplan: {plan.tittel} (ID: {plan.id})")
    print("-" * 50)
    for i in range(1, 7):
        emner = getattr(plan, f"sem{i}", [])
        print(f"Semester {i}:")
        if not emner:
            print("  Ingen emner registrert.")
        else:
            for e in emner:
                print(f"  {e.kode} - {e.navn} ({e.studiepoeng} SP, {e.semester})")
        print(f"  Totalt: {sum(e.studiepoeng for e in emner)} SP\n")
