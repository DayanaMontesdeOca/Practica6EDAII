class Vertice:
    def __init__(self, n):
        self.nombre = n
        self.vecinos = list()
        
    def agregarVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)
            self.vecinos.sort()

class Grafo:
    def __init__(self):
        # Se inicializa como atributo de instancia para poder crear múltiples grafos
        self.vertices = {}

    def agregarVertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            return True
        else:
            return False

    def agregarArista(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.agregarVecino(v)
                if key == v:
                    value.agregarVecino(u)
            return True
        else:
            return False

    def imprimeGrafo(self):
        for key in sorted(list(self.vertices.keys())):
            print("Vertice " + key + " Sus vecinos son " + str(self.vertices[key].vecinos))


# Clase controladora
class Controladora:
    def main(self):
        print("--- Grafo Original del Documento ---")
        # Se crea un objeto 'g' de la clase Grafo
        g = Grafo()
        # Se crea un objeto 'a' de la clase Vertice
        a = Vertice('A')
        # se agrega el vertice a al grafo
        g.agregarVertice(a)
        
        # Esta estructura de repetición es para agregar
        # todos los vertices, y no hacerlo uno a uno
        for i in range(ord('A'), ord('K')):
            g.agregarVertice(Vertice(chr(i)))
            
        # Se declara una lista que contiene las aristas del grafo
        edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ']
        
        # Se agregan las aristas al grafo
        for edge in edges:
            g.agregarArista(edge[:1], edge[1:])
            
        # Se imprime el grafo, como lista de adyacencia
        g.imprimeGrafo()

        # ---------------------------------------------------------
        # Pruebas con tres grafos no dirigidos propuestos
        # ---------------------------------------------------------
        
        print("\n--- Grafo Propuesto 1: Triángulo ---")
        g1 = Grafo()
        for v in ['A', 'B', 'C']:
            g1.agregarVertice(Vertice(v))
        for edge in ['AB', 'BC', 'CA']:
            g1.agregarArista(edge[0], edge[1])
        g1.imprimeGrafo()

        print("\n--- Grafo Propuesto 2: Cuadrado con diagonal ---")
        g2 = Grafo()
        for v in ['A', 'B', 'C', 'D']:
            g2.agregarVertice(Vertice(v))
        for edge in ['AB', 'BC', 'CD', 'DA', 'AC']:
            g2.agregarArista(edge[0], edge[1])
        g2.imprimeGrafo()

        print("\n--- Grafo Propuesto 3: Estrella de 4 puntas ---")
        g3 = Grafo()
        for v in ['Centro', 'P1', 'P2', 'P3', 'P4']:
            g3.agregarVertice(Vertice(v))
        # En este caso, al usar nombres de más de un carácter, pasamos los nombres completos
        aristas_estrella = [('Centro', 'P1'), ('Centro', 'P2'), ('Centro', 'P3'), ('Centro', 'P4')]
        for u, v in aristas_estrella:
            g3.agregarArista(u, v)
        g3.imprimeGrafo()

obj = Controladora()
obj.main()
