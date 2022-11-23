#el corral
print("**************")
print("HAMBURGUESAS EL CORRAL")
print("**************")

nombreUsuario=input( "digita EL nombre del usuario: ")
cedula=int(input( "Digita tu cedula: "))
pedido=input( "digite su pedido: ")
valorHamburguesa=int(input("valor de la hamburguesa: "))
cantidadPedido=int(input("Digite cantidad del pedido: "))
total= cantidadPedido*valorHamburguesa

print("----------------------")
print(nombreUsuario,"su pedido fue: ")
print(cantidadPedido,"hamburguesas de:",pedido)
print("por un valor total de:",total)

print("----------------------")
