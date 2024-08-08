class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        from collections import defaultdict
        ans = []
        mydict = defaultdict(list)

        for i in range(len(paths)):

            parts = paths[i].split()
            directory = parts[0]
            
            for filee in parts[1:]:
                f_start = filee.index('(')
                f_name = filee[:f_start]
                mydict[filee[f_start+1:-1]].append(directory + '/' + f_name)

        for k in mydict.values():
            if len(k) > 1:
                ans.append(k)

        return ans
