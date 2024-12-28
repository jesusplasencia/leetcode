public class Dog {

    public int weightInPounds;
    public static String binomem = "Canis familiaris";

    public Dog (int initWeight) {
        weightInPounds = initWeight;
    }

    public Dog() {
        this(0);
    }

    public void makeNoise() {
        if (weightInPounds < 10) {
            System.out.println("Yip!");
        } else if (weightInPounds < 50) {
            System.out.println("Bark!");
        } else {
            System.out.println("Wooof!");
        }
    }

    public static Dog maxDog(Dog d1, Dog d2) {
        if (d1 == null) return d2;
        if (d2 == null) return d1;
        if (d1.weightInPounds > d2.weightInPounds) return d1;
        return d2;
    }
    
}
