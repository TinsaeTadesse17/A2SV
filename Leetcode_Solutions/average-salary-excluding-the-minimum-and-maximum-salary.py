class Solution:
    def average(self, salary: List[int]) -> float:
        sum = 0
        count = 0
        avg = 0
        maxsalary = float("-inf")
        minsalary = float("inf")
        for i in salary:
            maxsalary = max(maxsalary, i)
            minsalary = min(minsalary, i)

        for j in salary:
            if j == maxsalary or j == minsalary:
                continue
            sum += j
            count += 1
        avg = sum / count
        return avg
        




        