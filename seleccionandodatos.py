#entradas de problema
niveldeagua = int(input("Digite nivel de agua:"))

# evaluando caminos multiples (mas de 2)
if niveldeagua <=100:
    print("Nivel de agua bajo")
elif niveldeagua >100 and niveldeagua <400:
    print("operacion optima")
elif niveldeagua >=400:
    print("peligro")
else:
    print("nivel de agua no valido")

