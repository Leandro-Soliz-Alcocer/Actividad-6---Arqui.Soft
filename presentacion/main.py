#Librerias de Directorios
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datos.gestionEmpleados import GestorEmpleados
from negocio.observer import Observador
from negocio.factoryMethodDecorator import DesarrolladorFactory, BonoExtra
import time
#CAPA DE PRESENTACION (EJEMPLO)
if __name__ == "__main__":
    gestor = GestorEmpleados() 

    observador = Observador()
    gestor.agregar_observador(observador)

    factory = DesarrolladorFactory()

    fecha_actual = time.time()

    empleado1 = factory.crear_empleado("Juan", 2000, fecha_actual)
    empleado2 = factory.crear_empleado("Maria", 2500, fecha_actual)
    gestor.agregar_empleado(empleado1)
    gestor.agregar_empleado(empleado2)

    empleado3 = factory.crear_empleado("Pedro", 1800, fecha_actual)
    empleado3_con_bono1 = BonoExtra(empleado3, 500)

    gestor.agregar_empleado(empleado3_con_bono1)
    gestor.eliminar_empleado(empleado1)

    gestor.eliminar_empleado(empleado2)

    empleado2 = BonoExtra(empleado2, 200)
    gestor.agregar_empleado(empleado2)
