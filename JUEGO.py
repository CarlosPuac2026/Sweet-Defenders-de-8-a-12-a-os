print("🍬 DULCE INVASIÓN 🍬")
print("Los monstruos de dulces invadieron la ciudad.")

nombre = input("Escribe el nombre de tu héroe: ")

vida = 3
puntos = 0

print("\n¡Hola", nombre + "!")
print("Tienes 3 vidas.")

while vida > 0:

    print("\n¿Qué quieres hacer?")
    print("1. Atacar al monstruo de galleta")
    print("2. Escapar")
    
    opcion = input("Elige: ")

    if opcion == "1":
        print("¡Atacaste al monstruo!")
        puntos = puntos + 100
        print("Ganaste 100 puntos.")

    elif opcion == "2":
        print("¡Escapaste!")
        vida = vida - 1
        print("Perdiste una vida.")

    else:
        print("Opción incorrecta.")

    print("Vidas:", vida)
    print("Puntos:", puntos)

    if puntos >= 300:
        print("\n🎉 ¡GANASTE!")
        print("Derrotaste al monstruo de algodón de azúcar.")
        break

if vida == 0:
    print("\n💀 PERDISTE")
    print("Los monstruos convirtieron la ciudad en azúcar.")
print("🍬 DULCE INVASIÓN 🍬")
print("Los monstruos de dulces invadieron la ciudad.")

nombre = input("Escribe el nombre de tu héroe: ")

vida = 3
puntos = 0

print("\n¡Hola", nombre + "!")
print("Tienes 3 vidas.")

while vida > 0:

    print("\n¿Qué quieres hacer?")
    print("1. Atacar al monstruo de galleta")
    print("2. Escapar")
    
    opcion = input("Elige: ")

    if opcion == "1":
        print("¡Atacaste al monstruo!")
        puntos = puntos + 100
        print("Ganaste 100 puntos.")

    elif opcion == "2":
        print("¡Escapaste!")
        vida = vida - 1
        print("Perdiste una vida.")

    else:
        print("Opción incorrecta.")

    print("Vidas:", vida)
    print("Puntos:", puntos)

    if puntos >= 300:
        print("\n🎉 ¡GANASTE!")
        print("Derrotaste al monstruo de algodón de azúcar.")
        break

if vida == 0:
    print("\n💀 PERDISTE")
    print("Los monstruos convirtieron la ciudad en azúcar.")
