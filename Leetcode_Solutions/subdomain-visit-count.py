class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = []
        mydict = defaultdict(int)

        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)

            subdomains = domain.split('.')
            for i in range(len(subdomains)):
                mydict['.'.join(subdomains[i:])] += count

        for key, value in mydict.items():
            ans.append(f"{value} {key}")

        return ans