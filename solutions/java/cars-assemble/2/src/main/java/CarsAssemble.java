public class CarsAssemble {

    public double productionRatePerHour(int speed) {
        double successRate = 0;
        
        if (speed == 0) {
            return 0;
        }

        int carsPerSpeed = 221;
        
        if (speed < 5) {
            successRate = 1;
        } else if (speed < 9) {
            successRate = 0.9;
        } else if (speed == 9) {
            successRate = 0.8;
        } else if (speed == 10) {
            successRate = 0.77;
        }

        return speed * carsPerSpeed * successRate;
    }

    public int workingItemsPerMinute(int speed) {
        return (int)Math.floor(productionRatePerHour(speed) / 60);
    }
}