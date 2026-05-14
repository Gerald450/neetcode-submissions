class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for s in tokens:

            if s == '+':
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif s == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif s == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            elif s == '*':
                res = stack.pop() * stack.pop()
                stack.append(res)
            else:
                stack.append(int(s))

        return stack[0]

        