class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate) 
        radiant = deque()
        dire = deque()

        for i,party in enumerate(senate):
            if party == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            rad = radiant.popleft()
            di = dire.popleft()
    
            if rad < di:
                radiant.append(n)
            else:
                dire.append(n)
            n += 1

        if radiant:
            return "Radiant"
        else:
            return "Dire"
            



