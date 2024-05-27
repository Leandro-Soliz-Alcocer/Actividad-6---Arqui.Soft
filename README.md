# Actividad 6 - Arquitectura de Software
En los siguientes archivos se encuentras codigos en lenguaje Python que utilizan los principios SOLID y patrones de Diseño para un proyecto de gestion de empleados usando un ARQUITECTURA DE CAPAS.
## Capa Datos:
Contiene la clase gestionEmpleados.py. Donde se simula la gestion de datos de nuevos empleados mediante el patron Observador que actualizara la informacion y lo almacenara en una lista de empleados
## Capa Negocio:
Contiene las clases factoryMetodDecorator y observer:
factoryMethodDecorator: Encargado de la creacion de empleados nuevos con el patron FactoyMethod y extender su funcionalidad mediante el patron decorador
observer: Encargado de asignar un observador a cada empleado y actualizar la lista de empleados
## Capa Presentacion:
Contiene la clase main, que se encarga de simular el proyecto creando, eliminando y actualizando una lista de empleados

----------------------------------

## Factory Method(CREACIONAL):
Para crear empleados nuevos 
## Observer(DE COMPORTAMIENTO):
Para actualizar la informacion de los empleados
## Decorator(ESTRUCTURAL):
Para extender funcionalidades a los empleados

----------------------------

### S:
Cada clase cumple una unica funcionalidad
### O:
El codigo esta abierto para la extension y cerrado para la modificacion
### L:
Las instancias empleado pueden ser sustituidas por instancias decoradas, en este caso: **BonoExtra**
### I:
Las interfaces esta bien segregadas, en este caso: **EmpleadoFactory**, **Observador**
### D:
El codigo depende de Abstracciones y no de implementaciones concretas, por ejemplo: **EmpleadoFactory**, **Observador**
