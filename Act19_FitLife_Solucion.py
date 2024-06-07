import os
import msvcrt
import csv

#Funcion para crear titulos
#def NombreFuncion(parametros):
    #Codigo función
def titulo(texto : str):
    print(f"\033[33m 🐱‍👤 {texto.upper()} 🐱‍👤\033[0m")
def error(texto : str):
    print(f"\033[31m ❌ {texto.upper()} ❌\033[0m")
def exito(texto : str):
    print(f"\033[32m ✅ {texto.upper()} ✅\033[0m")

#Tuplas - Clases
clases = [
    ("Pesas","Lun-Mie 08:30-10:00 a.m",10),
    ("Zumba","Mar-Jue 03:30-05:40 p.m",20),
    ("Nutrición","Vie 06-07:30 a.m",2),
    ("Crossfit","Sab 11:30-12:55 p.m",10)
]
#Diccionario - Usuarios
usuarios = {}
#Lista - Reservas
reservas = []
#Contador - ID usuario
numero_usuario = 100

#Comenzamos el sistema
while True:
    print("<<Press any key>>")
    msvcrt.getch()
    os.system("cls")

    print("""
     Sistema Gestión FitLife
--------------------------------
1) Registrar Usuario
2) Reservar Clase
3) Consultar Clases Disponibles
4) Consultar Clases de Usuario
5) Consultar Usuarios
0) Salir
--------------------------------""")
    opcion = input("Seleccione : ")
    if opcion=="0":
        titulo("Adios")
        break
    elif opcion=="1":
        titulo("Registrar Usuario")
        nombre = input("Ingrese nombre de Usuario : ").title()
        #Validar que el nombre no se repita
        if nombre not in usuarios.values():
            usuarios[numero_usuario] = nombre
            exito(f"Usuario {numero_usuario} Registrado")
            numero_usuario+=100
        else:
            error("Usuario ya Registrado")
    elif opcion=="2":
        titulo("Reservar Clase")
        codigo = int(input("Ingrese su ID : "))
        if codigo in usuarios:
            curso = input("Ingrese Curso para Inscribirse : ").capitalize()
            centinelacurso = False
            centinelacupos = False
            for c in clases:
                if c[0].capitalize()==curso:
                    centinelacurso = True
                    if c[2]>0: #Verificamos si hay cupos
                        centinelacupos = True
                        #Realizar Reservas
                        reservas.append([codigo, usuarios[codigo], c[0], c[1]])
                        exito("Reserva Realizada")
                        #Descontar Cupo
                        actualizacionCupo = (c[0],c[1],c[2]-1)
                        clases.remove(c)
                        clases.append(actualizacionCupo)
                        #Registrar reservas en CSV
                        with open('PY_Clase14_07-06\Reporte_Reservas.csv','w',newline='',encoding='utf-8') as a:
                            escribir = csv.writer(a, delimiter=',')
                            escribir.writerows(reservas)
                        break
                    elif centinelacupos==False:
                        error("No Quedan Cupos")
            if centinelacurso==False:
                error("No Existe el Curso")
        else:
            error("ID Invalido")
    elif opcion=="3":
        titulo("Consultar Clases Disponibles")
        for c in clases:
            print(f"{c[0]} Horario: {c[1]}\t Cupos: {c[2]}")
    elif opcion=="4":
        titulo("Consultar Clases de Usuario")
        if len(reservas)>0:
            codigo = int(input("Ingrese codigo de Usuario : "))
            centinela = False
            for r in reservas:
                if r[0]==codigo:
                    print(f"{r[0]} {r[1]} Curso:{r[2]} Horario:{r[3]}")
                    centinela = True
            if centinela==False:
                error("El ID no tiene Reservas")
        else:
            error("No Existen Reservas")
    elif opcion=="5":
        titulo("Consultar Usuarios")
        if len(usuarios)>0:
            for u in usuarios:
                print(f"{u} : {usuarios[u]}")
        else:
            error("No hay Usuarios Registrados")
    else:
        error("Opcion no valida")