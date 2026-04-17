#primera

entrada = int(input("Introduzca su numero: "))

def filtro(numero):
    if numero % 2 == 0:
        return "Es par"
    else:
        return "Es impar"

salida = filtro(entrada)
print(salida)
