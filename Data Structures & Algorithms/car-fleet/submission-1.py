class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #make a pair of spee and position
        #sort the pair and iterate in reverse order
        #use formula target - position / speed to find time
        #if its less, pop
        pair = [[p,s] for p,s in zip(position, speed)]
        stack = []

        for p,s in sorted(pair)[::-1]:
            time = (target - p)/s
            stack.append(time)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)