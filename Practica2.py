#EJERCICIO 1
# Tupla de países
paises = ("Argentina", "México", "España", "Colombia", "Perú")


# Mostrar el tercer elemento (índice 2)
print("El tercer país es:", paises[2])



#EJERCICIO 2
# Diccionario con datos personales

persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Mostrar la edad
print("La edad es:", persona["edad"])



#EJERCICIO 3
#Calculadora Usando Funciones

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero"
    
# Prueba de la calculadora
print("Suma:", sumar(5, 3))
print("Resta:", restar(10, 4))
print("Multiplicación:", multiplicar(6, 7))
print("División:", dividir(20, 5))



#EJERCICIO 4
#Calculadora Usando Bibliotecas
import math

# Operaciones con math
a = 9
b = 2

print("Potencia:", math.pow(a, b))           # a^b
print("Raíz cuadrada de a:", math.sqrt(a))   # √a
print("Seno de a (rad):", math.sin(a))       # seno
print("Logaritmo de a:", math.log(a))        # logaritmo natural


