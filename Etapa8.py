import Etapa10
LONGITUD_PALABRA_MINIMA = Etapa10.obtener_longitud_palabra_minima()
def ordenar_diccionario(diccionario):
    """"
            El objetivo de esta funcion es ordenar alfabeticamente el diccionario
        de palabras y definiciones
    - Nicolas Cardone
    """
    diccionario_ordenado = {}
    for palabra in sorted(list(diccionario.keys())):
        diccionario_ordenado[palabra] = diccionario[palabra]
    return diccionario_ordenado

# filtre tildes y las reemplace por letra sin tilde

def crear_archivo(diccionario):
    """"
            El objetivo de esta funcion es crear el archivo diccionario.csv con las palabras y definiciones
    - Nicolas Cardone
    """
    arch = open("diccionario.csv", "w" , encoding='utf-8')
    pa = list(diccionario.keys())
    defi = list(diccionario.values())
    for k in range(len(pa)):
        arch.write(pa[k] + ", '" + defi[k] + "'\n")
    arch.close()
def crear_diccionario(palabras, definiciones):
    """"
            Recibe una lista con las palabras y otra lista con sus respectivas definiciones.
            El objetivo de esta funcion es crear el diccinario con las palabras y sus definiciones correspondientes y devolverlo.
    - Nicolas Cardone
    """
    diccionario = {}
    palabras_no = []
    for i in range(len(palabras)):
        palabra = palabras[i]
        definicion = definiciones[i]
        diccionario[palabra] = definicion
    for clave in diccionario.keys():
        if len(clave) < LONGITUD_PALABRA_MINIMA:
            palabras_no.append(clave)
    for n in palabras_no:
        del diccionario[n]
    return diccionario
def obtener_lista_definiciones():
    """"
            El objetivo de esta funcion es leer cada archivo de texto y obtener las palabras
        y definiciones 
    - Nicolas Cardone
    """
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