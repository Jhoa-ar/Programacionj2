class A:
    def __init__(self, x, z):
        self.x = x
        self.z = z

    def incrementaXZ(self):
        self.x += 1
        self.z += 1

    def incrementaZ(self):
        self.z += 1

class B:
    def __init__(self, y, z):
        self.y = y
        self.z = z

    def incrementaYZ(self):
        self.y += 1
        self.z += 1

    def incrementaZ(self):
        self.z += 1

class D:
    def __init__(self, x, y, z):
        self.a = A(x, z)
        self.b = B(y, z)

    def incrementaXYZ(self):
        self.a.x += 1
        self.b.y += 1
        self.a.z += 1
        self.b.z = self.a.z  
        
    def incrementaXZ(self):
        self.a.incrementaXZ()
        self.b.z = self.a.z

    def incrementaYZ(self):
        self.b.incrementaYZ()
        self.a.z = self.b.z

    def incrementaZ(self):
        self.a.incrementaZ()
        self.b.incrementaZ()
        max_z = max(self.a.z, self.b.z)
        self.a.z = max_z
        self.b.z = max_z

    def mostrar(self):
        print(f"x: {self.a.x}, y: {self.b.y}, z: {self.a.z}")
j = D(1, 2, 3)
j.incrementaXYZ()
j.mostrar()
