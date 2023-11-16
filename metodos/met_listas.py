
#crea una lista con list()
lista = list(["hola Alejandro", "tengo", 40])

resultado = len(lista) #devuelve la cantidad de elementos de una lista

lista.append("jajaja") #agrega un elemento a la lista original

lista.insert(2, "birrrra") #agrega en una posicion deseada

lista.extend(["hay caramba", 23]) #agrega varios elementos de una lista a otra lista
# se agregan al final

lista.pop(0) #elimina elemento por su indice,
# si pones pop(-1) elimina el ultimo, pop(-2) elimina el anteultimo, etc...

lista.remove(40) #remueve un elemento de la lista por su valor,
#caso no encuentre devuelve una excepcion(error)

lista.index() #busca el indice del elemento pedido si lo encuentra dentro de la lista
# si no encuentra nada, da una excepcion
#no se pueden usar el metodo index() en conjuntos!!!

print(lista)

lista.sort() # ordena toda la lista siempre y cuando sea solamente numeros, bolean tambien
#da una excepcion si hay cadena de texto

lista.sort(reverse=True) # invierte el orden

lista.reverse() #invierte el orden de la lista, este o no ordenada

lista.clear() #elimina todo de la lista1