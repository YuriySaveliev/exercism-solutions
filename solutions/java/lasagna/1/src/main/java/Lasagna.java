public class Lasagna {
    public int expectedMinutesInOven() {
        return 40;
    }

    public int remainingMinutesInOven(int actualMinutes) {
        return expectedMinutesInOven() - actualMinutes;
    }

    public int preparationTimeInMinutes(int layersCount) {
        int minutesPerLayer = 2;
        return layersCount * minutesPerLayer;
    }

    public int totalTimeInMinutes(int layersCount, int timeInOven) {
        return preparationTimeInMinutes(layersCount) + timeInOven;
    }
}
