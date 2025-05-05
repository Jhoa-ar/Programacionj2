from multimethod import multimethod

class LineaTeleferico:
    
    def __init__(self, color="", tramo="", nroCabinas=0, nroEmpleados=4):  # a) Inciso A: Constructor con parámetros por defecto
        self.__color = color
        self.__tramo = tramo
        self.__nroCabinas = nroCabinas
        self.__nroEmpleados = nroEmpleados
        self.__empleados = [["pedro", "rojas", "luna"],
                            ["lucy", "sosa", "rios"],
                            ["ana", "perez", "rojas"],
                            ["saul", "arce", "calle"]]
        self.__edades = [35, 43, 26, 29]
        self.__sueldos = [2500.0, 3250.0, 2700.0, 2500.0]
    
    def __str__(self):
        cad = f"Color: {self.__color}, Tramo: {self.__tramo}, nroCabinas: {self.__nroCabinas}, nroEmpleados: {self.__nroEmpleados}\n"
        cad += " Empleados: \n"
        for i in range(len(self.__empleados)):
            cad += f"Nombre: {self.__empleados[i][0]} {self.__empleados[i][1]} {self.__empleados[i][2]}, Edad: {self.__edades[i]} sueldo: {self.__sueldos[i]}\n"
        return cad

    def eliminarPorApellido(self, x):  # b) Inciso B: Eliminar por apellido (paterno o materno)
        rango = len(self.__empleados)
        i = 0
        while i < len(self.__empleados):
            if self.__empleados[i][1] == x or self.__empleados[i][2] == x:
                self.__empleados.pop(i)
                self.__edades.pop(i)
                self.__sueldos.pop(i)
                self.__nroEmpleados -= 1
            else:
                i += 1

    def __add__(self, parametros):  # c) Inciso C: Sobrecarga del operador + para transferencia de empleados
        otro, x = parametros
        if isinstance(otro, LineaTeleferico):
            for i in range(len(self.__empleados)):
                if self.__empleados[i][0] == x:
                    nombre, paterno, materno = self.__empleados[i]
                    otro.__empleados.append([nombre, paterno, materno])
                    otro.__edades.append(self.__edades[i])
                    otro.__sueldos.append(self.__sueldos[i])
                    self.__empleados.pop(i)
                    self.__edades.pop(i)
                    self.__sueldos.pop(i)
                    self.__nroEmpleados -= 1
                    otro.__nroEmpleados += 1
                    break
        return otro

    def mayorEdad(self):  # d) Inciso D.1: Obtener mayor edad
        return max(self.__edades) if self.__edades else 0

    def mayorSueldo(self):  # d) Inciso D.2: Obtener mayor sueldo
        return max(self.__sueldos) if self.__sueldos else 0

    @multimethod
    def mostrar(self, e: int):  # d) Inciso D.1: Mostrar empleados con mayor edad
        cad = "Empleados con mayor edad: \n"
        for i in range(len(self.__empleados)):
            if self.__edades[i] == e:
                cad += f"Nombre: {self.__empleados[i][0]} {self.__empleados[i][1]} {self.__empleados[i][2]}, Edad: {self.__edades[i]} sueldo: {self.__sueldos[i]}\n"
        print(cad)

    @multimethod
    def mostrar(self, s: float):  # d) Inciso D.2: Mostrar empleados con mayor sueldo
        cad = "Empleados con mayor sueldo: \n"
        for i in range(len(self.__empleados)):
            if self.__sueldos[i] == s:
                cad += f"Nombre: {self.__empleados[i][0]} {self.__empleados[i][1]} {self.__empleados[i][2]}, Edad: {self.__edades[i]} sueldo: {self.__sueldos[i]}\n"
        print(cad)

# ======================
# Parte Principal (main)
# ======================
class main():  # a) Inciso A: Instanciación de objetos con y sin parámetros
    # Primer teleférico (usando parámetros)
    t01 = LineaTeleferico("Amarillo", "Sopocachi, estacion Libertador, Estacion San Jorge", 20, 4)
    # Segundo teleférico (usando constructor por defecto)
    t02 = LineaTeleferico()

    print("primer teleferico: ")
    print(t01)

    print("segundoTeleferico: ")
    print(t02)

    print("Eliminar por apellido: (en este caso rojas)") 
    t01.eliminarPorApellido("rojas")
    t02.eliminarPorApellido("rojas")

    print(t01)
    print(t02)
    print(t01 + (t02, "saul")) 
    mayEdad = t01.mayorEdad()
    t01.mostrar(mayEdad)  
    maySueldo = t01.mayorSueldo()
    t01.mostrar(maySueldo) 
