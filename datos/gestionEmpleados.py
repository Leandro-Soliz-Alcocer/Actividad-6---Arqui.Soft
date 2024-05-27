#Librerias para directorios
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from negocio.observer import Observador
from negocio.factoryMethodDecorator import Empleado

#CAPA LOGICA DE NEGOCIO
class GestorEmpleados:
    def __init__(self):
        self._empleado_data = EmpleadoData()
        self._observadores = []

    def agregar_observador(self, observador: Observador):
        self._observadores.append(observador)

    def agregar_empleado(self, empleado: Empleado):
        self._empleado_data.agregar_empleado(empleado)
        self.notificar_observadores()

    def eliminar_empleado(self, empleado: Empleado):
        self._empleado_data.eliminar_empleado(empleado)
        self.notificar_observadores()

    def listar_empleados(self):
        empleados = self._empleado_data.listar_empleados()
        for empleado in empleados:
            print(f"{empleado.nombre} - Salario: {empleado.salario}")
        return empleados

    def notificar_observadores(self):
        for observador in self._observadores:
            observador.actualizar(self._empleado_data.listar_empleados())

class EmpleadoData:
    def __init__(self):
        self._empleados = []

    def agregar_empleado(self, empleado: Empleado):
        self._empleados.append(empleado)

    def eliminar_empleado(self, empleado: Empleado):
        self._empleados.remove(empleado)

    def listar_empleados(self):
        return self._empleados
