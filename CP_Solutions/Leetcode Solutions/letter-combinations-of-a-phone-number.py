class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mydict = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        if len(digits) == 0:
                return []
        ans = []
        def backtrack(path,nxt_digits):
            if len(nxt_digits) == 0:
                ans.append(path)

            else:
                for i in mydict[nxt_digits[0]]:
                    backtrack(path + i,nxt_digits[1:])

        backtrack("",digits)
        return ans

        