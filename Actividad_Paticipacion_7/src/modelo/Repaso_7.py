from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str = ''

    def __eq__(self, nom1: object) -> bool:
        return self.nombre == nom1.nombre
    
    def __str__(self) -> str:
        return self.nombre
        
class Conjunto:

    Contador = 0
    
    def __init__(self, nombre) -> None:
        self.lista_elementos: list = []
        self.nombre: str = nombre
        Conjunto.Contador += 1
        self.__id: int = Conjunto.Contador
    
    @property
    def id(self):
        return self.__id
    
    def contiene(self, obj) -> bool:
        return any(obj == e for e in self.lista_elementos)
    
    def agregar_elemento(self, obj: Elemento):
        if not self.contiene(obj):
            self.lista_elementos.append(obj)

    def __add__(self, other):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNIDO {other.nombre}")
        for elem in self.lista_elementos:
            nuevo_conjunto.agregar_elemento(elem)
        for elem2 in other.lista_elementos:
            nuevo_conjunto.agregar_elemento(elem2)
        return nuevo_conjunto
    
    @classmethod
    def inter(cls, conju, conju2):
        nue_conju = Conjunto(f"{conju.nombre} INTERSECTADO {conju2.nombre}")
        for elem in conju.lista_elementos:
            for elem2 in conju2.lista_elementos:
                if elem == elem2:
                    nue_conju.agregar_elemento(elem2)
        return nue_conju
    
    def __str__(self):
        elementos_str = ', '.join(elem.nombre for elem in self.lista_elementos)
        return f"{self.nombre}: ({elementos_str})"