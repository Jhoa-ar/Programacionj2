public class FigurasGeometricas {
    public double area(float r) {
        return Math.PI * r * r;
    }

    public double area(float b, float h) {
        return (b * h);
    }

    public double area(int b, int h) {
        return (b * h) / 2;
    }

    public double area(int B, double b, double h) {
        return ((B + b) * h) / 2;
    }

    public double area(int L, double a) {
        double P = 5 * L;
        return (P * a) / 2;
    }

    public static void main(String[] args) {
        FigurasGeometricas figuras = new FigurasGeometricas();

        System.out.println("Área del círculo: " + figuras.area(5.0f));
        System.out.println("Área del rectángulo: " + figuras.area(10.0f, 4.0f));
        System.out.println("Área del triángulo: " + figuras.area(8, 6));
        System.out.println("Área del trapecio: " + figuras.area(10, 6.0, 5.0));
        System.out.println("Área del pentágono: " + figuras.area(7, 4.0));
    }

}