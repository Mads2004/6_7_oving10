def finn_planer_for_emnekode(studieplaner):
    if not studieplaner:
        print("Ingen studieplaner registrert.")
        return
    print("Oppgi emnekode (eksakt):")
    kode = input("> ").strip().lower()
    if not kode:
        print("Ingen emnekode oppgitt.")
        return

    funn = []
    for sp in studieplaner:
        brukt = any(
            any(e.kode.lower() == kode for e in (sp.semestre[i] if i < len(sp.semestre) else []))
            for i in range(6)
        )
        if brukt:
            funn.append(sp)

    if not funn:
        print(f"Ingen studieplaner bruker '{kode}'.")
    else:
        print(f"Studieplaner som bruker '{kode}':")
        for sp in funn:
            print(f"  - {sp.tittel} (ID: {sp.id})")

if __name__ == "__main__":
    finn_planer_for_emnekode(globals().get("studieplaner", []))
