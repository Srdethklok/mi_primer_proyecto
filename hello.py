numero_a_adivinar = 7

numero_del_usuario = int(input("adivina el numero: "))

if numero_a_adivinar == numero_del_usuario:
    print("Has ganado")
    input(exit())


else:
    numero_del_usuario = int(input("vuelve a intentarlo: "))


if numero_del_usuario == numero_a_adivinar:
    print("has ganado")
    input(exit())


else:
    numero_del_usuario = int(input("ultimo intento: "))

if numero_del_usuario ==  numero_a_adivinar:
    print("Has ganado")


else:
    print("A la mierda")