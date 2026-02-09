import os

# --- 1. LOGICKÁ VRSTVA (Práce s daty, žádné print/input) ---

def vytvor_ukol(nazev, popis):
    """
    Vytvoří slovník úkolu. Provádí validaci (nesmí být prázdné).
    Vrací: slovník s daty nebo None, pokud jsou data neplatná.
    """
    nazev = nazev.strip()
    popis = popis.strip()
    
    if not nazev or not popis:
        return None  # Validace selhala
        
    return {"nazev": nazev, "popis": popis}

def odstran_ukol_ze_seznamu(seznam_ukolu, index):
    """
    Pokusí se odstranit úkol na daném indexu.
    Vrací: (True, odstraneny_ukol) nebo (False, chybova_zprava)
    """
    try:
        # Převod z lidského číslování (1, 2...) na programátorské (0, 1...)
        cislo_index = int(index) - 1
        
        if 0 <= cislo_index < len(seznam_ukolu):
            odstraneny = seznam_ukolu.pop(cislo_index)
            return True, odstraneny
        else:
            return False, f"Číslo {index} není v seznamu."
    except ValueError:
        return False, "Nebylo zadáno platné číslo."

# --- 2. UI VRSTVA (Vstupy a výstupy, komunikace s uživatelem) ---

def pause():
    """Pomocná funkce pro zastavení výpisu, než uživatel stiskne Enter."""
    input("\nStiskněte Enter pro návrat do menu...")

def zobrazit_ukoly_ui(seznam_ukolu):
    """Vypíše seznam úkolů do konzole."""
    print("\n=== SEZNAM ÚKOLŮ ===")
    if not seznam_ukolu:
        print("Seznam je prázdný.")
    else:
        for i, ukol in enumerate(seznam_ukolu, start=1):
            print(f"{i}. [{ukol['nazev']}] - {ukol['popis']}")

def pridat_ukol_ui(seznam_ukolu):
    """Získá vstupy od uživatele a zavolá logiku pro vytvoření."""
    print("\n--- Přidání nového úkolu ---")
    nazev = input("Zadejte název úkolu: ")
    popis = input("Zadejte popis úkolu: ")
    
    # Volání logické vrstvy
    novy_ukol = vytvor_ukol(nazev, popis)
    
    if novy_ukol:
        seznam_ukolu.append(novy_ukol)
        print(f"Úkol '{nazev}' byl úspěšně přidán.")
    else:
        print("Chyba: Název ani popis nesmí být prázdný! Úkol nebyl vytvořen.")

def odstranit_ukol_ui(seznam_ukolu):
    """Zobrazí seznam a požádá uživatele o číslo k smazání."""
    if not seznam_ukolu:
        print("\nSeznam je prázdný, není co mazat.")
        return

    zobrazit_ukoly_ui(seznam_ukolu)
    index_raw = input("\nZadejte číslo úkolu k odstranění: ")
    
    # Volání logické vrstvy
    uspech, vysledek = odstran_ukol_ze_seznamu(seznam_ukolu, index_raw)
    
    if uspech:
        print(f"Hotovo! Úkol '{vysledek['nazev']}' byl smazán.")
    else:
        print(f"Chyba: {vysledek}")

# --- 3. HLAVNÍ PROGRAM (Smyčka) ---

def main():
    # Seznam úkolů (v paměti)
    ukoly = []
    
    while True:
        # Vyčištění obrazovky (volitelné, pro Windows 'cls', pro Mac/Linux 'clear')
        # os.system('cls' if os.name == 'nt' else 'clear') 
        
        print("\n--- SPRÁVCE ÚKOLŮ ---")
        print("1. Přidat úkol")
        print("2. Zobrazit úkoly")
        print("3. Odstranit úkol")
        print("4. Konec")
        
        volba = input("Vyberte (1-4): ")
        
        if volba == '1':
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
            print("Neplatná volba, zkuste to znovu.")
            pause()

if __name__ == "__main__":
    main()