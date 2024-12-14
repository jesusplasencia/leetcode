public class Stutter {
    
    public static String stutter(String input) {
        StringBuilder str = new StringBuilder();
        for (int i = 0; i < input.length(); i++) {
            str.append(String.valueOf(input.charAt(i)).repeat(2));
        }
        return str.toString();
    }

    public static void main(String[] args) {
        String in = "Hello!";
        String res = stutter(in);
        System.out.println(res);
    }

}
