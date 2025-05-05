from multimethod import multimethod

class LineaTeleferico:
    def __init__(self, color="", tramo="", nroCabinas=0, nroEmpleados=0):
        self.color = color
        self.tramo = tramo
        self.nroCabinas = nroCabinas
        self.nroEmpleados = nroEmpleados
        self.empleados = [] 
        self.edades = []
        self.sueldos = []

    def agregarEmpleado(self, nombre, paterno, materno, edad, sueldo):
        self.empleados.append([nombre, paterno, materno])
        self.edades.append(edad)
        self.sueldos.append(sueldo)
        self.nroEmpleados += 1

    def __str__(self):
        info = f"Color: {self.color}, Tramo: {self.tramo}, Cabinas: {self.nroCabinas}, Empleados: {self.nroEmpleados}\n"
        for i in range(len(self.empleados)):
            e = self.empleados[i]
            info += f"  {e[0]} {e[1]} {e[2]}, Edad: {self.edades[i]}, Sueldo: {self.sueldos[i]}\n"
        return info

    def eliminarPorApellido(self, apellido):
        i = 0
        while i < len(self.empleados):
            if self.empleados[i][1] == apellido or self.empleados[i][2] == apellido:
                self.empleados.pop(i)
                self.edades.pop(i)
                self.sueldos.pop(i)
                self.nroEmpleados -= 1
            else:
                i += 1

    def __add__(self, other_info):
        destino, nombre = other_info
        for i in range(len(self.empleados)):
            if self.empleados[i][0] == nombre:
                destino.agregarEmpleado(*self.empleados[i], self.edades[i], self.sueldos[i])
                self.empleados.pop(i)
                self.edades.pop(i)
                self.sueldos.pop(i)
                self.nroEmpleados -= 1
                break
        return destino

    def mayorEdad(self):
        if self.edades:
            return max(self.edades)
        else:
            return 0

    def mayorSueldo(self):
        if self.sueldos:
            return max(self.sueldos)
        else:
            return 0.0

    @multimethod
    def mostrar(self, edad: int):
        print("Empleados con mayor edad:")
        for i in range(len(self.empleados)):
            if self.edades[i] == edad:
                e = self.empleados[i]
                print(f"  {e[0]} {e[1]} {e[2]}, Edad: {self.edades[i]}, Sueldo: {self.sueldos[i]}")

    @multimethod
    def mostrar(self, sueldo: float):
        print("Empleados con mayor sueldo:")
        for i in range(len(self.empleados)):
            if self.sueldos[i] == sueldo:
                e = self.empleados[i]
                print(f"  {e[0]} {e[1]} {e[2]}, Edad: {self.edades[i]}, Sueldo: {self.sueldos[i]}")


t1 = LineaTeleferico("Rojo", "Estación Central - 16 de Julio", 20)
t2 = LineaTeleferico("Azul", "Estación Buenos Aires - UPEA", 25)


t1.agregarEmpleado("Pedro", "Rojas", "Luna", 35, 2500)
t1.agregarEmpleado("Lucy", "Sosa", "Rios", 43, 3250)
t1.agregarEmpleado("Ana", "Perez", "Rojas", 26, 2700)
t1.agregarEmpleado("Saul", "Arce", "Calle", 29, 2500)

print("Teleférico 1")
print(t1)
print("Teleférico 2")
print(t2)

print("Eliminando por apellido Rojas")
t1.eliminarPorApellido("Rojas")
print(t1)

print("Transferencia de Saul")
t1 + (t2, "Saul")
print("Teleférico 1 después de transferencia:")
print(t1)
print("Teleférico 2 después de transferencia:")
print(t2)

print("Empleado con mayor edad")
t2.mostrar(t2.mayorEdad())

print("Empleado con mayor sueldo")
t2.mostrar(t2.mayorSueldo())
