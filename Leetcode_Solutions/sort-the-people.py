class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        mydict = defaultdict(list)
        
        for i in range(len(heights)):
            mydict[heights[i]].append(names[i])
       
        sorted_values = sorted(mydict.items(), key=lambda x: x[0], reverse=True)

        sorted_keys = [name for names in sorted_values for name in names[1]]

        return sorted_keys