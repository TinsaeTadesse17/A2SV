class Solution:
    def checkInclusion(self, s1, s2):
        count = [0] * 128
        temp = len(s1)

        for c in s1:
            count[ord(c)] += 1

        l = 0
        for r in range(len(s2)):
            char_r = ord(s2[r])
            count[char_r] -= 1

            if count[char_r] >= 0:
                temp -= 1

            while temp == 0:
                if r - l + 1 == len(s1):
                    return True

                char_l = ord(s2[l])
                count[char_l] += 1

                if count[char_l] > 0:
                    temp += 1

                l += 1

        return False