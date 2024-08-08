class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.remove(salary[0])
        salary.remove(salary[len(salary)-1])
        return sum(salary)/len(salary)
