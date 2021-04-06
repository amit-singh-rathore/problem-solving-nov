class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0 or x==1:
            return 1
        if x==0:
            return 0
        if x==-1:
            if n%2 == 0:
                return 1
            else:
                return -1
        
        if n<0:
            x=1/x
            n=-n
            
        ans=1
        while n>0:
            if n%2==1:
                ans=ans*x
            n=n//2
            x=x*x
        return ans