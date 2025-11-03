def finn_planer_for_emne(studieplaner, emnekode):
    funnet = []
    for plan in studieplaner:
        for i in range(1, 7):
            for e in getattr(plan, f"sem{i}", []):
                if e.kode.lower() == emnekode.lower():
                    funnet.append(plan)
                    break
    if not funnet:
        print(f"Ingen studieplaner bruker emnet {emnekode}.")
    else:
        print(f"Studieplaner som bruker {emnekode}:")
        for p in funnet:
            print(f"  - {p.tittel} (ID: {p.id})")
