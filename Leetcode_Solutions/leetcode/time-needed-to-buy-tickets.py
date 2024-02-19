class Solution:
    def timeRequiredToBuy(self, tickets, k):
        cnt = 0
        while True:
            for i in range(len(tickets)):
                if tickets[i] == 0:
                    continue
                tickets[i] -= 1
                cnt += 1
                if tickets[k] == 0:
                    return cnt
