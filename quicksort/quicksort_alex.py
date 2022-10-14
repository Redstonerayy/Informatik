
liste = [3, 4, 1, 6, 7, 2, 1, 1, 0, 6]

def quicksort(liste):
    # eine Liste aus einem oder null Elementen zurückgeben
    # Rekursionsanker
    if len(liste) <= 1:
        return liste
    
    # Pivotelement festlegen (das erste Element)
    pivot = liste[0]

    # Teillisten erstellen
    kleinere = []
    groessere = []
    # Elemente den Teillisten zuordnen
    for i in range(1, len(liste)):
        if liste[i] < pivot:
            kleinere.append(liste[i])
            continue
        groessere.append(liste[i])
    
    # Algorithmus auf Teillisten anwenden -> Rekursionsschritt und Rekursionsabstieg
    # Teilergebnisse zusammensetzen -> Rekursionsaufstieg
    # Ergebnis zurückgeben
    return quicksort(kleinere) + [pivot] + quicksort(groessere)

if __name__ == "__main__":
    print(quicksort(liste))
