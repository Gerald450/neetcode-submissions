class Solution:
    def myPow(self, x: float, n: int) -> float:
        s = 1
        for i in range(abs(n)):
            s *= x
        
        return s if n > 0 else 1/s
        