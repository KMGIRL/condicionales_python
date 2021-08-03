# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y calcule a sumatoria total de todos los números dentro de esa secuencia
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

#inicio = int(input('Ingrese el primer número de la secuencia\n'))
#fin = int(input('Ingrese el último número de la secuencia\n'))
sumatoria = 0  # Inicializo el contador en 0

lista =[]
inicio = int(input('Ingrese el primer número de la secuencia\n'))
fin = int(input('Ingrese el primer número de la secuencia\n'))

for i in range(inicio-1,fin):
    print(i)
for i in range(inicio-1, fin):
    sumatoria =+ i + i-1 
    print('sumatoria:', sumatoria) 


    
#for numero in lista:
#    sumatoria += numero
#    print('numero =', numero, 'sumatoria', sumatoria)




# for ... in range(....)

# Imprimir el valor de la sumatoria

print("terminamos!")
