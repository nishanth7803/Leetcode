class Solution(object):
    def topKFrequent(self, nums, k):
        h_map = {}
        ans = []
        for i in nums:
            if i in h_map:
                h_map[i]+=1
            else:
                h_map[i]=1
        for i in range(k):
            max_key = max(h_map, key = lambda x: h_map[x])
            ans.append(max_key)
            del h_map[max_key]
        return ans
