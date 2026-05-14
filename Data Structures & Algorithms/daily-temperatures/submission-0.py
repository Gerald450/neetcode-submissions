class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        for i,a in enumerate(temperatures):
            l = i + 1
            while l < len(temperatures):
                if temperatures[l] > a:
                    res[i] = l - i
                    break
                l += 1
            
        return res