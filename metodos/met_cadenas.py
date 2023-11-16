
cadena1="hola soy Alejandro"
cadena2="tengo 40 años"

print(dir(cadena1)) 

# la funcion "dir" me ofrece todal los métodos que tengo para hacer de esa variable:
#['__add__', '__class__', '__contains__','__delattr__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
# '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__',
# '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs',
# 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
# 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace',
# 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
# 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpart',
# 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
# 'swapcase', 'title', 'translate', 'upper', 'zfill']

resultado = cadena1.upper() # tranforma a mayuscula
resultado = cadena1.lower() # tranforma a minuscula
resultado = cadena1.capitalize() #solamente primer letra en mayuscula

resultado = cadena1.find("hola") #devuelve 0 que es la posicion donde esta lo que busca
#devuelve -1 si no encuentra nada

resultado = cadena1.index("h") #devuelve lo mismo que el find() pero en cqso que no encuentre
#devuelve una excepcion, como si fuera un error 

resultado = cadena1.isnumeric() #devuelve un bolean

#resultado = cadena1.isalpha() # devuleve bolean si es alfanumerico
#(solo a-z/A-Z sin espacios,)

resultado = cadena1.count("a") #devuelve la cantidad de veces hay lo que busca, 
# 0 si no encuentra nada.

resultado = len(cadena1) #devuelve cantidad de caracteres de una cadena, por ej 27.
# len es una funcion, no un método

resultado = cadena1.startswith("h") #devuelve bolean si empieza con una letra o cadena
#determinada 

resultado = cadena1.endswith("h") #devuelve bolean si termina con una letra o cadena
#determinada 

resultado = cadena1.replace("hola", "chau") #reemplaza letra, cadena o simbolos por otra dada
#si encuentra coincidencia en en primer parametro, si no encuentra imprime como es!

resultado = cadena1.split() #crea una lista y separa todo por el parametro que le pase
#por ej: , ; - 

print(resultado)




