import random

juego = ["piedra", "papel", "tijera"]

while True:
    Computadora = random.choice(juego)
    Jugador = None

    while Jugador not in juego:
        Jugador = input("piedra, papel o tijera?: ").lower()
        if Jugador not in juego:
            print("Ingrese una opción válida")

    if Jugador == Computadora:
        print("Computadora:", Computadora)
        print("Jugador:", Jugador)
        print("Empate!")
    elif Jugador == "piedra":
        if Computadora == "papel":
            print("Computadora:", Computadora)
            print("Jugador:", Jugador)
            print("Perdiste!")
        elif Computadora == "tijera": # Usa 'elif' en lugar de 'if' para evitar chequeos innecesarios.
            print("Computadora:", Computadora)
            print("Jugador:", Jugador)
            print("Ganaste!")
    elif Jugador == "papel":
        if Computadora == "tijera":
            print("Computadora:", Computadora)
            print("Jugador:", Jugador)
            print("Perdiste!")
        elif Computadora == "piedra":
            print("Computadora:", Computadora)
            print("Jugador:", Jugador)
            print("Ganaste!")
    elif Jugador == "tijera":
        if Computadora == "piedra":
            print("Computadora:", Computadora)
            print("Jugador:", Jugador)
            print("Perdiste!")
        elif Computadora == "papel":
            print("Computadora:", Computadora)
            print("Jugador:", Jugador)
            print("Ganaste!")

    Jugar_de_nuevo = input("Quieres jugar de nuevo? (si/no): ").lower()

    if Jugar_de_nuevo != "si":
        break

print("Adios")
