def finn_plan(studieplaner, søk):
    søk = søk.strip().lower()
    for sp in studieplaner:
        if str(sp.id).lower() == søk or sp.tittel.lower() == søk:
            return sp
    for sp in studieplaner:  # startswith fallback
        if sp.tittel.lower().startswith(søk):
            return sp
    return None

def skriv_ut_studieplan(studieplaner):
    if not studieplaner:
        print("Ingen studieplaner å vise.")
        return
    print("Oppgi studieplan (ID eller tittel):")
    sp = finn_plan(studieplaner, input("> "))
    if not sp:
        print("Fant ikke studieplanen.")
        return

    print(f"\n=== {sp.tittel} (ID: {sp.id}) ===")
    for i in range(6):
        emner = sp.semestre[i] if i < len(sp.semestre) else []
        print(f"\nSemester {i+1}:")
        if not emner:
            print("  (ingen emner)")
        else:
            total = 0
            for e in emner:
                print(f"  - {e.kode} — {e.navn} ({e.studiepoeng} sp)")
                total += float(e.studiepoeng)
            print(f"  Sum: {total} sp")

if __name__ == "__main__":
    skriv_ut_studieplan(globals().get("studieplaner", []))
