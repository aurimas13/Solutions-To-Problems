class UndergroundSystem:
    def __init__(self):
        self.checkIns = {}
        self.stationData = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id] = {"stationName": stationName, "time": t}

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkInData = self.checkIns[id]
        route = checkInData["stationName"] + "-" + stationName
        travelTime = t - checkInData["time"]

        if route not in self.stationData:
            self.stationData[route] = [0, 0]
        self.stationData[route][0] += travelTime
        self.stationData[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = startStation + "-" + endStation
        data = self.stationData[route]
        return data[0] / data[1]


if __name__ == "__main__":
    undergroundSystem = UndergroundSystem()
    undergroundSystem.checkIn(1, "A", 0)
    undergroundSystem.checkOut(1, "B", 5)
    averageTime = undergroundSystem.getAverageTime("A", "B")
    print("Average Time:", averageTime)
