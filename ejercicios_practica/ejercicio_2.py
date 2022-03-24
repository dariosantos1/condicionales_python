# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda
if texto_1 > texto_2 :
    print ("La primera palabra es mayor a la segunda")
elif texto_1 == texto_2 :
    print ("Ambas palabras son iguales")
else :
    print ("la segunda palabra es mayor a la primera")


# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda
if len (texto_1) > len(texto_2) :
    print ("La primera palabra tiene mas caracteres que la segunda")
elif len (texto_1) == len (texto_2) :
    print ("Ambas palabras tienen la misma cantidad de caracteres")
else :
    print ("La segunda palabra tiene mas caracteres que la primera")

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda
if texto_1 [0] > texto_2 [0] :
    print ("La primera letra de la primera palabra es mayor a la primera letra de la segunda palabra")
elif texto_1 [0] == texto_2 [0] :
    print ("La primera letra de la primera palabra es igual a la primera letra de la segunda palabra")
else :
    print ("La primera letra de la segunda palabra es mayor a la primera letra de la primera palabra")


copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda
if copia_texto_1 == texto_1 :
    print ("La variable copia_texto1 es igual a" , texto_1)
# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda
if copia_texto_1 != texto_2 :
    print ("la variable copia_texto1 es distinta a" , texto_2)

