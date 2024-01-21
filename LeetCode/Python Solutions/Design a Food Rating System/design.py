from typing import List
from collections import defaultdict
import heapq

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_info = {food: [cuisine, rating] for food, cuisine, rating in zip(foods, cuisines, ratings)}
        self.cuisine_max_heap = defaultdict(list)
        for food, (cuisine, rating) in self.food_info.items():
            heapq.heappush(self.cuisine_max_heap[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, oldRating = self.food_info[food]
        self.food_info[food][1] = newRating
        heapq.heappush(self.cuisine_max_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while self.cuisine_max_heap[cuisine]:
            rating, food = self.cuisine_max_heap[cuisine][0]
            if self.food_info[food][1] == -rating:
                return food
            heapq.heappop(self.cuisine_max_heap[cuisine])
