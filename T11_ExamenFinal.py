#Programa que calcula con que frecuencia aparecen las primeras letras del abecedario en un texto
#Gianluca de la Rosa Bandini A01736162
lista_de_letra_a = []
lista_de_letra_b = []
lista_de_letra_c = []
lista_de_letra_d = []
lista_de_letra_e = []
lista_de_primeras_5_letras = []

archivo = open("T11_ElCoheteDePapel.txt", "r")
linea = archivo.readline()

for letra in linea:
    if letra == "a":
        lista_de_letra_a.append(letra)
    elif letra == "b":
        lista_de_letra_b.append(letra)
    elif letra == "c":
        lista_de_letra_c.append(letra)
    elif letra == "d":
        lista_de_letra_d.append(letra)
    elif letra == "e":
        lista_de_letra_e.append(letra)

for letra in linea:
    if letra == "a" or letra == "b" or letra == "c" or letra == "d" or letra == "e":
        lista_de_primeras_5_letras.append(letra)

cantidad_de_primeras_5_letras = len(lista_de_primeras_5_letras)
cantidad_de_a = len(lista_de_letra_a)
cantidad_de_b = len(lista_de_letra_b)
cantidad_de_c = len(lista_de_letra_c)
cantidad_de_d = len(lista_de_letra_d)
cantidad_de_e = len(lista_de_letra_e)

print("La cantidad de veces que aparecen las letras a, b, c, d y e son:", cantidad_de_primeras_5_letras, "veces")
print("La letra a se repite: ", cantidad_de_a, "veces")
if cantidad_de_a <= 5:
    print("La categoría de repetición de a es BAJA")
elif 5 < cantidad_de_a <= 10:
    print("La categoría de repetición de a es MEDIA")
elif 10 < cantidad_de_a <= 15:
    print("La categoría de repetición de a es MEDIA-ALTA")
else:
    print("La categoría de repetición de a es ALTA")

print("La letra b se repite: ", cantidad_de_b, "veces")
if cantidad_de_b <= 5:
    print("La categoría de repetición de b es BAJA")
elif 5 < cantidad_de_b <= 10:
    print("La categoría de repetición de b es MEDIA")
elif 10 < cantidad_de_b <= 15:
    print("La categoría de repetición de b es MEDIA-ALTA")
else:
    print("La categoría de repetición de b es ALTA")

print("La letra c se repite: ", cantidad_de_c, "veces")
if cantidad_de_c <= 5:
    print("La categoría de repetición de c es BAJA")
elif 5 < cantidad_de_c <= 10:
    print("La categoría de repetición de c es MEDIA")
elif 10 < cantidad_de_c <= 15:
    print("La categoría de repetición de c es MEDIA-ALTA")
else:
    print("La categoría de repetición de c es ALTA")

print("La letra d se repite: ", cantidad_de_d, "veces")
if cantidad_de_d <= 5:
    print("La categoría de repetición de d es BAJA")
elif 5 < cantidad_de_d <= 10:
    print("La categoría de repetición de d es MEDIA")
elif 10 < cantidad_de_d <= 15:
    print("La categoría de repetición de d es MEDIA-ALTA")
else:
    print("La categoría de repetición de d es ALTA")

print("La letra e se repite: ", cantidad_de_e, "veces")
if cantidad_de_e <= 5:
    print("La categoría de repetición de e es BAJA")
elif 5 < cantidad_de_e <= 10:
    print("La categoría de repetición de e es MEDIA")
elif 10 < cantidad_de_e <= 15:
    print("La categoría de repetición de e es MEDIA-ALTA")
else:
    print("La categoría de repetición de e es ALTA")