#Patron de comportamiento Observador
class Observador:
    def actualizar(self, empleados):
        print("Lista de empleados actualizada:")
        for empleado in empleados:
            print(f"{empleado.nombre} - Salario: {empleado.salario}")
