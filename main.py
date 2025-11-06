def hlavni_menu():
    """
    Zobrazí hlavní menu a vrátí volbu uživatele.
    """
    print("\n--- Správce úkolů - Hlavní menu ---")
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol")
    print("4. Konec programu")
    
    volba = input("Vyberte možnost (1-4): ")
    return volba

def pridat_ukol(seznam_ukolu):
    """
    Přidá nový úkol (jako slovník s názvem a popisem) do zadaného seznamu.
    """
    print("\n--- Přidání nového úkolu ---")
    nazev = input("Zadejte název úkolu: ")
    popis = input("Zadejte popis úkolu: ")
    
    novy_ukol = {
        "nazev": nazev,
        "popis": popis
    }
    seznam_ukolu.append(novy_ukol)
    print(f"Úkol '{nazev}' byl úspěšně přidán.")

def zobrazit_ukoly(seznam_ukolu):
    """
    Zobrazí všechny úkoly v seznamu.
    """
    print("\nSeznam úkolů:")
    
    if not seznam_ukolu:
        print("Seznam úkolů je prázdný.")
    else:
        for i, ukol in enumerate(seznam_ukolu, start=1):
            print(f"{i}. {ukol['nazev']} - {ukol['popis']}")

def odstranit_ukol(seznam_ukolu):
    """
    Nejprve zobrazí seznam úkolů a poté odstraní úkol na základě čísla.
    """
    print("\n--- Odstranění úkolu ---")

    # 1. Zobrazíme seznam, aby uživatel viděl, co maže
    # Použijeme stejný kód jako v 'zobrazit_ukoly'
    print("\nSeznam úkolů:")
    if not seznam_ukolu:
        print("Seznam úkolů je prázdný. Není co odstranit.")
        return # Ukončíme funkci, pokud je seznam prázdný

    for i, ukol in enumerate(seznam_ukolu, start=1):
        print(f"{i}. {ukol['nazev']} - {ukol['popis']}")

    # 2. Zeptáme se na číslo úkolu k odstranění
    try:
        cislo_str = input("\nZadejte číslo úkolu, který chcete odstranit: ")
        # Převedeme vstup na číslo a upravíme na 0-indexovaný seznam (číslo 1 je index 0)
        cislo_index = int(cislo_str) - 1

        # 3. Zkontrolujeme, zda je zadané číslo platné
        if 0 <= cislo_index < len(seznam_ukolu):
            # Použijeme .pop() k odstranění úkolu. 
            # .pop() zároveň vrátí odstraněnou položku.
            odstraneny_ukol = seznam_ukolu.pop(cislo_index)
            
            # Vypíšeme potvrzení
            print(f"Úkol '{odstraneny_ukol['nazev']}' byl odstraněn.")
        
        else:
            # Uživatel zadal číslo mimo rozsah (např. 5, i když má jen 2 úkoly)
            print(f"Chyba: Číslo {cislo_str} není platné číslo v seznamu.")

    except ValueError:
        # Uživatel zadal něco, co není číslo (např. "abc")
        print("Chyba: Nebylo zadáno platné číslo.")
    except Exception as e:
        # Zachycení jakýchkoliv dalších neočekávaných chyb
        print(f"Došlo k neočekávané chybě: {e}")

def main():
    """
    Hlavní funkce, která řídí běh programu.
    """
    ukoly = []

    while True:
        volba = hlavni_menu()
        
        if volba == '1':
            pridat_ukol(ukoly)
            input("\nStiskněte Enter pro návrat do menu...")
            
        elif volba == '2':
            zobrazit_ukoly(ukoly)
            input("\nStiskněte Enter pro návrat do menu...")
            
        elif volba == '3':
            odstranit_ukol(ukoly) 
            input("\nStiskněte Enter pro návrat do menu...")

        elif volba == '4':
            print("\nUkončuji program. Nashledanou!")
            break 
            
        else:
            print("\nNeplatná volba. Zadejte prosím číslo od 1 do 4.")
            input("\nStiskněte Enter pro návrat do menu...")

# Spuštění hlavní funkce programu
if __name__ == "__main__":
    main()