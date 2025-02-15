# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''
nro1 = int(input('Ingrese el primer número\n'))
nro2 = int(input('Ingrese el segundo número\n'))

sim =  str(input('ingrese simbolo: + - / * ** o FIN'))


for nro in range(nro1,nro2):
    if sim == '+':
        resultado1 = nro1 + nro2
        print('suma' ,resultado1)
    elif sim == '-':
        resultado2 = nro1-nro2
        print('resta',resultado2 )
    elif sim == '/':
        resultado3 = nro1/nro2
        print('division',resultado3)
    elif sim == '*':
        resultado4 = nro1*nro2
        print('multiplicacion',resultado4 )
    else:
        resultado5 = nro1**2 
        print('exponente nro1', resultado5)
        resultado6 = nro2**2
        print('exponente nro2', resultado6)
for nro in range(nro1,nro2):
    if sim== 'FIN':
        break         
print('terminar')

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio
