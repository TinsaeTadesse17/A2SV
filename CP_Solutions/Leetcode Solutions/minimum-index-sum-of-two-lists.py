class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_sum = float("inf")
        ans = set()
        index_dict = {arr: i for i, arr in enumerate(list1)}

        for j, arr in enumerate(list2):
            if arr in index_dict:
                current_sum = j + index_dict[arr]
                if current_sum < index_sum:
                    ans = {arr}
                    index_sum = current_sum
                elif current_sum == index_sum:
                    ans.add(arr)

        return list(ans)