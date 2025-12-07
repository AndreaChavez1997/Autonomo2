import random
#Se genera aleatoriamente
opciones = ["piedra", "papel", "tijera"]
#variables
print("BIENVENIDOS AL JUEGO\n")
print("Ingresa tu nombre\n")
    
   print(f"Escoje piedra, papel o tijera: {opciones}")
    jugador = input("Elige piedra, papel o tijera): ").lower()
    #print(f"La computadora eligió: {computadora}")
    computadora = random.choice(opciones)
    if jugador == computadora:

        print("¡Juega otra vez!\n")
    elif (
        (jugador == "piedra" and computadora == "tijera")
     
    ):
        print("¡Ganaste!\n")
    else:
         (jugador == "papel" and computadora == "piedra") 
