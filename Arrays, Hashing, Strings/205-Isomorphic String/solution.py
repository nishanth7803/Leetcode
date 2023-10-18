class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_1, map_2 = {}, {}
        for i, j in zip(s, t):
            if (i in map_1 and map_1[i] != j) or (j in map_2 and map_2[j] != i):
                return False
            map_1[i] = j
            map_2[j] = i
        return True
