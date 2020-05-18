class AFN_lambda:

    alphabet = ""
    states = ""
    initial = ""
    accepting = ""
    transitions = ""

    # constructor para inicializar atributos
    # def __init__(self, alphabet, states, initial, accepting, transitions):
    #     print("Constructor")
    #     self.alphabet = alphabet
    #     self.states = states
    #     self.initial = initial
    #     self.accepting = accepting
    #     self.transitions = transitions

    def __init__(self, nombreArchivo):
        print("Constructor con fichero para inicializar atributos")
        self.fich = open(nombreArchivo, "r")
        allFich = self.fich.read()
        splitFich = allFich.split("#")
        self.alphabet = splitFich[1].split("\n")[1:-1]
        self.states = splitFich[2].split("\n")[1:-1]
        self.initial = splitFich[3].split("\n")[1:-1]
        self.accepting = splitFich[4].split("\n")[1:-1]
        self.transitions = splitFich[5].split("\n")[1:]



    @classmethod
    def calcularLambdaClausura(self, estado):
        pass

    def calcularLambdaClausuraLista(self, conjuntoEstados):
        pass

    def procesarCadena(self, cadena): #boolean
        print("procesarCadena: ")
        if():
            return True
        else:
            return False

    def procesarCadenaConDetalles(self, cadena): #boolean
        print("procesarCadenaConDetalles: ")
        pass

    def computarTodosLosProcesamientos(self, cadena):
        pass

    def procesarListaCadena(self, listaCadenas, nombreArchivo, imprimirPantalla): #imprimirPantalla es boolean
        print("procesarListaCadena: ")
        pass

nombreArchivo = "fileAutomata.txt"

a = AFN_lambda(nombreArchivo)
# print(a.alphabet)
# print(a.states)
# print(a.initial)
# print(a.accepting)
# print(a.transitions)


# f_nuevo = open(nombreArchivo, "w") #Crear nuevo archivo