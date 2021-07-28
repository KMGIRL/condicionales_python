# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

palabra1= str(input('ingrese palabra 1: '))
palabra2 = str(input('ingrese palabra 2:'))
palabra3 = str(input('ingrese palabra 3:'))
print('como quieres ordenar las palabras ?')
seleccion = input('(1) orden alfabetico-(2) cantidad de letras')

if seleccion == 1 and palabra1 > palabra2 and palabra1>palabra3:
    print('palabra 1 es mayor')
elif palabra2 > palabra1 and palabra2 > palabra3:
    print('palabra2 es mayor')
elif palabra3 > palabra1 and palabra3 > palabra2:
    print('palabra 3 es mayor')        
else:
    print( 'son iguales las palabras ')

if seleccion ==2 and len(palabra1) >len(palabra2) and len(palabra1)>len(palabra1):
    print('palabra 1 es mayor')
elif len(palabra2)>len(palabra1) and len(palabra2)>len(palabra3):
    print('palabra 2 es mayor')
elif len(palabra3)> len(palabra1) and len(palabra3) > len(palabra2):
    print('la palabra 3 es mayor')        

    