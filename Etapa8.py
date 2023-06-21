def ordenar_diccionario(diccionario):
    diccionario_ordenado = {}
    for palabra in sorted(list(diccionario.keys())):
        diccionario_ordenado[palabra] = diccionario[palabra]
    return diccionario_ordenado
def crear_archivo(diccionario):
    arch = open("diccionario.csv", "w" , encoding='utf-8')
    pa = list(diccionario.keys())
    defi = list(diccionario.values())
    for k in range(len(pa)):
        arch.write(pa[k] + "," + defi[k] + "\n")
    arch.close()
def crear_diccionario(palabras, definiciones):
    diccionario = {}
    palabras_no = []
    for i in range(len(palabras)):
        palabra = palabras[i]
        definicion = definiciones[i]
        diccionario[palabra] = definicion
    for clave in diccionario.keys():
        if len(clave) < 4:
            palabras_no.append(clave)
    for n in palabras_no:
        del diccionario[n]
    return diccionario
def obtener_lista_definiciones():
    palabras = []
    definiciones = []
    arch_1 = open("palabras.txt", encoding='utf-8')
    for linea in arch_1:
        linea = linea.rstrip("\n")
        if linea.isalpha():
            palabras.append(linea)
    arch_1.close()
    arch_2 = open("definiciones.txt", encoding='utf-8')
    for linea_2 in arch_2:
        linea_2  = linea_2 .rstrip("\n")
        definiciones.append(linea_2 )
    arch_2.close()
    dic = crear_diccionario(palabras, definiciones)
    dic = ordenar_diccionario(dic)
    crear_archivo(dic)
    return dic
obtener_lista_definiciones()