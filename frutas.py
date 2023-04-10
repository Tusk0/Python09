fruteria={"manzana":10 ,"pera":8,"aguacate":15,"mango":16,"limon":3,"guayaba":6,"Naranja":7}
print("Aguilar Flores Diego 4IV8")
print(f"Lista de frutas disponibles son:",fruteria.keys())
frut = input("Ingrese que fruta desea comprar:")
if frut in fruteria:
    cant= int(input("Cuantas frutas comprará?"))
    precio=cant*int(fruteria.get(frut))
    print("El a pagar por las frutas es: ",precio)
else:
    print("Esa fruta no está en la fruteria")
