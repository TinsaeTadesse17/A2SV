class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        mydict = defaultdict(list)
        count = 0
       
        for i in range(len(strs[0])):

            for j in range(0,len(strs)):

                mydict[i].append(strs[j][i])
                
        for k in mydict.values():

            unsortedd= k
            sortedd = sorted(k)


            if unsortedd != sortedd:
                count += 1

        return count