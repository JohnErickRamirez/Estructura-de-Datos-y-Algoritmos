#EJERCICIO 1
#Area de un Rectángulo.
# El usuario debe ingresar el largo y el ancho Rectángulo.

largo = float(input("Ingresa el largo del rectángulo: "))
ancho = float(input("Ingresa el ancho del rectángulo: "))

# Calcular el área
area = largo * ancho

# Mostrar el resultado
print(f"El área del rectángulo es: {area}")

# EJERCICIO 2
# Solicitar al usuario la temperatura en Celsius
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# Convertir a Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Mostrar el resultado
print(f"{celsius}°C equivale a {fahrenheit}°F")

# EJERCICIO 3

#Introduccion de los valores

# Definir dos números complejos
num1 = complex(3, 4)  # 3 + 4j
num2 = complex(1, 2)  # 1 + 2j

# Sumar los números complejos
resultado = num1 + num2

# Mostrar el resultado
print(f"La suma de {num1} y {num2} es: {resultado}")


# EJERCICIO 4
nombre = input("Por favor, ingresa tu nombre: ")
print(f"¡Bienvenido, {nombre}!")

# EJERCICIO 5
edad = int(input("Por favor, ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# EJERCICIO 6

# Solicitar números al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else "No se puede dividir entre 0"

# Mostrar resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

# ejercicio 7
# Solicitar número al usuario
num = float(input("Ingresa un número: "))

# Determinar si es positivo, negativo o cero
if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

# ejercicio 8
# Solicitar número al usuario
num = int(input("Ingresa un número: "))

# Verificar si es par o impar
if num % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# ejercicio 9

for num in range(1, 11):
    print(num)

# ejercicio 10

# Inicializar la suma
suma = 0

while True:
    num = float(input("Ingresa un número (0 para salir): "))
    
    if num == 0:
        break  # Salir del bucle si el usuario ingresa 0
    
    suma += num  # Sumar el número ingresado

print(f"La suma total es: {suma}")