lista = []

def aggiunta():
    item = input("Inserisci un elemento alla lista: ")
    item = item.lower()  
    lista.append(item)

def stampaLista():
    print(lista)

def eliminaElemento():
    print(lista)
    risp = input("Inserisci il nome dell'elemento che vuoi eliminare: ")
    risp = risp.lower()  
    if risp in lista:
        lista.remove(risp)
    else:
        print("Elemento non trovato nella lista.")

controllo = True
while controllo:
    print("1) aggiungi un numero alla lista")
    print("2) visualizza la lista")
    print("3) elimina un elemento dalla lista")
    x = input("Inserisci il numero dell'azione che vuoi eseguire: ")

    try:
        x = int(x)  
        if x == 1: 
            aggiunta()
        elif x == 2:
            stampaLista()
        elif x == 3:
            eliminaElemento()
        else:
            uscita = input("Vuoi uscire (y/n): ")
            uscita = uscita.lower()
            if uscita == "y":
                controllo = False
    except ValueError:
        print("Per favore, inserisci un numero valido.")