import doctest
from doctest import testmod
PTO_ACIERTO=10
PTO_ERROR=-3
PRIMERA_LETRA = 0
POSICION_PALABRA = 0
MIN_LETRAS = 5
PRIMERA_LETRA = 0

#--------------------------------------------------------------------MODIFICACION DE FUNCIONES ETAPA :1-----------------------------------------------------------------------------
"""
Para poder cumplir con la consigna tuvimos que realizar modificaciones para adaptar las funciones al modulo doctest,
sin embargo, las demás funciones no se pueden adaptar ya que tienen un llamado a random que lo hace impredecible 

"""


"""def tablero(palabras, palabras_significado):



 
    puntos=0
    iniciales=[]
    palabra_completa=[]
    respuesta=[]
    letras=[]
    significado=[]
    
    for llaves,valor in palabras.items():
        iniciales.append(f"[{llaves}]")
        palabra_completa.append(valor)
        respuesta.append('[ ]')
    for letters,meaning in palabras_significado.items():
        letras.append(f"[{letters}]")
        significado.append(meaning)
    j=0 
    aciertos=0
    errores=0
    historial=[]
    while j<len(iniciales):
        print("".join(iniciales))
        print("".join(respuesta))
        print("                           ")
        print(f"Aciertos: {aciertos}")
        print(f"Errores: {errores}")
        print(f"Turno letra {iniciales[j][1]} -palabra de {len(palabra_completa[j])} letras")
        print(f"Definición: {significado[j]} ")
        pregunta=input('Ingrese una palabra: ')
        
        
        if pregunta ==palabra_completa[j]:
                respuesta[j]='[a]'
                aciertos+=1
                puntos+=PTO_ACIERTO
                historial.append(f"Turno letra {iniciales[j][1]}-palabra de {len(palabra_completa[j])} letras - acierto")
                j+=1
        else:
                respuesta[j]='[e]'
                errores+=1
                puntos+=PTO_ERROR
                historial.append(f"Turno letra {iniciales[j][1]}-palabra de {len(palabra_completa[j])} letras - error - palabra correcta: {palabra_completa[j]}")
                j+=1

    print("".join(iniciales))
    print("".join(respuesta))
    return puntos"""

def letra_palabra():
    
    lista_vieja =["algoritmos"]
    palabra_significado={}
    dicc={"algoritmos":"materia informatica del primer cuatrimestre de ing. informatica"}

    for word in lista_vieja:
        palabra_significado[word]=dicc[word]

    return  palabra_significado

#--------------------------------------------------------------------MODIFICACION DE FUNCIONES ETAPA :3-----------------------------------------------------------------------------
"""def eleccion_palabras_candidatas(diccionario, lista):
    
    palabras_candidatas = []
    palabras = diccionario.keys()
   
    for palabra in palabras:
        if palabra[PRIMERA_LETRA] in lista:
            palabras_candidatas.append(palabra)
            lista.remove(palabra[PRIMERA_LETRA])
    return sorted(palabras_candidatas)"""#------------------------------------------------------------------MODIFICACION DE FUNCIONES ETAPA :2-------------------------------------------------------------------------------
"""def impresiones ( palabras_candidatas ) :


    lista = list( palabras_candidatas.keys() )

    palabras_por_letras= {}
    
    for i in range(len(lista)) :

        contador_De_letras = 0


        for j in range(len(lista)) :

            
            if ( lista[i][0] == lista[j][0] ) :
 
                contador_De_letras+=1
            
        palabras_por_letras[ lista[i][0] ] = contador_De_letras

    print('Letras y cuantas veces estan: ', palabras_por_letras)

    for elem in palabras_por_letras :


        if ( palabras_por_letras[elem] == 1 ) :
            
            print( 'Hay', palabras_por_letras[elem], 'palabra que empieza con la letra', elem )
        
        else:
            

            print( 'Hay', palabras_por_letras[elem], 'palabras que empiezan con la letra', elem )
   

    print('La cantidad total de palabras candidatas son:', len(palabras_candidatas))"""

"""def generar_palabras_candidatas () : 
    palabras_candidatas = {}
    
    lista_de_listas =datos_prueba()



    indice = 0

    while ( indice < len(lista_de_listas)):

        if( len( lista_de_listas[indice][ POSICION_PALABRA] ) >= MIN_LETRAS) :

            palabras_candidatas[lista_de_listas[indice][POSICION_PALABRA]] = lista_de_listas[indice][1]

        indice+=1


    return palabras_candidatas"""

#-----------------------------------------------------------------------ETAPA 7----------------------------------------------------------------------------------------------
def obtener_usuarios_claves():
    """"
        El objetivo de esta funcion es obtener los nombres de usuario y su contraseña para ingresar
        al juego
    - Nicolas Cardone
    """
    diccionario = {}
    archivo = open("usuarios.csv", "r")
    for linea in archivo:
        usuario,clave = linea.rstrip("\n").split(",")
        diccionario[usuario] = clave
    archivo.close()
    return diccionario
def validar_usuario(usuario, usuarios):
    """"
        El objetivo de esta funcion es comprobar que el usuario sea correcto
    - Nicolas Cardone
    """
    validez = True
    if usuario in usuarios:
        validez = False
    elif len(usuario) < 4 or len(usuario) > 20:
        validez = False
    elif not usuario.isalnum():
        for caracter in usuario:
            if not caracter.isalnum() and caracter != "-":
                validez = False
    return validez

#-----------------------------------------------------------------------ETAPA 9----------------------------------------------------------------------------------------------
def puntaje(dicc_puntaje_jugadores,lista_participantes):
    cadena=""
    for nombre,puntos in dicc_puntaje_jugadores.items():
        cadena+=f" {lista_participantes.index(nombre)+1}.{nombre} = {puntos} puntos"
    return cadena
def listado(historial_turno):
    """
    almacena el historial de juego en cada tablero para mostrar al final en formato
    cadena una lista de errores y aciertos
    -Agustín Demicheli-
    """
    lista=""
    for intentos in historial_turno:
        lista+=intentos
    return lista    
#-------------------------------------------------------------------------Etapa 10-------------------------------------------------------------------------------------------
def obtener_longitud_palabra_minima():
        """"
                El objetivo de esta funcion es devolver la longitud de palabra minima
        - Nicolas Cardone
        """
        return int(dic["LONGITUD_PALABRA_MINIMA"])
    
def obtener_cantidad_letras_rosco():
        """"
                El objetivo de esta funcion es devolver la cantidad de letras del rosco
        - Nicolas Cardone
        """
        return int(dic["CANTIDAD_LETRAS_ROSCO"])
    
def obtener_maximo_partidas():
        """"
                El objetivo de esta funcion es devolver el maximo de partidas a jugar
        - Nicolas Cardone
        """
        return int(dic["MAXIMO_PARTIDAS"])
    
def obtener_puntaje_acierto():
        """"
                El objetivo de esta funcion es devolver cuantos puntos suma un acierto
        - Nicolas Cardone
        """
        return int(dic["PUNTAJE_ACIERTO"])

def obtener_puntaje_desacierto():
        """"
                El objetivo de esta funcion es devolver cuantos puntos resta un desacierto
        - Nicolas Cardone
        """
        return int(dic["PUNTAJE_DESACIERTO"])
    
arch = open("configuracion.csv", encoding='utf-8')
dic = {}
for linea in arch:
    nombre, valor = linea.rstrip("\n").split(",")
    dic[nombre] = valor
#-------------------------------------------------------------------------PRUEBAS UNITARIAS----------------------------------------------------------------------------------
def main():

    """    
>>> puntaje({'agus':20,'nico':20},['agus','nico'])
' 1.agus = 20 puntos 2.nico = 20 puntos'
>>> listado(['turno letra a- palabra 4 letras acierto','turno letra c- palabra de 6 letras error- palabra correcta: cabras']) 
'turno letra a- palabra 4 letras aciertoturno letra c- palabra de 6 letras error- palabra correcta: cabras'
>>> letra_palabra()
{'algoritmos': 'materia informatica del primer cuatrimestre de ing. informatica'}
>>> obtener_puntaje_desacierto()
3
>>> obtener_puntaje_acierto()
10
>>> obtener_maximo_partidas()
5
>>> obtener_cantidad_letras_rosco()
10
>>> obtener_longitud_palabra_minima()
4
>>> obtener_usuarios_claves()
{'nico7': '#Asd123', 'ademicheli': 'Aaaa0000#'}
>>> validar_usuario('jaime',['nico7','ademicheli'])
True
""" 

    print(doctest.testmod())
main()