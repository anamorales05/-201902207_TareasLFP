cadena1 = "__servidor1"
cadena2 = "3servidor"

def AFD(texto):
    estado= 0

    for i in range(len(texto)):
        if estado==0:
            if texto[0]=="_":
                estado=1
            elif texto[0]==map(chr,range(97,123)):
                estado=2
            else:
                print("Cadena no valida")
                return
        if estado==1:
            if texto[i]=="_":
                estado=1
            elif texto[i]==map(chr,range(97,123)):
                estado=3
            else:
                print("Cadena no valida")
                return
        if estado==2:
            if texto[i]==map(chr,range(97,123)):
                estado=2
            elif texto[i]==map(chr,range(48,57)):
                estado=4
            else:
                print("cadena no valida")
                return
        if estado==3:
            if texto[i]==map(chr,range(48,57)):
                estado=4
            else:
                print("cadena no valida")
                return
        if estado==4:
            print("Cadena valida")


AFD(cadena1)
AFD(cadena2)