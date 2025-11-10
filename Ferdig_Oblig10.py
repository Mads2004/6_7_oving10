# -*- coding: utf-8 -*-
emner = []
studieplaner = []

class Studieplan:
    def __init__(self, id, tittel):
        self.id = id
        self.tittel = tittel
        self.emner_per_semester = {}

    def legg_til_emne(self, emne, semester):
        if semester not in self.emner_per_semester:
            print(f"Semester {semester} finnes ikke i planen.")
            return
        if any(e.emnekode == emne.emnekode for e in self.emner_per_semester[semester]):
            print(f"{emne.emnekode} ligger allerede i semester {semester}.")
            return
        self.emner_per_semester[semester].append(emne)
        print(f"La til {emne.emnekode} i '{self.tittel}' (semester {semester}).")

    def vis_semestre(self):
        return sorted(self.emner_per_semester.keys())

    def __str__(self):
        return f"{self.id} - {self.tittel}"

class Emne:
    def __init__(self, emnekode, semester, studiepoeng):
        self.emnekode = emnekode.upper()
        self.semester = semester
        self.studiepoeng = studiepoeng 
    def __str__(self):
        return f"{self.emnekode} - {self.semester} - {self.studiepoeng} stp"        

def finn_plan_med_id(planer, søkt_id):
    for plan in planer:
        if plan.id == søkt_id:
            return plan
    return None

def lag_nytt_emne(): #Oppg1
    global emner  
    print("Registrering av emner")
    print("Skriv 'stopp' som emnekode for å avslutte.\n")

    while True:
        kode = input("Skriv inn emnekode: ").upper()
        if kode == "STOPP":
            break

        if any(emne.emnekode == kode for emne in emner):
            print(" Dette emnet finnes allerede. Prøv igjen.\n")
            continue

        sem = input("Hvilket semester undervises emnet (høst/vår): ").lower()
        if sem not in ["vår", "høst"]:
            print("Skriv enten høst eller vår")
            continue

        try:
            poeng = int(input("Antall studiepoeng: "))
        except ValueError:
            print("Det var ikke et tall, start på nytt")
            continue

        nytt_emne = Emne(kode, sem, poeng)
        emner.append(nytt_emne)
        print(f"Emnet {kode}, {poeng} stp, {sem} semester, er lagt til.\n")

    print("\n Registrerte emner")
    for emne in emner:
        print(emne)

    print("\nSender bruker tilbake til meny.")

def legg_til_emne(emner, planer): #Oppg2
    print("Velg studieplan:")
    bruk_eksisterende = input("Vil du bruke en eksisterende studieplan? (ja/nei): ").lower()

    if bruk_eksisterende == "ja":
        søkt_id = input("Skriv inn ID for eksisterende studieplan: ")
        eksisterende_plan = finn_plan_med_id(planer, søkt_id)
        if eksisterende_plan:
            plan = eksisterende_plan
            print(f"Studieplan '{plan.tittel}' med ID '{plan.id}' er valgt.")
        else:
            print("Fant ikke studieplan med den ID-en.\nLager ny.")
            id = søkt_id
            tittel = input("Skriv inn tittel for ny studieplan: ")
            plan = Studieplan(id, tittel)
            for i in range(1, 7):
                if i not in plan.emner_per_semester:
                    plan.emner_per_semester[i] = []
            planer.append(plan)
    else:
        print("Opprett ny studieplan")
        id = input("Skriv inn ID for studieplan: ")
        tittel = input("Skriv inn tittel for studieplan: ")
        plan = Studieplan(id, tittel)
        for i in range(1, 7):
            if i not in plan.emner_per_semester:
                plan.emner_per_semester[i] = []
        planer.append(plan)

    print(f"\nStudieplan '{plan.tittel}' med ID '{plan.id}' er klar.")

    if not emner:
        print("Ingen emner er registrert ennå. Gå til menyvalg 1 først.")
        return planer

    legg_til = input("Vil du legge til emner nå? (ja/nei): ").lower()
    if legg_til == "ja":
        while True:
            print("\nRegistrerte emner:")
            for i, emne in enumerate(emner):
                print(f"{i + 1}. {emne}")

            try:
                valg = int(input("Velg emne å legge til (nummer): ")) - 1
                valgt_emne = emner[valg]
                semester = int(input("Hvilket semester skal emnet legges til (1–6): "))
                plan.legg_til_emne(valgt_emne, semester)
            except (ValueError, IndexError):
                print("Ugyldig valg. Prøv igjen.")

            fortsett = input("Vil du legge til flere emner? (ja/nei): ").lower()
            if fortsett != "ja":
                break

    return planer

def fjern_emne(): #Oppg.3
    if not studieplaner:
        print("Ingen studieplaner er registrert.")
        return

    print("Tilgjengelige studieplaner:")
    for i, plan in enumerate(studieplaner):
        print(f"{i + 1}. {plan.tittel}")

    try:
        valg = int(input("Velg studieplan (nummer): ")) - 1
        valgt_plan = studieplaner[valg]
    except (ValueError, IndexError):
        print("Ugyldig valg.")
        return

    semester = int(input("Hvilket semester vil du fjerne emne fra? "))
    if semester not in valgt_plan.emner_per_semester:
        print("Semester finnes ikke.")
        return

    emneliste = valgt_plan.emner_per_semester[semester]
    if not emneliste:
        print("Ingen emner i dette semesteret.")
        return

    print("Emner i semesteret:")
    for i, emne in enumerate(emneliste):
        print(f"{i + 1}. {emne.emnekode}")

    try:
        emnevalg = int(input("Velg emne å fjerne (nummer): ")) - 1
        fjernet = emneliste.pop(emnevalg)
        print(f"Fjernet {fjernet.emnekode} fra semester {semester}.")
    except (ValueError, IndexError):
        print("Ugyldig valg.")

def registrerte_emner(): #Oppg.4
    print("\nRegistrerte emner:")
    for i, emne in enumerate(emner):
        print(f"{i + 1}. {emne.emnekode}")
        
def lag_tom_studieplan(plan_id=None, tittel=None, antall_semestre=6): #Oppg5
    if plan_id is None:
        print("Lag en ny tom studieplan")
        plan_id = input("ID: ")
    if tittel is None:
        tittel = input("Tittel: ")
    
    if antall_semestre is None:
        ant_txt = input("Antall semestre (Enter = 6): ")
        if ant_txt == "":
            antall_semestre = 6
        else:
            try:
                antall_semestre = int(ant_txt)
                if antall_semestre < 1:
                    print("Antall semestre må være minst 1. Setter til 6.")
                    antall_semestre = 6
            except ValueError:
                print("Ugyldig tall. Setter antall semestre til 6.")
                antall_semestre = 6

    plan = Studieplan(plan_id, tittel)
    for sem in range(1, antall_semestre + 1):
        plan.emner_per_semester[sem] = []

    try:
        studieplaner.append(plan)
    except NameError:
        pass

    print("\nStudieplan opprettet!")
    print(f"ID: {plan.id}")
    print(f"Tittel: {plan.tittel}")
    for sem_nr in sorted(plan.emner_per_semester):
        print(f"  Semester {sem_nr}: {plan.emner_per_semester[sem_nr]}")

def skriv_ut_studieplan(studieplaner): #Oppg6
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
               
def sjekk_studieplan(): #Oppg7
    if not studieplaner:
        print("Ingen studieplaner er registrert.")
        return

    print("Registrerte studieplaner:")
    for plan in studieplaner:
        print(f"{plan.id}: {plan.tittel}")

    søkt_id = input("Skriv inn ID på studieplan som skal sjekkes: ").strip()
    plan = finn_plan_med_id(studieplaner, søkt_id)
    if not plan:
        print("Fant ikke studieplan med den ID-en.")
        return

    feil = []

    sett = set()
    for emneliste in plan.emner_per_semester.values():
        for e in emneliste:
            if e.emnekode in sett:
                feil.append(f"Duplikat: {e.emnekode} ligger i flere semestre.")
            else:
                sett.add(e.emnekode)

    for sem in range(1, 7):
        emner_i_sem = plan.emner_per_semester.get(sem, [])
        stp = sum(e.studiepoeng for e in emner_i_sem)
        if stp != 30:
            feil.append(f"Semester {sem}: {stp} stp. - Forventet 30stp")

        forventet = "høst" if sem % 2 == 1 else "vår"
        for e in emner_i_sem:
            if e.semester != forventet:
                feil.append(
                    f"{e.emnekode} i semester {sem} har termin '{e.semester}' (forventet '{forventet}')."
                )
    if feil:
        print("\nPlanen er IKKE gyldig:\n Årsak til feil:")
        for f in sorted(set(feil)):
            print("\n", f)
    else:
        print("\nPlanen er gyldig!")  

def finn_planer_for_emne(): #Oppg8
    sok = input("Skriv emnekode eller del av emnekode du vil finne: ").strip().upper()
    if not sok:
        print("Tomt.")
        return []

    funn = []
    for plan in studieplaner:
        for sem, emneliste in plan.emner_per_semester.items():
            for emne in emneliste:
                if sok in emne.emnekode.upper():
                    funn.append((plan, sem, emne))

    if not funn:
        print(f"Ingen studieplaner har emnet '{sok}'")
        return []
    
    from collections import defaultdict
    resultat = defaultdict(list)
    for plan, sem, emne in funn:
        resultat[plan].append((sem, emne))

    print(f"\nFant emnet '{sok}' i:")
    for plan, entries in resultat.items():
        print(f"\nStudieplan: {plan.tittel} (ID: {plan.id})")
        
        for sem, emne in entries:
            print(f"  Semester {sem}: {emne.emnekode} - {emne.studiepoeng} stp (undervises: {emne.semester})")

def les_til_fil(): #Oppg9
    try:
        with open("studiestuff.txt", "w", encoding="utf-8") as fil:
            fil.write("Emner:\n")
            if not emner:
                fil.write("  Ingen registrerte emner.\n")
            else:
                for i, emne in enumerate(emner, start=1):
                    fil.write(f"  {i}. {emne.emnekode} - {emne.semester} - {emne.studiepoeng} stp\n")
            fil.write("\nStudieplaner:\n")
            if not studieplaner:
                fil.write("Ingen registrerte studieplaner.\n")
            else:
                for i, plan in enumerate(studieplaner, start=1):
                    fil.write(f"\n {i}. {plan.tittel} (ID: {plan.id})\n")
                    semestre = plan.vis_semestre()
                    if not semestre:
                        fil.write("Ingen semestre i denne planen.\n")
                        continue
                    for sem in semestre:
                        emneliste = plan.emner_per_semester.get(sem, [])
                        fil.write(f"    Semester {sem}:\n")
                        if not emneliste:
                            fil.write("Ingen emner.\n")
                        else:
                            for em in emneliste:
                                fil.write(f"- {em.emnekode} ({em.studiepoeng} stp, undervisning: {em.semester})\n")
        print("Data skrevet til studiestuff.txt")
    except Exception as e:
        print("Feil ved skriving til fil:", e)   

def les_fra_fil(): #Oppg10
    try:
        with open ("studiestuff.txt", "r") as fil:
            skriv_ut = fil.read()
            print(skriv_ut)
    except FileNotFoundError:
        print("feil")
        
def avslutt_program(): #Oppg11
    print("avslutter")

menytekst = """
:::::::::::::::::::::
1.  Lag et nytt emne
2.  Legg til et emne i \n    studieplanen
3.  Fjern ett emne fra en \n    studieplan
4.  Liste over registrerte \n    emner
5.  Lag tom studieplan
6.  Skriv ut studieplan med \n    semesteroversikt
7.  Kontroller gyldighet på \n    studieplan
8.  Finn studieplaner med \n    ønkset emne
9.  Lagre emner og studieplan \n    til fil
10. Les inn emner og studieplan \n    fra fil
11. Avslutt programm
:::::::::::::::::::::
"""

def kjør_valg(funksjon):
    funksjon()
    velger()

menyvalg_funksjoner = {
    1: lambda: kjør_valg(lag_nytt_emne),
    2: lambda: kjør_valg(lambda: legg_til_emne(emner, studieplaner)),
    3: lambda: kjør_valg(fjern_emne),
    4: lambda: kjør_valg(registrerte_emner),
    5: lambda: kjør_valg(lag_tom_studieplan),
    6: lambda: kjør_valg(lambda: skriv_ut_studieplan(studieplaner)),
    7: lambda: kjør_valg(sjekk_studieplan),
    8: lambda: kjør_valg(finn_planer_for_emne),
    9: lambda: kjør_valg(les_til_fil),
    10: lambda: kjør_valg(les_fra_fil),
    11: avslutt_program } 

def velger():
    print(menytekst)
    try:
        menyvalg = int(input("Velg et alternativ (1-11): "))
        funksjon = menyvalg_funksjoner.get(menyvalg)
        if funksjon:
            funksjon()
        else:
            print("Ugyldig valg. Prøv igjen.")
            velger()
    except ValueError:
        print("Du må skrive inn et tall mellom 1 og 11.")
        velger()

velger()

 


