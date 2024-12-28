public class Triangle {
    
    public static void drawTriangle(int size) {
        for (int i = 1; i <= size; i ++) {
            System.out.println("*".repeat(i));
        }
    }

    public static void main(String[] args) {
        drawTriangle(5);
    }

}
