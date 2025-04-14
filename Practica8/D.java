public class D implements IA, IB {
    private A a;
    private B b;

    public D(int x, int y, int z) {
        a = new A(x, y);
        b = new B(y, z);
    }

    public void incrementaXYZ() {
        a.x++;
        b.y++;
        a.z++;
        b.z = a.z;
    }

    public void incrementaXZ() {
        a.incrementaXZ();
        b.z = a.z;
    }

    public void incrementaYZ() {
        b.incrementaYZ();
        a.z = b.z;
    }

    public void incrementaZ() {
        a.incrementaZ();
        b.incrementaZ();

        int maxZ = Math.max(a.z, b.z);
        a.z = maxZ;
        b.z = maxZ;
    }

    public void mostrar() {
        System.out.println("x: " + a.x + ", y: " + b.y + ", z: " + a.z);
    }

}
