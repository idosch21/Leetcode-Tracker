class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        diff = []
        size = len(s1)
        
        for i in range(0,size):
            if s1[i] != s2[i]:
                diff.append(i)
                if len(diff)>2:
                    return False
        
        if len(diff) == 2:
            i,j = 0,1
            return s1[diff[i]] == s2[diff[j]] and s1[diff[j]] == s2[diff[i]]
        return False