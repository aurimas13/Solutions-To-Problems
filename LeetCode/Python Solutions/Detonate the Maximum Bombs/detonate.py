class Solution:
    def __init__(self):
        self.X_INDEX = 0
        self.Y_INDEX = 1
        self.R_INDEX = 2
        self.ID_INDEX = 3

    def maximumDetonation(self, bombs):
        bomb_graph = self.createBombGraph(bombs)
        return self.findLargestDetonation(bomb_graph)

    def findLargestDetonation(self, bomb_graph):
        max_detonation = 0
        visited_bombs = set()

        for bomb_id in bomb_graph.keys():
            if bomb_id in visited_bombs:
                continue
            max_detonation = max(max_detonation, self.detonateBomb(bomb_graph, set(), visited_bombs, bomb_id))

        return max_detonation

    def detonateBomb(self, bomb_graph, visited, all_visited, bomb_id):
        if bomb_id in visited:
            return 0

        all_visited.add(bomb_id)
        visited.add(bomb_id)

        detonation_count = 1
        for neighbour_bomb in bomb_graph[bomb_id]:
            neighbour_bomb_id = neighbour_bomb[self.ID_INDEX]
            detonation_count += self.detonateBomb(bomb_graph, visited, all_visited, neighbour_bomb_id)

        return detonation_count

    def createBombGraph(self, bombs):
        bomb_graph = {}

        for bomb_id, bomb in enumerate(bombs):
            bomb_graph.setdefault(bomb_id, [])

            for neighbour_bomb_id, neighbour_bomb in enumerate(bombs):
                if bomb_id == neighbour_bomb_id:
                    continue  # same bomb

                if self.isWithinRange(bomb, neighbour_bomb):
                    bomb_graph[bomb_id].append(self.createBombEntry(neighbour_bomb, neighbour_bomb_id))

        return bomb_graph

    def createBombEntry(self, bomb, id):
        return [bomb[self.X_INDEX], bomb[self.Y_INDEX], bomb[self.R_INDEX], id]

    def isWithinRange(self, bomb1, bomb2):
        distance = ((bomb2[self.X_INDEX] - bomb1[self.X_INDEX]) ** 2 + (bomb2[self.Y_INDEX] - bomb1[self.Y_INDEX]) ** 2) ** 0.5
        return distance <= bomb1[self.R_INDEX]
