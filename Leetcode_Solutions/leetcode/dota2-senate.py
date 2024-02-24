class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()

        for i in range(n):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            indexR = radiant.popleft()
            indexD = dire.popleft()

            if indexR < indexD:
                radiant.append(indexR + n)
            else:
                dire.append(indexD + n)

        return "Dire" if not radiant else "Radiant"