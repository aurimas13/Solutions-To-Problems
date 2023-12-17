import java.util.*;

public class FoodRatings {
    private Map<String, String> foodToCuisine;
    private Map<String, Integer> foodToRating;
    private Map<String, TreeMap<Integer, Set<String>>> cuisineToFood;

    public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
        foodToCuisine = new HashMap<>();
        foodToRating = new HashMap<>();
        cuisineToFood = new HashMap<>();

        for (int i = 0; i < foods.length; i++) {
            foodToCuisine.put(foods[i], cuisines[i]);
            foodToRating.put(foods[i], ratings[i]);
            cuisineToFood.putIfAbsent(cuisines[i], new TreeMap<>(Collections.reverseOrder()));
            cuisineToFood.get(cuisines[i]).putIfAbsent(ratings[i], new TreeSet<>());
            cuisineToFood.get(cuisines[i]).get(ratings[i]).add(foods[i]);
        }
    }

    public void changeRating(String food, int newRating) {
        String cuisine = foodToCuisine.get(food);
        int oldRating = foodToRating.get(food);
        foodToRating.put(food, newRating);

        cuisineToFood.get(cuisine).get(oldRating).remove(food);
        if (cuisineToFood.get(cuisine).get(oldRating).isEmpty()) {
            cuisineToFood.get(cuisine).remove(oldRating);
        }

        cuisineToFood.putIfAbsent(cuisine, new TreeMap<>(Collections.reverseOrder()));
        cuisineToFood.get(cuisine).putIfAbsent(newRating, new TreeSet<>());
        cuisineToFood.get(cuisine).get(newRating).add(food);
    }

    public String highestRated(String cuisine) {
        Set<String> foods = cuisineToFood.get(cuisine).firstEntry().getValue();
        return foods.iterator().next();
    }
}
