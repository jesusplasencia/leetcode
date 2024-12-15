public class Operation {

    public static int add(int operandOne, int operandTwo) {
        return operandOne + operandTwo;
    }

    public static int mul(int operandOne, int operandTwo) {
        return operandOne * operandTwo;
    }

    public static void main(String[] args) {
        int res = mul(add(4, mul(4, 6)), add(3, 5));
        System.out.println(res);
    }

}
