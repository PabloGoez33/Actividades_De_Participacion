from modelo.Repaso_7 import Elemento, Conjunto

nombre1 = Elemento("A")
nombre2 = Elemento("B")
nombre3 = Elemento("C")
nombre4 = Elemento("D")

comparar = nombre1 == nombre2
print(comparar)

conjunto = Conjunto("Conjunto AA")
print(conjunto.nombre)
print(f"Id del conjunto: {conjunto.id}")

conjunto2 = Conjunto("Conjunto BB")
print(conjunto2.nombre)
print(f"Id del conjunto: {conjunto2.id}")


print(conjunto.lista_elementos)
conjunto.agregar_elemento(nombre1)
print(conjunto.lista_elementos)
conjunto.agregar_elemento(nombre3)
print(conjunto.lista_elementos)
conjunto.agregar_elemento(nombre2)
print(conjunto.lista_elementos)

print(conjunto2.lista_elementos)
conjunto2.agregar_elemento(nombre2)
print(conjunto2.lista_elementos)
conjunto2.agregar_elemento(nombre4)
print(conjunto2.lista_elementos)
conjunto2.agregar_elemento(nombre1)
print(conjunto2.lista_elementos)
conjunto2.agregar_elemento(nombre3)
print(conjunto2.lista_elementos)

lista = conjunto + conjunto2
print(lista)

inter = Conjunto.inter(conjunto, conjunto2)
print(inter)