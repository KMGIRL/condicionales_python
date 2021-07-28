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

if texto_1 > texto_2:
    print('{} es mayor que {}'.format(texto_1, texto_2))
else:
    print('{} es mayor que {}'.format(texto_2, texto_1))


# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según correspond

if len(texto_1) > len(texto_2):
    print('el texto 1 es mas largo que el texto 2')
else:
    print('el texto 1 es mas corto que el texto 2')
    
# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

if texto_1[0] > texto_2[0]:
    print("la primera del texto 1 es mayor")
else:
    print("la primera del texto2 es mayor")



copia_texto_1 = texto_1  # Copia de la variable texto_1

if copia_texto_1 == texto_1:
    print("la copia del texto1 es igual al texto 1")
else:
    print("no son iguales las copias")    

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

if texto_2 != copia_texto_1:
    print("el texto 2 no es igual a la copia texto 1")
else:
    print(" el texto2 es igual a la copia texto1 ")
# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda
