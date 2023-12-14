class UndergroundSystem:
  def __init__(self):
    self.checkIns = {}
    self.checkOuts = collections.defaultdict(lambda: [0, 0])

  def checkIn(self, id: int, stationName: str, t: int) -> None:
    self.checkIns[id] = (stationName, t)

  def checkOut(self, id: int, stationName: str, t: int) -> None:
    startStation, startTime = self.checkIns.pop(id)
    var = (startStation, stationName)
    self.checkOuts[var][0] += 1
    self.checkOuts[var][1] += t - startTime

  def getAverageTime(self, startStation: str, endStation: str) -> float:
    numTrips, totalTime = self.checkOuts[(startStation, endStation)]
    return totalTime / numTrips
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)