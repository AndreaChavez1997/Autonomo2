#Genera aleatoriamente
import random
print(" Bienvenidos a Piedra, Papel o Tijera ")
juego = True
#Iniciamos un bucle para que el juego continúe o se detenga
while juego:
    #Creamos una función
    def jugar():
        #Se crea una lista de los elementos del juego (Estructura de datos)
        opc = ["piedra", "papel", "tijera"]
        nombre = input("Por favor escribe tu nombre: ")
        #Se solicita el nombre para que sea personalizado
        #Se utiliza la funcion lower para que internamente las letras se conviertan en 
        #minúsculas y no salte error
        usuario = input(f"{nombre} elige una opción (piedra, papel, tijera): \n").lower()
        #Condicional en caso de escribir algo diferente a las opciones
        if usuario not in opc:
            print("Opción no válida. Inténtalo de nuevo.")
            return
        
        #Almacena en una variable el elemento aleatorio del programa
        sistema = random.choice(opc)
        print("Piedra, papel o tijera 1,2 y 3!\n")
        print(f"Tu elegiste:       {usuario}")
        print(f"El sistema eligió: {sistema}\n")
        #Compara la selección del usuario y la máquina
        if usuario == sistema:
            #En caso de que sean iguales
            print("Ninguno nada, es empate")
            
        elif (sistema == "papel" and usuario == "tijera") or \
             (sistema == "tijera" and usuario == "piedra") or \
             (sistema == "piedra" and usuario == "papel"):
            print("¡Ganaste!")
        else:
            #Si no cumple con ninguna de las condiciones
            print("Perdiste. Inténtalo de nuevo.")

    if __name__ == "__main__":
        #Se almacena la función
        jugar()
        #Parte final del bucle
    respuesta = input("¿Quieres jugar nuevamente? (s/n): \n").lower()
    if respuesta != 's':
        juego = False
        print("Gracias por visitarnos. Vuelve pronto para jugar")

