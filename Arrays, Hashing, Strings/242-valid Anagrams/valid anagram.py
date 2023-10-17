class Solution(object):
    def isAnagram(self, s, t):
        h_map = {} 
        for i in s:
            if i in h_map:
                h_map[i]+=1
            else:
                h_map[i]=1
        for i in t:
            if i in h_map:
                h_map[i]-=1
            else:
                return False
        for i in h_map:
            if h_map[i] != 0:
                return False
        return True
