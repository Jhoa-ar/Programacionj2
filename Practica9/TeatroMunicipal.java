import java.util.Scanner;

// Superclase abstracta
abstract class Boleto {
    protected int numero;
    protected double precio;

    public Boleto(int numero) {
        this.numero = numero;
    }

    public abstract String getDescripcion();
}

// Subclase Palco
class Palco extends Boleto {
    public Palco(int numero) {
        super(numero);
        this.precio = 100.0;
    }

    @Override
    public String getDescripcion() {
        return "Número: " + numero + ", Precio: " + precio;
    }
}

// Subclase Platea
class Platea extends Boleto {
    public Platea(int numero, int diasAnticipacion) {
        super(numero);
        if (diasAnticipacion >= 10) {
            this.precio = 50.0;
        } else {
            this.precio = 60.0;
        }
    }

    @Override
    public String getDescripcion() {
        return "Número: " + numero + ", Precio: " + precio;
    }
}

// Subclase Galeria
class Galeria extends Boleto {
    public Galeria(int numero, int diasAnticipacion) {
        super(numero);
        if (diasAnticipacion >= 10) {
            this.precio = 25.0; // 50% de 100
        } else {
            this.precio = 30.0;
        }
    }

    @Override
    public String getDescripcion() {
        return "Número: " + numero + ", Precio: " + precio;
    }
}

// Clase principal
public class TeatroMunicipal {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean continuar = true;

        while (continuar) {
            System.out.println("\n--- Menú de Boletos ---");
            System.out.println("1. Palco");
            System.out.println("2. Platea");
            System.out.println("3. Galeria");
            System.out.println("4. Salir");
            System.out.print("Seleccione una opción: ");
            int opcion = scanner.nextInt();

            if (opcion == 4) {
                continuar = false;
                System.out.println("Programa finalizado.");
            } else {
                System.out.print("Ingrese el número del boleto: ");
                int numero = scanner.nextInt();

                Boleto boleto = null;

                switch (opcion) {
                    case 1:
                        boleto = new Palco(numero);
                        break;
                    case 2:
                        System.out.print("¿Con cuántos días de anticipación se compró?: ");
                        int diasPlatea = scanner.nextInt();
                        boleto = new Platea(numero, diasPlatea);
                        break;
                    case 3:
                        System.out.print("¿Con cuántos días de anticipación se compró?: ");
                        int diasGaleria = scanner.nextInt();
                        boleto = new Galeria(numero, diasGaleria);
                        break;
                    default:
                        System.out.println("Opción inválida.");
                }

                if (boleto != null) {
                    System.out.println(boleto.getDescripcion());
                }
            }
        }

        scanner.close();
    }
}
