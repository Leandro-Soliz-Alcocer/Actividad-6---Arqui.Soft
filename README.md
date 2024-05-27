# Actividad 6 - Arquitectura de Software
En los siguientes archivos se encuentras codigos en lenguaje Python que utilizan los principios SOLID y patrones de Diseño para un proyecto de gestion de empleados.
Los patrones usados fueron:
## Factory Method:
Para crear empleados nuevos
## Observer:
Para actualizar la informacion de los empleados
## Decorator:
Para extender funcionalidades a los empleados

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
