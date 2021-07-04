# Iterative Solution
class Solution:
    def grayCode(self, n: int) -> List[int]:
        temp=[""]
        for i in range(1,n+1):
            res=[]
            for bits in temp:
                res.append("0"+bits)
            for bits in reversed(temp):
                res.append("1"+bits)
            
            temp=res    

        return [int(bits,2) for bits in res]
  
# Recursive Solution  
class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        def helper(n):
            if n==1:
                return ['0','1']
            
            temp = helper(n-1)
            
            ret=[]
            
            for bits in temp:
                ret.append("0"+bits)
            
            for bits in reversed(temp):
                ret.append("1"+bits)
                
            return ret
        
        res = helper(n)
        
        return [int(bits, 2) for bits in res]