# ...existing code...
def hlavni_menu():
    """
    Zobrazí hlavní menu a vrátí volbu uživatele.
    """
    print("\nSprávce úkolů - Hlavní menu")
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
    print(f"Úkol '{nazev}' byl přidán.")

def zobrazit_ukoly(seznam_ukolu):
    """
    Zobrazí všechny úkoly v seznamu (podle obrázku).
    """
    print("\nSeznam úkolů:")
    
    if not seznam_ukolu:
        print("Seznam úkolů je prázdný.")
    else:
        # Prochází seznam slovníků a tiskne index + název + popis
        for i, ukol in enumerate(seznam_ukolu, start=1):
            print(f"{i}. {ukol['nazev']} - {ukol['popis']}")

def odstranit_ukol(seznam_ukolu):
    """
    Nejprve zobrazí seznam úkolů a poté odstraní úkol na základě čísla.
    """
    # 1. Zobrazení seznamu
    zobrazit_ukoly(seznam_ukolu)
    
    if not seznam_ukolu:
        # Většinou již zachyceno v zobrazit_ukoly, ale pro jistotu:
        print("Není co odstranit.")
        return 

    # 2. Získání volby od uživatele
    try:
        cislo_str = input("\nZadejte číslo úkolu, který chcete odstranit: ").strip()
        # Převod na 0-indexovaný seznam
        cislo_index = int(cislo_str) - 1

        # 3. Kontrola platnosti a odstranění
        if 0 <= cislo_index < len(seznam_ukolu):
            # Použijeme .pop() k odstranění a získání odstraněného úkolu
            odstraneny_ukol = seznam_ukolu.pop(cislo_index)
            
            # Potvrzení (přesně jako na obrázku)
            print(f"Úkol '{odstraneny_ukol['nazev']}' byl odstraněn.")
        
        else:
            print(f"Chyba: Číslo {cislo_str} není platné číslo v seznamu.")

    except ValueError:
        print("Chyba: Nebylo zadáno platné číslo.")
    except Exception as e:
        print(f"Došlo k neočekávané chybě: {e}")

def main():
    """
    Hlavní funkce, která řídí běh programu ve smyčce.
    """
    # Seznam pro ukládání úkolů (slovníků s názvem a popisem)
    ukoly = []

    # Hlavní smyčka programu
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
            break  # Ukončí smyčku a program
            
        else:
            print("\nNeplatná volba. Zadejte prosím číslo od 1 do 4.")
            input("\nStiskněte Enter pro návrat do menu...")

# Spuštění hlavní funkce programu
if __name__ == "__main__":
    main()
# ...existing code...