# Ejercicio 1: Definición de Variables
# Define dos variables llamadas 'nombre' y 'edad' con tus datos y muestra un mensaje que diga "Hola, [nombre], tienes [edad] años."
nombre = "Juan"
edad = 25
print("Hola,", nombre + ", tienes", edad, "años.")

# Ejercicio 2: Cambio de Tipo de Variable
# Define una variable llamada 'numero_entero' con un número entero y otra llamada 'numero_flotante' con un número flotante. Luego, convierte 'numero_entero' a flotante y 'numero_flotante' a entero, y muestra ambos resultados.
numero_entero = 10
numero_flotante = 5.5

numero_entero = float(numero_entero)
numero_flotante = int(numero_flotante)

print("Número entero convertido a flotante:", numero_entero)
print("Número flotante convertido a entero:", numero_flotante)

# Ejercicio 3: Uso de Print
# Muestra un mensaje que diga "Python es divertido!" en una sola línea, usando tres instrucciones print separadas.
print("Python", end=" ")
print("es", end=" ")
print("divertido!")
