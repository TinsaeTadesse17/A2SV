class Solution:
  def isLongPressedName(self, name: str, typed: str) -> bool:

    i = 0

    for j, k in enumerate(typed):

      if i < len(name) and name[i] == k:
        i += 1

      elif j == 0 or k != typed[j - 1]:
        return False

    return i == len(name)