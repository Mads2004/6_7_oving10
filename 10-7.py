def finn_plan(studieplaner, søk):
    søk = søk.strip().lower()
    for sp in studieplaner:
        if str(sp.id).lower() == søk or sp.tittel.lower() == søk:
            return sp
    for sp in studieplaner:
        if sp.tittel.lower().startswith(søk):
            return sp
    return None

def sjekk_gyldighet(studieplaner):
    if not studieplaner:
        print("Ingen studieplaner å sjekke.")
        return
    print("Oppgi studieplan (ID eller tittel):")
    sp = finn_plan(studieplaner, input("> "))
    if not sp:
        print("Fant ikke studieplanen.")
        return

    avvik = []
    for i in range(6):
        emner = sp.semestre[i] if i < len(sp.semestre) else []
        total = sum(float(e.studiepoeng) for e in emner)
        if abs(total - 30.0) > 1e-6:
            avvik.append((i+1, total))

    if not avvik:
        print("Studieplanen er gyldig (alle semestre har 30 sp).")
    else:
        print("Studieplanen er IKKE gyldig. Avvik:")
        for sem, total in avvik:
            print(f"  - Semester {sem}: {total} / 30 sp")

if __name__ == "__main__":
    sjekk_gyldighet(globals().get("studieplaner", []))
