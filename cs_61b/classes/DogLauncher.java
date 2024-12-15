// Test driver Class
public class DogLauncher {

    public static Dog[] largerThanFourNeighbors (Dog[] dogs) {
        Dog[] returnDogs = new Dog[dogs.length];
        int cnt = 0;

        for (int i = 0; i < dogs.length; ++i) {
            if (isBiggestOfFour(dogs, i)) {
                returnDogs[cnt] = dogs[i];
                cnt++;
            }
        }
        return returnDogs;
    }

    public static boolean isBiggestOfFour(Dog[] dogs, int i) {
        boolean isBiggest = true;
        for ( int j = -2; j <= 2; j++ ) {
            int currIdx = i + j;
            if (j == 0) continue;
            if (validIndex(dogs, currIdx)) {
                if (dogs[ currIdx ].weightInPounds >= dogs[ i ].weightInPounds) {
                    isBiggest = false;
                }
            }
        }
        return isBiggest;
    }

    public static boolean validIndex(Dog[] dogs, int idx) {
        if (idx < 0) return false;
        if (idx >= dogs.length) return false;
        return true;
    }

    public static void main(String[] args) {

        Dog[] dogs = new Dog[]{
                new Dog(10),
                new Dog(15),
                new Dog(20),
                new Dog(15),
                new Dog(10),
                new Dog(5),
                new Dog(10),
                new Dog(15),
                new Dog(22),
                new Dog(15),
                new Dog(10)
        };

        Dog[] bigDogs = largerThanFourNeighbors(dogs);
    
        for ( int k = 0; k < bigDogs.length; k++ ) {
            if (bigDogs[k] == null) continue;
            System.out.print( bigDogs[k].weightInPounds + " " );
        }

    }

}