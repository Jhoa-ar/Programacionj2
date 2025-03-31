public class AlgebraVectorial {
    private double x, y, z;
    public AlgebraVectorial() {
        this.x = 0;
        this.y = 0;
        this.z = 0;
    }
    public AlgebraVectorial(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }
    public AlgebraVectorial(AlgebraVectorial o) {
        this.x = o.x;
        this.y = o.y;
        this.z = o.z;
    }
    public double longitud() {
        return Math.sqrt(x * x + y * y + z * z);
    }
    public double productoEscalar(AlgebraVectorial b) {
        return this.x * b.x + this.y * b.y + this.z * b.z;
    }
    public AlgebraVectorial productoVectorial(AlgebraVectorial b) {
        double i = this.y * b.z - this.z * b.y;
        double j = this.z * b.x - this.x * b.z;
        double k = this.x * b.y - this.y * b.x;
        return new AlgebraVectorial(i, j, k);
    }
    public AlgebraVectorial suma(AlgebraVectorial b) {
        return new AlgebraVectorial(this.x + b.x, this.y + b.y, this.z + b.z);
    }
    public AlgebraVectorial resta(AlgebraVectorial b) {
        return new AlgebraVectorial(this.x - b.x, this.y - b.y, this.z - b.z);
    }


    public boolean sonPerpendiculares(AlgebraVectorial b) {
        return productoEscalar(b) == 0;
    }
    public boolean sonPerpendicularesPorSumaResta(AlgebraVectorial b) {
        double sumaLongitud = suma(b).longitud();
        double restaLongitud = resta(b).longitud();
        return sumaLongitud == restaLongitud;
    }

    public boolean sonMutuamenteOrtogonales(AlgebraVectorial b) {
        double restaAB = resta(b).longitud(); 
        double restaBA = b.resta(this).longitud();
        return restaAB == restaBA;
    }
    public boolean sonPerpendicularesPorLongitudes(AlgebraVectorial b) {
        double sumaCuadrado = suma(b).longitud() * suma(b).longitud();
        double sumaLongitudesCuadrado = this.longitud() * this.longitud() + b.longitud() * b.longitud();
        return sumaCuadrado == sumaLongitudesCuadrado;
    }
    public boolean sonParalelosPorEscalar(AlgebraVectorial b) {
        double rX = this.x / b.x;
        double rY = this.y / b.y;
        double rZ = this.z / b.z;
        return rX == rY && rY == rZ;
    }
    public boolean sonParalelosPorProductoVectorial(AlgebraVectorial b) {
        return productoVectorial(b).longitud() == 0;
    }
    public AlgebraVectorial proyeccion(AlgebraVectorial b) {
        double escala = productoEscalar(b) / (b.longitud() * b.longitud());
        return new AlgebraVectorial(escala * b.x, escala * b.y, escala * b.z);
    }
    public double componente(AlgebraVectorial b) {
        return productoEscalar(b) / b.longitud();
    }
    @Override
    public String toString() {
        return "(" + x + ", " + y + ", " + z + ")";
    }
    public static void main(String[] args) {
        AlgebraVectorial a = new AlgebraVectorial(5, 8, 8);
        AlgebraVectorial b = new AlgebraVectorial(4, -3, 0);
        System.out.println("¿Son perpendiculares? " + a.sonPerpendiculares(b));
        System.out.println("¿Son perpendiculares? " + a.sonPerpendicularesPorSumaResta(b));
        System.out.println("¿Son perpendiculares? " + a.sonPerpendicularesPorLongitudes(b));
        System.out.println("¿Son mutuamente ortogonales? " + a.sonMutuamenteOrtogonales(b));
        System.out.println("¿Son paralelos? " + a.sonParalelosPorEscalar(b));
        System.out.println("¿Son paralelos? " + a.sonParalelosPorProductoVectorial(b));
        System.out.println("Proyección de a sobre b: " + a.proyeccion(b));
        System.out.println("Componente de a en b: " + a.componente(b));
    }
}
