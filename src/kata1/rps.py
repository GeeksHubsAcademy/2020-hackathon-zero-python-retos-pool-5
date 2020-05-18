from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    player = player.lower()
    ai = ai.lower()
    mensaje = ''

    if player == ai:
        mensaje = 'Empate!'

    elif player == "piedra":
        if ai.lower() == "papel":
            mensaje = 'Perdiste!'
        else:
            mensaje = 'Ganaste!'

    elif player == "papel":
        if ai.lower() == "tijeras":
            mensaje = 'Perdiste!'
        else:
            mensaje = 'Ganaste!'

    elif player == "tijeras":
        if ai == "piedra":
            mensaje = 'Perdiste!'
        else:
            mensaje = 'Ganaste!'

    return mensaje

# Entry Point
def Game():
    player = input("Introduce piedra papel o tijera: ")
    ai = options[randint(0, 2)]
    winner = quienGana(player, ai)

    print(winner)
