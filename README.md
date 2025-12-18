# Juego Piedra, papel o tijera
Este programa representa al típico juego de piedra, papel o tijera, en el cual existen 2 jugadores que será el usuario y la máquina.
Mediante el lenguaje de Python, como inicio se hará la declaración de variables y uso de las diferentes estructuras que nos permita alcanzar el objetivo de que la máquina aleatoriamente nos de un elemento y se ponga a comparación con el elemento que el usuario elija. (07/12/2025)

Se trabajará con variables, operadores, mecanismos de flujo, estructuras y funciones que permitan desarrollar el juego adecuadamente.

Se hicieron uso de las siguientes variables, cada una almacenando la información necesaria dependiendo de su funcionalidad:
* opc: es una variable tipo lista, la cual almacena múltiples elementos en un solo objeto permitiendo que sus valores sean modificados
* nombre: es una variable   de tipo string o cadena de texto
* usuario: es una variable   de tipo string o cadena de texto
* sistema: es una variable   de tipo string o cadena de texto, pero implementada con una función que devuelve un único elemento aleatorio
* juego: es una variable de tipo booleano (True, False)


Para la facilidad del juego, previo a una investigación, se hizo uso de una función que la llamaremos "jugar", la cual consiste en que se generará un conjunto o un bloque de código personalizado, donde tendrá todas las instruccines principales del juego que es comparar los dos elementos del usuario y el sistema y eligir el ganador.
* Función
  
def jugar():

jugar()


Por otra parte, se encontró una librería que actúa como un random provider, para que la máquina elija una opción aleatoriamente:
import random
Para la toma de decisión se complementará con la asignación de la variable y la función de la siguiente manera:

  sistema = random.choice(opc)
  
Donde  random.choice es la función que selecciona un solo elemento al azar de la lista que se encuentra dentro del paréntesis, que en este caso, pertenece a la variable opc que almacena una lista de elementos.



Para cumplir con el objetivo del programa, que es la simulación del juego Piedra, papel o tijera, en la cual debe compararse los elementos seleccionados por ambos jugadores, se hace uso de los condicionales IF, ELIF, ELSE de la siguiente manera:


  if usuario == sistema:

              print("Ninguno nada, es empate")  

          elif (sistema == "papel" and usuario == "tijera") or \

               (sistema == "tijera" and usuario == "piedra") or \

               (sistema == "piedra" and usuario == "papel"):

              print("¡Ganaste!")

          else:

              print("Perdiste. Inténtalo de nuevo.")

Con ellos comparamos todas las alternativas que se pueden presentar para determinar si se gana el juego, se pierde o existe un empate.



Finalmente se agregó un bucle WHILE para que se cumpla la funcionalidad de iniciar y finalizar el juego, es decir, que se va a repetir las veces necesarias hasta que el usuario o jugador decida finalizar y salir del juego. Para ellos también se hizo uso de las variables tipo booleanas, de la siguiente manera:

  
  juego = True

  while juego:

  respuesta = input("¿Quieres jugar nuevamente? (s/n): \n")

      if respuesta != 's':

          juego = False

          print("Gracias por visitarnos. Vuelve pronto para jugar")

