class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res =[0] * len(temperatures)
        stack =[] #pair[index, value]

        for i in range(len(temperatures)):

            while stack and stack[-1][1] < temperatures[i]:
                index, tempe = stack.pop()
                res[index] = i - index
            stack.append((i, temperatures[i]))
        return res
