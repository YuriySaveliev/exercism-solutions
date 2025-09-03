public class Lasagna {
    private static final int COOK_MINUTES = 40;
    private static final int LAYER_MINUTES = 2;

    public int expectedMinutesInOven() {
        return COOK_MINUTES;
    }

    public int remainingMinutesInOven(int actualMinutes) {
        return expectedMinutesInOven() - actualMinutes;
    }

    public int preparationTimeInMinutes(int layersCount) {
        return layersCount * LAYER_MINUTES;
    }

    public int totalTimeInMinutes(int layersCount, int timeInOven) {
        return preparationTimeInMinutes(layersCount) + timeInOven;
    }
}
