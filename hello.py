numero_a_adivinar = 7

numero_del_usuario = int(input("adivina el numero: "))

if numero_a_adivinar == numero_del_usuario:
    print("adivinaaste")
else:
    numero_del_usuario = int(input("vuelve a intentarlo: "))

if numero_del_usuario == numero_a_adivinar:
    print("adivinaaste")

else:
    numero_del_usuario = int(input("ultimo uintento: "))

if numero_del_usuario ==  numero_a_adivinar:
    print("adivinaaste")

else:
    print("A la mierda")











