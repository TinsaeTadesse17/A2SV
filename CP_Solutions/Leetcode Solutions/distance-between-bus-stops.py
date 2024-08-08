class Solution:
  def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
    cw = 0
    ccw = 0

    if start > destination:
      start, destination = destination, start

    for i, d in enumerate(distance):
      if i >= start and i < destination:
        cw += d
      else:
        ccw += d

    return min(cw, ccw)    