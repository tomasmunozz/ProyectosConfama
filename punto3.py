opcion= 100

print("Menu supermerado")
print("****************")

print ("Opcion 1: Agregar producto a la lista ")
print ("Opcion 2: Mostrar productos registrados ")
print ("Opcion 3: Elimina ultimo producto de la lista ")
print ("Digita 0 para salir")

productos=[]
while opcion !=0:
    opcion= int(input("Digite una opcion: "))
    
    if opcion==1:
        producto=input("Digita nombre del producto: ")
        productos.append (producto)

    elif opcion==2:
        for producto in productos:
            print (productos)

    elif opcion==3:
        productos.pop()
        print (productos)

    elif opcion==0:
        
        break
   
    else: 
        print("Selecciona una opcion valida ")

