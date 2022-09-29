from estudiantes import estudiantes
from io import open
listado=[]
#Crear contactos
def nuevoestudiante(nombre,grado, promedio):
    listado.append(estudiantes(nombre,grado,promedio))

#Eliminar estudiantes
def eliminarestudiantes(nombre):
    posicion= None
    for i in range(len(listado)):
        if nombre==listado[i].vernombre():
            posicion=i
            break
    if posicion==None:
        return 'El estudiante no existe en el sistema-----------------------------\n'
    else:
        listado.pop(posicion)
        return 'Estudiante eliminado con éxito del sistema---------------------------- \n'

#crear reporte en html
def crearreporte():
    reporte=open("reporte.html","w")
    reporte.write('!doctype html \n')
    reporte.write("<html> \n")
    reporte.write("<head>\n")
    reporte.write("\t<title>REPORTE DE ESTUDIANTES REGISTRADOS EN EL SISTEMA</title>\n")
    reporte.write("</head> \n")
    reporte.write("<body>")
    reporte.write("")
    reporte.write("</body>")
    reporte.write("</html> \n")
    reporte.close()

def menu():
    print("1. Registrar nuevo estudiante \n",
    "2. Eliminar estudiante \n")