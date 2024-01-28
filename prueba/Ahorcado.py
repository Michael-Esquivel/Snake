import random

palabra = ["MOTO", "CARRO", "CICLA"]
miPalabra = ""

randomWordl = random.choice(palabra)        #Escoge cualquier elemento de la lista
fallos = 0
while True:
    miletra = input("\n\nEscriba: ")
    miPalabra += miletra
    fallo = True
    
    for letra in randomWordl:
        if letra.upper() in miPalabra.upper():   #Esta linea funciona como un for ya que escanea cada letra de miPalabra
            print(letra.upper(), end = "")
            fallo = False
        else:
            print("_", end = " ")
            
    # Comprueba fallos      
    if miletra.upper() not in randomWordl:
        fallos += 1
    
    print(f"\tFallos: {fallos}")




    

