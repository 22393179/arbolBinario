class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class Arbol:
    # Funciones privadas
    def __init__(self, dato):
        self.raiz = Nodo(dato)  #se crea un nuevo nodo utilizando la clase Nodo


    def __agregar_recursivo(self, nodo, dato):  #self => instancia de la clase, nodo => el nodo actual, dato => el nuevo dato que se agregara

        if dato < nodo.dato:    #Comprueba si el nuevo dato (dato) es menor que el dato del nodo actual (nodo.dato).

            if nodo.izquierda is None:      #si el nuevo dato es menor que el dato del nodo actual y si el nodo actual no tiene un hijo izquierdo
                
                nodo.izquierda = Nodo(dato)     #Si no hay un hijo izquierdo, crea un nuevo nodo con el dato proporcionado y lo establece como el hijo izquierdo del nodo actual.

            else:
                self.__agregar_recursivo(nodo.izquierda, dato)  

        else:   #Entra en esta sección si el nuevo dato no es menor que el dato del nodo actual.
            if nodo.derecha is None:    #Verifica si el nodo actual tiene un hijo derecho (nodo.derecha). Si no tiene uno, entra en la condición.
                nodo.derecha = Nodo(dato)   #Si no hay un hijo derecho, crea un nuevo nodo con el dato proporcionado y lo establece como el hijo derecho del nodo actual.
            else:
                self.__agregar_recursivo(nodo.derecha, dato)   


    def __inorden_recursivo(self, nodo):    #Se define el método. 
        if nodo is not None:    #Se verifica si el nodo actual no es None. Si el nodo es None, no hay nada que procesar, y la recursión se detiene.

            self.__inorden_recursivo(nodo.izquierda)   
            print(nodo.dato, end=", ")  #Imprime el dato del nodo actual. 
            self.__inorden_recursivo(nodo.derecha)  #Llama recursivamente, con el hijo derecho del nodo actual como nuevo nodo.

    def __preorden_recursivo(self, nodo):   #se define el metodo
        if nodo is not None:    #Se verifica si el nodo actual no es None. Si el nodo es None, no hay nada que procesar, y la recursión se detiene.
            print(nodo.dato, end=", ")  #imprime al dato del nodo actual
            self.__preorden_recursivo(nodo.izquierda)   
            self.__preorden_recursivo(nodo.derecha) 

    def __postorden_recursivo(self, nodo):  #se define el metodo
        if nodo is not None:    #Se verifica si el nodo actual no es None. Si el nodo es None, no hay nada que procesar, y la recursión se detiene.
            self.__postorden_recursivo(nodo.izquierda)  
            self.__postorden_recursivo(nodo.derecha)    
            print(nodo.dato, end=", ")  #imprime el dato del nodo actual


    def __buscar(self, nodo, busqueda): #se define el metodo
        if nodo is None:    #Se verifica si el nodo actual es nada. Si es así, significa que se ha llegado a una hoja del árbol y el valor buscado no está presente en esa rama. En este caso, devuelve None.

            return None #Si el nodo actual es None, se devuelve None para indicar que el valor de búsqueda no se encontró en la rama actual.
        
        if nodo.dato == busqueda:   #Se verifica si el dato del nodo actual es igual al valor de búsqueda. Si es así, se ha encontrado el valor y se devuelve el nodo actual.

            return nodo #Si el dato del nodo actual es igual al valor de búsqueda, se devuelve el nodo actual para indicar que se encontró el valor en el árbol.
        
        if busqueda < nodo.dato:    #Se verifica si el valor de búsqueda es menor que el dato del nodo actual. Si es así, se debe buscar en el subárbol izquierdo.

            return self.__buscar(nodo.izquierda, busqueda)  #Llama recursivamente a __buscar con el hijo izquierdo del nodo actual como nuevo nodo. 
        
        else:   #si el valor es mayor que el dato del nodo actual 

            return self.__buscar(nodo.derecha, busqueda)    #Llama recursivamente a __buscar con el hijo derecho del nodo actual como nuevo nodo. 


    # Funciones públicas
    def agregar(self, dato):
        self.__agregar_recursivo(self.raiz, dato)

    def inorden(self):
        print("Imprimiendo árbol inorden : ")
        self.__inorden_recursivo(self.raiz)
        print("")

    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)
    

arbol_numeros = Arbol(5)
arbol_numeros.agregar(1984)
arbol_numeros.agregar(60)
arbol_numeros.agregar(10)
arbol_numeros.agregar(20)
arbol_numeros.agregar(10)
arbol_numeros.agregar(25)
arbol_numeros.agregar(59)
arbol_numeros.agregar(64)
arbol_numeros.agregar(10)
arbol_numeros.agregar(19)
arbol_numeros.agregar(23)
arbol_numeros.agregar(18)
arbol_numeros.agregar(1)
arbol_numeros.agregar(2013)
arbol_numeros.preorden()
arbol_numeros.inorden()
arbol_numeros.postorden()

busqueda = int(input("Ingresa un número para buscar en el árbol: "))
n = arbol_numeros.buscar(busqueda)
if n is None:
    print(f"{busqueda} no existe")
else:
    print(f"{busqueda} sí existe")