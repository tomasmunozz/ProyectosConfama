
contador=[]
for i in range(10):
    num= int(input("Ingrese un numero: "))
    if num % 3 ==0:
        contador.append(num)

print ( f" En la lista de numeros hay {len (contador)} multiplos de 3 {(contador)}" )