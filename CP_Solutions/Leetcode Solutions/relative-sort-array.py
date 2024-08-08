class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        inarr2 = []
        notinarr2 = []
        
        mydict = defaultdict(int)
        res = []
        
        for item in arr1:
            if item not in arr2:
                notinarr2.append(item)
            else:
                inarr2.append(item)

        notinarr2.sort()

        counter = Counter(inarr2)
        

        for temp in arr2:
            mydict[temp] = counter[temp]
        

        for i in mydict.keys():
            for j in range(mydict[i]):
                res.append(i)
                

        return res + notinarr2
