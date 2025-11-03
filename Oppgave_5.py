    # -*- coding: utf-8 -*-
    """
    Created on Mon Nov  3 00:42:04 2025
    
    @author: madsj
    """
    
    def tom_studieplan(plan_id, tittel, antall_semestre=6):
        emner_per_semester = {}
        for sem in range(1, antall_semestre + 1):
            emner_per_semester[sem] = []
    
        plan = {
            "id": plan_id,
            "tittel": tittel,
            "emner_per_semester": emner_per_semester
        }
        return plan
    
    
    def menyvalg_5():
        print("\n--- Lag en ny tom studieplan ---")
        plan_id = input("ID: ").strip()
        tittel = input("Tittel: ").strip()
        ant_txt = input("Antall semestre (Enter = 6): ").strip()
    
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
    
        plan = tom_studieplan(plan_id, tittel, antall_semestre)
    
        
        print("\n Studieplan opprettet!")
        print(f"ID: {plan['id']}")
        print(f"Tittel: {plan['tittel']}")
        for sem_nr in sorted(plan["emner_per_semester"]):
            print(f"  Semester {sem_nr}: {plan['emner_per_semester'][sem_nr]}")
    
        return plan
    
    
    if __name__ == "__main__":
        menyvalg_5()
