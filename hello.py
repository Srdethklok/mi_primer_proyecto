numero_a_adivinar = 4

numero_del_usuario = int(input("numero a adivinar: "))



if numero_del_usuario == numero_a_adivinar:
    print("Acertaste")

else:
    numero_del_usuario = int(input("prueba otra vez: "))

if numero_del_usuario == numero_a_adivinar:
    print("Acertaste")

else:
    numero_del_usuario = int(input("ultimo intento: "))

if numero_a_adivinar == numero_del_usuario:
    print("Acertaste")

else:
    print("A cagar")










