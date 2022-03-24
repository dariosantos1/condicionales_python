# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda
if numero_1 > numero_2 :
    print ("El número mayor es:", numero_1)
if numero_1 == numero_2 :
    print ("Ambos numeros son iguales")
else : 
    print ("El número mayor es:", numero_2)

# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso
if numero_1 > 0 : 
    print ("El numero 1 es positivo")
if numero_1 < 0 :
    print ("el numero 1 es negativo")
if numero_1 == 0 :
    print ("El numero 1 es cero")

# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición
if numero_1 > 0 and numero_1 < 100 :
    print ("El numero 1 es mayor a 0 y menor a 100")
else :
    print ("el numero 1 no se encuentra en el rango de 0 a 99")

# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición
if numero_1 < 10 :
    print ("El numero 1 es menor a 10")
else : 
    print ("El numero 1 no es menor a 10")
if numero_2 > -2 :
    print ("El numero 2 es mayor a -2")
else : 
    print ("El numero 2 no es mayor a -2")

