from multimethod import multimethod

class Ministerio:
    def __init__(self, nombre="", direccion="", nroEmpleados=4):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__nroEmpleados = nroEmpleados
        self.__empleados = [
            ["Pedro", "Rojas", "Luna"],
            ["Lucy", "Sosa", "Rios"],
            ["Ana", "Perez", "Rojas"],
            ["Saul", "Arce", "Calle"]
        ]
        self.__edades = [35, 43, 26, 29]
        self.__sueldos = [2500.0, 3250.0, 2700.0, 2500.0]
        
    def __str__(self):
        cad = f"Nombre: {self.__nombre}, Dirección: {self.__direccion}, NroEmpleados: {self.__nroEmpleados}\n"
        cad += " Empleados:\n"
        for i in range(len(self.__empleados)):
            cad += f"Nombre: {self.__empleados[i][0]} {self.__empleados[i][1]} {self.__empleados[i][2]}, Edad: {self.__edades[i]}, Sueldo: {self.__sueldos[i]}\n"
        return cad
    
    def eliminarPorEdad(self, x):
        nuevos_empleados = []
        nuevas_edades = []
        nuevos_sueldos = []
        for i in range(len(self.__empleados)):
            if self.__edades[i] != x:
                nuevos_empleados.append(self.__empleados[i])
                nuevas_edades.append(self.__edades[i])
                nuevos_sueldos.append(self.__sueldos[i])
        self.__empleados = nuevos_empleados
        self.__edades = nuevas_edades
        self.__sueldos = nuevos_sueldos
        self.__nroEmpleados = len(nuevos_empleados)
        
    def __add__(self, parametros):
        otro, nombreX = parametros
        for i in range(len(self.__empleados)):
            if self.__empleados[i][0] == nombreX:
                otro.__empleados.append(self.__empleados[i])
                otro.__edades.append(self.__edades[i])
                otro.__sueldos.append(self.__sueldos[i])
                otro.__nroEmpleados += 1

                for j in range(i, self.__nroEmpleados - 1):
                    self.__empleados[j] = self.__empleados[j + 1]
                    self.__edades[j] = self.__edades[j + 1]
                    self.__sueldos[j] = self.__sueldos[j + 1]
                self.__empleados.pop()
                self.__edades.pop()
                self.__sueldos.pop()
                self.__nroEmpleados -= 1
                break
        return otro
    
    def menorEdad(self):
        if self.__edades:
            menor = self.__edades[0]
            for edad in self.__edades:
                if edad < menor:
                    menor = edad
            return menor
        return 0

    def menorSueldo(self):
        if self.__sueldos:
            menor = self.__sueldos[0]
            for sueldo in self.__sueldos:
                if sueldo < menor:
                    menor = sueldo
            return menor
        return 0

    @multimethod
    def mostrar(self, e: int):
        cad = "Empleados con menor edad:\n"
        for i in range(len(self.__empleados)):
            if self.__edades[i] == e:
                cad += f"Nombre: {self.__empleados[i][0]} {self.__empleados[i][1]} {self.__empleados[i][2]}, Edad: {self.__edades[i]}, Sueldo: {self.__sueldos[i]}\n"
        print(cad)

    @multimethod
    def mostrar(self, s: float):
        cad = "Empleados con menor sueldo:\n"
        for i in range(len(self.__empleados)):
            if self.__sueldos[i] == s:
                cad += f"Nombre: {self.__empleados[i][0]} {self.__empleados[i][1]} {self.__empleados[i][2]}, Edad: {self.__edades[i]}, Sueldo: {self.__sueldos[i]}\n"
        print(cad)
class main():
    m1 = Ministerio("Ministerio de Salud", "La Paz - Zona Central")
    m2 = Ministerio()

    print("Primer Ministerio:")
    print(m1)

    print("Segundo Ministerio:")
    print(m2)

    print("Eliminar empleados con edad 43:")
    m1.eliminarPorEdad(43)
    m2.eliminarPorEdad(43)

    print("Después de eliminar:")
    print(m1)
    print(m2)

    print("Transferencia:")
    m1 = m1 + (m2, "Saul")

    print("Primer Ministerio actualizado:")
    print(m1)

    print("Segundo Ministerio actualizado:")
    print(m2)

    print("Mostrar empleados con menor edad:")
    edadMin = m1.menorEdad()
    m1.mostrar(edadMin)

    print("Mostrar empleados con menor sueldo:")
    sueldoMin = m1.menorSueldo()
    m1.mostrar(sueldoMin)
