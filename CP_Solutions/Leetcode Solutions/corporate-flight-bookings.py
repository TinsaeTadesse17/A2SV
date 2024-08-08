class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        seats = [0] * (n+1)
        
        for first, last, seat in bookings:
            seats[first-1] += seat
            seats[last] -= seat


        #create prefix sum

        prefix_sum = [seats[0]]

        for i in range(1,len(seats)):
            prefix_sum.append(prefix_sum[i-1] + seats[i])

        return prefix_sum[:-1]




