# --- LOGICKÁ VRSTVA (Bez inputů a printů) ---

def odstran_ukol_ze_seznamu(seznam_ukolu, index):
    """
    Pokusí se odstranit úkol na daném indexu.
    Vrací (úspěch, data_ukolu/chybová_zpráva).
    """
    try:
        # Převod číslování (1, 2...) na programátorské (0, 1...)
        cislo_index = int(index) - 1
        
        if 0 <= cislo_index < len(seznam_ukolu):
            odstraneny = seznam_ukolu.pop(cislo_index)
            return True, odstraneny
        else:
            return False, f"Číslo {index} není v seznamu."
    except ValueError:
        return False, "Nebylo zadáno platné číslo."

# UI (Interakce s uživatelem)

def zobrazit_ukoly_ui(seznam_ukolu):
    """Zobrazí seznam úkolů v přehledném formátu."""
    print("\n=== SEZNAM ÚKOLŮ ===")
    if not seznam_ukolu:
        print("Seznam je prázdný.")
    else:
        for i, ukol in enumerate(seznam_ukolu, start=1):
            print(f"{i}. [{ukol['nazev']}] - {ukol['popis']}")

def odstranit_ukol_ui(seznam_ukolu):
    """UI proces pro odstranění úkolu."""
    if not seznam_ukolu:
        print("\nSeznam je prázdný, není co mazat.")
        return

    zobrazit_ukoly_ui(seznam_ukolu)
    index_raw = input("\nZadejte číslo úkolu k odstranění: ")
    
    uspech, vysledek = odstran_ukol_ze_seznamu(seznam_ukolu, index_raw)
    
    if uspech:
        print(f"Hotovo! Úkol '{vysledek['nazev']}' byl smazán.")
    else:
        print(f"Chyba: {vysledek}")

def pause():
    """Jednotné místo pro pauzu po akci."""
    input("\nStiskněte Enter pro návrat do menu...")

# HLAVNÍ SMYČKA

def main():
    ukoly = []
    while True:
        print("\n--- SPRÁVCE ÚKOLŮ ---")
        print("1. Přidat úkol")
        print("2. Zobrazit úkoly")
        print("3. Odstranit úkol")
        print("4. Konec")
        
        volba = input("Vyberte (1-4): ")
        
        if volba == '1':
            # Předpokládáme existenci pridat_ukol_ui z předchozí ukázky
            pridat_ukol_ui(ukoly)
            pause()
        elif volba == '2':
            zobrazit_ukoly_ui(ukoly)
            pause()
        elif volba == '3':
            odstranit_ukol_ui(ukoly)
            pause()
        elif volba == '4':
            print("Nashledanou!")
            break
        else:
            print("Neplatná volba.")
            pause()

if __name__ == "__main__":
    main()