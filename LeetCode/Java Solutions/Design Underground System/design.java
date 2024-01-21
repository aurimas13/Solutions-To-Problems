import java.util.HashMap;
import java.util.Map;

class UndergroundSystem {
    private Map<Integer, CheckInData> checkIns;
    private Map<String, StationData> stationData;

    public UndergroundSystem() {
        checkIns = new HashMap<>();
        stationData = new HashMap<>();
    }

    public void checkIn(int id, String stationName, int t) {
        checkIns.put(id, new CheckInData(stationName, t));
    }

    public void checkOut(int id, String stationName, int t) {
        CheckInData checkInData = checkIns.get(id);
        String route = checkInData.stationName + "-" + stationName;
        int travelTime = t - checkInData.time;

        stationData.putIfAbsent(route, new StationData());
        StationData station = stationData.get(route);
        station.totalTime += travelTime;
        station.totalTrips++;
    }

    public double getAverageTime(String startStation, String endStation) {
        String route = startStation + "-" + endStation;
        StationData station = stationData.get(route);
        return (double) station.totalTime / station.totalTrips;
    }

    private static class CheckInData {
        String stationName;
        int time;

        public CheckInData(String stationName, int time) {
            this.stationName = stationName;
            this.time = time;
        }
    }

    private static class StationData {
        int totalTime;
        int totalTrips;
    }
}
