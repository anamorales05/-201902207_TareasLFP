texto="""(
    <
    [precio] = 45.09,
    [descripcion] = "adios mundo",
    [disponible] = false
    >,
    <
    [precio] = 4,
    [descripcion] = "adios mundo",
    [disponible] = false
    >,
    <
    [precio] = -56.4,
    [descripcion] =  "este es el otro ejemplo, las cadenas pueden ser muy largas",
    [disponible] = false
    >
)"""

texto2=texto.replace("","")
text3=texto2.replace("\n","")
text4=text3.replace(" ","")
print(text4)

def AFD(cadena):
    palabra = ""
    numero=''
    estado=0
    for i in range(len(texto)):
        if estado == 0:
            if cadena[i]=="(":
                print(cadena[i]+" =Token_parentesis")
                estado=1
        if estado ==1:
            if cadena[i]=="<":
                print(cadena[i]+" =token_mayorque")
                estado=2
        if estado==2:
            if cadena[i]=="[":
                print(cadena[i]+" =token_corchete")
                estado=3
        if estado==3:
            if cadena[i].isalpha():
                palabra = palabra + cadena[i]
            elif cadena[i]=="]":
                print(palabra+" =token_palabra")
                print(cadena[i]+" =token")
                estado=4
        if estado==4:
            if cadena[i]=="=":
                print(cadena[i]+" =token_igual")
                estado=5
        if estado==5:
            if cadena[i].isalnum():
                numero=numero+cadena[i]
            elif cadena[i]==",":
                print(numero)
                print(cadena[i]+" =token_coma")
                estado=2


try:
    AFD(text4)
except:
    print(error)