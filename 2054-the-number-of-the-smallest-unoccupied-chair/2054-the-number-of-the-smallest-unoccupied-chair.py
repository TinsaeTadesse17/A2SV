class Solution:
  def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
    events = []
    for i, (arrival_time, leave_time) in enumerate(times):
      events.append((arrival_time, 1, i)) 
      events.append((leave_time, -1, i)) 

    target_arrival_time = times[targetFriend][0]
    chair_hashmap = defaultdict() 
    free = [] 
    next_chair = 0 

    for time, event_type, friend_id in sorted(events):
      if event_type == 1:
        # Person arriving
        if free:
          chair = heappop(free)
          chair_hashmap[friend_id] = chair
        else:
          chair_hashmap[friend_id] = next_chair
          next_chair += 1
        if time == target_arrival_time:
          return chair_hashmap[friend_id]
      else:
        # Person leaving
        heappush(free, chair_hashmap[friend_id])

    return -1
