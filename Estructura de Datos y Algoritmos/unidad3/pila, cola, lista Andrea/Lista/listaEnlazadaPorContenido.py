
class Nodo:
	def __init__(self, dato):
		self.__dato = dato
		self.__siguiente = None

	def get_dato(self):
		return self.__dato

	def set_dato(self, dato):
		self.__dato = dato

	def get_siguiente(self):
		return self.__siguiente

	def set_siguiente(self, siguiente):
		self.__siguiente = siguiente


class ListaEnlazada:
	def __init__(self):
		self.__cabeza = None
		self.__cantidad = 0

	def get_cabeza(self):
		return self.__cabeza

	def set_cabeza(self, cabeza):
		self.__cabeza = cabeza

	def get_cantidad(self):
		return self.__cantidad

	def set_cantidad(self, cantidad):
		self.__cantidad = cantidad

	def InsertarPorContenido(self, dato):
		nuevo = Nodo(dato)
		if self.__cabeza is None or self.__cabeza.get_dato() >= dato:
			nuevo.set_siguiente(self.__cabeza)
			self.__cabeza = nuevo
		else:
			actual = self.__cabeza
			while actual.get_siguiente() is not None and actual.get_siguiente().get_dato() < dato:
				actual = actual.get_siguiente()
			nuevo.set_siguiente(actual.get_siguiente())
			actual.set_siguiente(nuevo)
		self.__cantidad += 1

	def SuprimirPorContenido(self, dato):
		if self.__cabeza is None:
			print("La lista está vacía")
			return
		if self.__cabeza.get_dato() == dato:
			self.__cabeza = self.__cabeza.get_siguiente()
			self.__cantidad -= 1
			return
		actual = self.__cabeza
		while actual.get_siguiente() is not None and actual.get_siguiente().get_dato() != dato:
			actual = actual.get_siguiente()
		if actual.get_siguiente() is None:
			print("No se encontró el elemento")
		else:
			actual.set_siguiente(actual.get_siguiente().get_siguiente())
			self.__cantidad -= 1

	def BuscarPorContenido(self, dato):
		actual = self.__cabeza
		pos = 1
		while actual is not None:
			if actual.get_dato() == dato:
				print(f"El dato se encuentra en la posición: {pos}")
				return True
			actual = actual.get_siguiente()
			pos += 1
		print("No se encontró el elemento")
		return False


	def BusquedaBinaria(self, dato):
		'''
		Realiza búsqueda binaria sobre la lista enlazada ordenada.
		Devuelve la posición (1-based) si lo encuentra, si no devuelve -1.
		'''
		inicio = 0
		fin = self.__cantidad - 1
		while inicio <= fin:
			medio = (inicio + fin) // 2
			actual = self.__cabeza
			idx = 0
			# Avanzar hasta el nodo en la posición 'medio'
			while idx < medio and actual is not None:
				actual = actual.get_siguiente()
				idx += 1
			if actual is None:
				break
			if actual.get_dato() == dato:
				return medio + 1  # posición 1-based
			elif actual.get_dato() < dato:
				inicio = medio + 1
			else:
				fin = medio - 1
		return -1

	def Recorrer(self):
		actual = self.__cabeza
		while actual is not None:
			print(actual.get_dato())
			actual = actual.get_siguiente()

if __name__=="__main__":
	l = ListaEnlazada()
	l.InsertarPorContenido(1)
	l.InsertarPorContenido(2)
	l.InsertarPorContenido(4)
	l.InsertarPorContenido(3)

	l.Recorrer()
	
	l.BuscarPorContenido(5)
	print("Búsqueda binaria de 3:", l.BusquedaBinaria(3))
	print("Búsqueda binaria de 5:", l.BusquedaBinaria(5))
