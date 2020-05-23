# todos los estados deben ser accesibles
# automata completo con estados limbo
# documentacion
# para lambda usar simbolo $
#archivo de especificacion de formato revisar
# import AFD
# import string
# prueba
import AFD
import ProcesamientoCadenaAFD
a = AFD.AFD("fileAFD.txt")

# b = ProcesamientoCadenaAFD.ProcesamientoCadenaAFD()

def lectura(tipo):
    print("|------------------------------------------|")
    print("|                Automatas                 |")
    print("|------------------------------------------|")
    print("| 1) Escribir Automata por consola         |")
    print("| 2) Cargar Automata por archivo           |")
    print("|------------------------------------------|")
    Numopc1 = int(input())
    if Numopc1 == 1:
        print("Ecribiendo "+ tipo)
        Escribir(tipo) ##llamar la funcion para empezar a escribir el automata
    if Numopc1 == 2:
        print("cargando "+ tipo)
        Cargar(tipo) #llamar la funcion para empezar a cargar el automata
ini = 1
while ini == 1:
    print("|------------------------------------------|")
    print("|                Automatas                 |")
    print("|------------------------------------------|")
    print("|  Con que tipo automata quiere trabajar   |")
    print("| 1) AFD                                   |")
    print("| 2) AFN                                   |")
    print("| 3) AFN-landa                             |")
    print("| 4) Salir                                 |")
    print("|------------------------------------------|")
    Numopc = int(input())
    if Numopc == 1:
        print("AFD")
        lectura("AFD")
    if Numopc == 2:
        print("AFN")
        lectura("AFN")
    if Numopc == 3:
        print("AFN-Landa")
        lectura("AFN-Landa")
    if Numopc == 4:
        print("salir")
        ini = 2
    else:
        print("escoge una opccion valida")







