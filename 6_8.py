def finn_planer_for_emne():
    if not studieplaner:
        print("Ingen studieplaner er registrert.")
        return

    emnekode = input("Skriv inn emnekode: ").strip().upper()
    funnet = False

    for plan in studieplaner:
        for emneliste in plan.emner_per_semester.values():
            if any(emne.emnekode == emnekode for emne in emneliste):
                print(f"- {plan.tittel}")
                funnet = True
                break

    if not funnet:
        print(f"Ingen studieplaner inneholder emnet {emnekode}.")
