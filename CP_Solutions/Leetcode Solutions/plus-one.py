class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        num =[str(l) for l in digits]
        nums = int(''.join(num))
        nums += 1
        return map(int,str(nums))



      


        