# Implementación de Cola Enlazada con los métodos solicitados

class Nodo:
	def __init__(self, dato):
		self.dato = dato
		self.siguiente = None

class ColaEnlazada:
	def __init__(self):
		self.Crear()

	def Crear(self):
		self.frente = None
		self.final = None

	def Vacia(self):
		return self.frente is None

	def Insertar(self, dato):
		nuevo = Nodo(dato)
		if self.Vacia():
			self.frente = self.final = nuevo
		else:
			self.final.siguiente = nuevo
			self.final = nuevo

	def Suprimir(self):
		if self.Vacia():
			print("Cola vacía")
			return None
		dato = self.frente.dato
		self.frente = self.frente.siguiente
		if self.frente is None:
			self.final = None
		return dato

	def Recorrer(self):
		actual = self.frente
		while actual:
			print(actual.dato)
			actual = actual.siguiente
