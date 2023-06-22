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
    