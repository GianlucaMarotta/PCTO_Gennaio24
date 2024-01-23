def inserimento_numeri():
    ripeti = True
    while ripeti == True: 
        n_input = float(input("quanti numeri vuoi inserire: "))
        resto_pari = n_input % 2
        if resto_pari != 0:
            resto_dispari = (n_input - 1) % 2
            if resto_dispari == 0:
                ripeti = False
        else:
            ripeti = False

    lista_numeri = [0]*int(n_input)

    for i in range(int(n_input)):
        lista_numeri[i] = float(input("inserisci il numero: "))

    return lista_numeri

def media_numeri(lista_numeri):
    somma = 0
    n_input = len(lista_numeri)
    for i in range(int(n_input)):
        somma = somma + lista_numeri[i]

    media = somma/n_input
    return media



lista_num = inserimento_numeri()
media = media_numeri(lista_num)
print(media)
    

