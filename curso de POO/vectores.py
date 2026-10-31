# listas

nombres = ["alice", "bob", "charlie"]

print(nombres[0])

nombres[2] = "juan"

print(nombres[2])

nombres.append("maria")

for i in range(len(nombres)):
    print(nombres[i])


# concatenación

nombre = "juan"
apellido = "perez"

completo = nombre + " " + apellido

print(completo)

print(f"hola, {nombre} {apellido}, bienvenido al programa")