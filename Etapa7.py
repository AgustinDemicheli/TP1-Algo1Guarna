from tkinter import *
from tkinter import messagebox
import random

import Etapa1TP 
import Etapa8

MAXIMO_JUGADORES = 4
usuarios_ingresados = []

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

def chequear_login(usuario, contraseña):
    """"
        El objetivo de esta funcion es obtener comprobar que el usuario se este logueando correctamente
    - Nicolas Cardone
    """
    dic = obtener_usuarios_claves() #--> ES EL DICCIONARIO DE LOS USUARIOS YA REGISTRADOS. LEE EL ARCHIVO USUARIOS.CSV
    if len(usuarios_ingresados) >= MAXIMO_JUGADORES :
        messagebox.showerror("","Maximo de jugadores ingresados para jugar")
    elif usuario in dic and dic[usuario] == contraseña:
        usuarios_ingresados.append(usuario)
        messagebox.showinfo("","Usuario y Clave Correctos")
    else:
        messagebox.showerror("","Algunos de los datos ingresados es Incorrecto")

def chequear_registro(usuario, clave, clave_2,rot):
    """"
        El objetivo de esta funcion es que el usuario se este registrando correctamente segun
        las condiciones dadas
    - Nicolas Cardone
    """
    diccionario = obtener_usuarios_claves()#--> ES EL DICCIONARIO DE LOS USUARIOS YA REGISTRADOS
    usuarios = list(diccionario.keys())
    usuario_chequeado = validar_usuario(usuario,usuarios) #--> ENVIO EL USUARIO INGRESADO EN EL FORMUULARIO Y EL "USUARIOS" QUE SON LOS QUE YA ESTAN INGRESADOS
    if usuario_chequeado:
        clave_chequeado = validar_contraseña(clave,clave_2)
    if usuario_chequeado and clave_chequeado:
        arch = open("usuarios.csv", "r+", encoding="utf-8")
        arch.seek(0,2)
        arch.write("\n"+usuario + "," + clave)
        messagebox.showinfo("","Usuario registrado correctamente")
        rot.destroy()
        arch.close()

def validar_usuario(usuario, usuarios):
    """"
        El objetivo de esta funcion es comprobar que el usuario sea correcto
    - Nicolas Cardone
    """
    validez = True
    if usuario in usuarios:
        validez = False
        messagebox.showerror("","El nombre de usuario ya existe")
    elif len(usuario) < 4 or len(usuario) > 20:
        validez = False
        messagebox.showerror("","El nombre de usuario debe tener entre 4 y 20 caracteres")
    elif not usuario.isalnum():
        for caracter in usuario:
            if not caracter.isalnum() and caracter != "-":
                validez = False
                messagebox.showerror("","El nombre de usuario debe estar formado solo por letras, numeros y guion medio")
    return validez

def validar_contraseña(clave,clave_2):
    """"
        El objetivo de esta funcion es comprobar que la contraseña sea correcta
    - Nicolas Cardone
    """
    validez = True
    mayus = False
    minus = False
    num = False
    simbolo = False
    if not clave == clave_2:
        validez = False
        messagebox.showerror("","Las contraseñas deben ser iguales")
    elif len(clave) < 6 or len(clave) > 12:
        validez = False
        messagebox.showerror("","La contraseña debe tener entre 6  y 12 caracteres")
    elif "á" in clave.lower() or "é" in clave.lower() or "í" in clave.lower() or "ó" in clave.lower() or "ú" in clave.lower():
        validez = False
        messagebox.showerror("","La contraseña no puede tener letras acentuadas")
    elif not clave.isalnum():
        for c in clave:
            if c != "#" and c != "!" and not c.isalnum():
                validez = False
                messagebox.showerror("","La contraseña solo puede tener simbolos como # o !")
    for caracter in clave:
        if caracter.isupper():
            mayus = True
        elif caracter.islower():
            minus = True
        elif caracter.isnumeric():
            num = True
        elif caracter == "#" or caracter == "!":
            simbolo = True
    if not mayus or not minus or not num or not simbolo:
        validez = False
        messagebox.showerror("","La contraseña debe tener al menos una mayúscula, una minúscula, un número y uno de estos dos caracteres # o !")
    return validez

def orden(root):
    """"
        El objetivo de esta funcion es conectar la interfaz grafica con el tablero de la 
        consola
    - Nicolas Cardone
    """
    if len(usuarios_ingresados) <= 1:
        messagebox.showerror("","Debe haber al menos 2 jugador para jugar")
    else:
        random.shuffle(usuarios_ingresados)
        root.destroy()  
        print(Etapa1TP.tablero(usuarios_ingresados))
        Etapa8.obtener_lista_definiciones()
def ventana_registro():
    """"
        El objetivo de esta funcion es mostrar la ventana del registro
    - Nicolas Cardone
    """
    rot = Toplevel()
    rot.title("Registro Grupo Cracker")
    rot.config(width = 300, height = 300, bg = "skyblue")
    Label(rot, text = "Usuario: ").grid(row = 0, column = 0,padx = 15,pady= 15)
    Label(rot, text = "Clave: ").grid(row = 1, column = 0,padx = 15,pady= 15)
    Label(rot, text = "Confirmar clave: ").grid(row = 2, column = 0,padx = 15,pady= 15)
    usuario_registro = StringVar()
    clave_registro  = StringVar()
    clave_registro_2 = StringVar()
    Entry(rot, textvariable = usuario_registro).grid(row = 0 , column = 1,padx = (0,15))
    Entry(rot,show='*' , textvariable = clave_registro).grid(row = 1 , column = 1, padx = (0,15))
    Entry(rot,show='*' ,textvariable = clave_registro_2).grid(row = 2 , column = 1, padx = (0,15))
    Button(rot, text = "Registro" ,command=lambda:chequear_registro(usuario_registro.get(),clave_registro.get(),clave_registro_2.get(),rot)).grid(row = 3 , column = 1)
    rot.mainloop()

def ventana_login():
    """"
        El objetivo de esta funcion es mostrar la ventana principal del logueo
    - Nicolas Cardone
    """
    root = Tk()
    root.title("Login Grupo Cracker")
    root.config(width = 500, height = 500, bg = "skyblue")
    imagen = PhotoImage(file="pasapalabra.png")
    imagen= imagen.subsample(10)#----> realizamos subsample debido al tamaño de la imagen que descargamos
    Label(root, image= imagen).grid(row = 0, column = 3)
    Label(root, text = "Usuario: ").grid(row = 0, column = 0,padx = 15,pady= 15)
    Label(root, text = "Clave: ").grid(row = 1, column = 0,padx = 15,pady= 15)
    mi_usuario = StringVar()
    mi_clave = StringVar()
    Entry(root, textvariable = mi_usuario).grid(row = 0 , column = 1,padx = (0,15))
    Entry(root, show = "*", textvariable = mi_clave).grid(row = 1 , column = 1, padx = (0,15))

    Button(root, text = "Ingresar" ,command=lambda:chequear_login(mi_usuario.get(), mi_clave.get())).grid(row = 2 , column = 0)
    Button(root, text = "Registrarse", command=ventana_registro).grid(row = 2 , column = 1)
    Button(root, text="Iniciar Partida", command=lambda: orden(root)).grid(row=2, column=3)
    root.mainloop()
    
ventana_login()