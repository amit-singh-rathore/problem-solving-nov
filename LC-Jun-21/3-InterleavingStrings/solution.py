class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        i, j, k = 0, 0, 0
        
        while i >= 0 and j < len(s2):
            
            if i < len(s1) and s3[k] == s1[i]:  
                i += 1
                k += 1
                
            elif s3[k] == s2[j]:                
                j += 1
                k += 1
            else:                               
                i -= 1
                j += 1
                
        return s1[i:] + s2[j:] == s3[k:] 