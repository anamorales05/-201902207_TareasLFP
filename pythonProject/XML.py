from xml.dom import minidom
def tarea():
    usuario = minidom.parse("tareaPrueba.xml")
    registro = usuario.getElementsByTagName("estudiante")

    for A in registro:
        nom = A.getElementsByTagName("nombre")[0]
        ape = A.getElementsByTagName("apellido")[0]
        edadd = A.getElementsByTagName("edad")[0]
        prom = A.getElementsByTagName("promedio")[0]

        print(f" Nombre:", nom.firstChild.data, f" Apellido:", ape.firstChild.data, f" Edad:", edadd.firstChild.data, f" Promedio:", prom.firstChild.data)
