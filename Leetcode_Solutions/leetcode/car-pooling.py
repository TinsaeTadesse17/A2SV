class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        seats = [0] * 1001

        for numPassengers, From, To in trips:
            seats[From] += numPassengers
            seats[To] -= numPassengers

        #create prefix sum array
        prefix_sum = [seats[0]]

        for i in range(1,len(seats)):
            prefix_sum.append(prefix_sum[i-1] + seats[i])

        #validate prefix sum array with constraint

        for numOfPassengers in prefix_sum:
            if numOfPassengers > capacity:
                return False
        return True



