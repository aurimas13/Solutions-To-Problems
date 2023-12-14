class ParkingSystem {
    private int[] slots;

    public ParkingSystem(int big, int medium, int small) {
        slots = new int[]{big, medium, small};
    }

    public boolean addCar(int carType) {
        if (slots[carType - 1] > 0) {
            slots[carType - 1]--;
            return true;
        }
        return false;
    }
}


public class Main {
    public static void main(String[] args) {
        // Create a parking system with 3 big, 3 medium, and 3 small slots
        ParkingSystem parkingSystem = new ParkingSystem(3, 3, 3);

        // Add cars of different types
        boolean car1Added = parkingSystem.addCar(1); // Big car
        boolean car2Added = parkingSystem.addCar(2); // Medium car
        boolean car3Added = parkingSystem.addCar(3); // Small car

        System.out.println("Car 1 added: " + car1Added);
        System.out.println("Car 2 added: " + car2Added);
        System.out.println("Car 3 added: " + car3Added);
    }
}
