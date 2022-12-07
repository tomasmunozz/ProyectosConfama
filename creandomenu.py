opcion=100

print("Empanadas machetico")
print("*******************\n")

print("1. Registrar empanada")
print("2. Ver empanada")
print("0. Salir ")


empanadas=[]
while opcion !=0:
    opcion=int(input("Digita una opcion: "))
    if opcion==1:
        empanada=input("Digite el nombre de la empanada a registrar: ")
        empanadas.append(empanada)

    elif opcion==2:
        print(f'La empanada registrada en base de datos es: {empanadas} y es rica')
        for empanada in empanadas
        print(f"La empanada seleccionada es: {empanada} ")
    
    elif opcion==0:
        break
    
    else: 
        print("Debe seleccinar una opcion valida...")
