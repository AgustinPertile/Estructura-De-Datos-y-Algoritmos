class Nodo:
	def __init__(self, dato):
		self.dato = dato
		self.siguiente = None

class ListaEnlazadaPorPosicion:
	def __init__(self):
		self.cabeza = None
		self.cantidad = 0

	def InsertarPorPosicion(self, pos, dato):
		nuevo = Nodo(dato)
		if pos < 0 or pos > self.cantidad:
			print("Posición fuera de rango")
			return
		if pos == 0:
			nuevo.siguiente = self.cabeza
			self.cabeza = nuevo
		else:
			actual = self.cabeza
			for _ in range(pos - 1):
				actual = actual.siguiente
			nuevo.siguiente = actual.siguiente
			actual.siguiente = nuevo
		self.cantidad += 1

	def SuprimirPorPosicion(self, pos):
		if self.cabeza is None or pos < 0 or pos >= self.cantidad:
			print("Posición fuera de rango o lista vacía")
			return
		if pos == 0:
			self.cabeza = self.cabeza.siguiente
		else:
			actual = self.cabeza
			for _ in range(pos - 1):
				actual = actual.siguiente
			actual.siguiente = actual.siguiente.siguiente
		self.cantidad -= 1

	def BuscarPorPosicion(self, pos):
		if self.cabeza is None or pos < 0 or pos >= self.cantidad:
			print("Posición fuera de rango o lista vacía")
			return
		actual = self.cabeza
		for _ in range(pos):
			actual = actual.siguiente
		print(actual.dato)

	def Recorrer(self):
		actual = self.cabeza
		while actual is not None:
			print(actual.dato)
			actual = actual.siguiente
