usuario = {}

for i in range(5):
    nombre = input(f"Introduzca nombre {i+1}: ")
    edad = int(input(f"Introduzca edad de {nombre}: "))
    usuario[nombre] = edad

print("\nPersonas mayores de edad:")

for nombre, edad in usuario.items():
    if edad >= 18:
        print(f"- {nombre} tiene {edad} años.")
