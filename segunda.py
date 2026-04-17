#bucle 
secuencia = []

for i in range(5):
    numero = int(input(f"Introduzca el número {i+1}: "))
    secuencia.append(numero)

suma_total = 0
for i in secuencia:
    suma_total += i

promedio = suma_total / len(secuencia)

print(f"Suma total: {secuencia}")
print(f"Promedio: {promedio}")