from abc import ABC, abstractmethod

#Patron Creacional Factory Method
class EmpleadoFactory(ABC):
    @abstractmethod
    def crear_empleado(self, nombre: str, salario: float, fecha_inicio):
        pass
    
#Producto Concreto
class Empleado:
    def __init__(self, nombre: str, salario: float, fecha_inicio):
        self.nombre = nombre
        self.salario = salario
        self.fecha_inicio = fecha_inicio
        
# Creador Concreto
class DesarrolladorFactory(EmpleadoFactory):
    def crear_empleado(self, nombre: str, salario: float, fecha_inicio):
        return Empleado(nombre, salario, fecha_inicio)

# Patron Estrucutral Decorador
class Decorador(Empleado, ABC):
    def __init__(self, empleado: Empleado):
        self._empleado = empleado

# Decorador Concreto
class BonoExtra(Decorador):
    def __init__(self, empleado: Empleado, bono: float):
        super().__init__(empleado)
        self._bono = bono

    def calcular_salario(self):
        return self._empleado.salario + self._bono

    @property
    def nombre(self):
        return self._empleado.nombre

    @property
    def salario(self):
        return self.calcular_salario()
