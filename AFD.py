class AFD:
    """Clase para automata AFD.

    """

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
        """Constructor(nombreArchivo).
            de la clase para inicializar los atributos a partir de un archivo cuyo 
            formato es el mismo acordado por todo el curso y aprobado por el docente 
            (ver archivo adjunto). Recuerde que en  los autómatas creados, todos los 
            estados deben ser accesibles. Además el autómata debe ser completo (debe 
            incluir los estados limbo).
    
        """
        self.fich = open(nombreArchivo, "r")
        allFich = self.fich.read()
        splitFich = allFich.split("#")
        self.alphabet = splitFich[1].split("\n")[1:-1]
        self.states = splitFich[2].split("\n")[1:-1]
        self.initial = splitFich[3].split("\n")[1:-1]
        self.accepting = splitFich[4].split("\n")[1:-1]
        self.transitions = splitFich[5].split("\n")[1:]



    @classmethod
    def procesarCadena(self, cadena): #boolean
        """Booleano procesarCadena(cadena):
            procesa la cadena y retorna verdadero si es aceptada y falso si es rechazada por el autómata.

        """
        print("procesarCadena: ")
        if():
            return True
        else:
            return False

    def procesarCadenaConDetalles(self, cadena): #boolean
        """Booleano procesarCadenaConDetalles(cadena):
            realiza lo mismo que el método anterior pero aparte imprime los estados que va tomando al procesar cada símbolo.

        """
        print("procesarCadenaConDetalles: ")
        pass

    def procesarListaCadena(self, listaCadenas, nombreArchivo, imprimirPantalla): #imprimirPantalla es boolean
        """procesarListaCadenas(listaCadenas,nombreArchivo, imprimirPantalla): 
            procesa cada cadenas con detalles pero los resultados deben ser impresos en un archivo cuyo nombre es nombreArchivo; si este es inválido se asigna un nombre por defecto.  Además todo esto debe ser impreso en pantalla de acuerdo al valor del Booleano imprimirPantalla. Los campos deben estar separados por tabulación y son: 
                cadena, 
                sucesión de parejas (estado, símbolo) de cada paso del procesamiento .
                sí o no dependiendo de si la cadena es aceptada o no.

        """
        print("procesarListaCadena: ")
        pass