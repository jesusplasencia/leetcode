public class Index {
    public static String printIndexed(String input) {
        int length = input.length();
        StringBuilder str = new StringBuilder();

        for (int i = 1; i <= length; i++) {
            str.append(input.charAt(i - 1) + Integer.toString(length - i));
        }

        return str.toString();
    }

    public static void main(String[] args) {
        String zelda = "ZELDA";
        String str = printIndexed(zelda);
        System.out.println(str);
    }
}
