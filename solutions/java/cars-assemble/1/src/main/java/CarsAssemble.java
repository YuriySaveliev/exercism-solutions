public class CarsAssemble {

    public double productionRatePerHour(int speed) {
        if (speed < 1) {
            return 0;
        }
        
        if (speed < 5) {
            return speed * 221 * 1;
        }

        if (speed < 9) {
            return speed * 221 * 0.9;
        }

        if (speed < 10) {
            return speed * 221 * 0.8;
        }

        return speed * 221 * 0.77;
    }

    public int workingItemsPerMinute(int speed) {
        return (int)Math.floor(productionRatePerHour(speed) / 60);
    }
}
