class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        beauty_upto_price = []
        maxx = float("-inf")
        for price,beauty in items:
            maxx = max(maxx,beauty)
            beauty_upto_price.append((price,maxx))
        
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        ans = [0] * len(queries)

        for q,idx in sorted_queries:
            #find the price less than or equal to the current query
            index = bisect_right(beauty_upto_price,(q,float("inf"))) - 1
            if index >= 0:
                ans[idx] = beauty_upto_price[index][1]
        
        return ans

