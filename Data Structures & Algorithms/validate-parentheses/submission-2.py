class Solution:
    def isValid(self, s: str) -> bool:
        #if open bracket: append
        #if closing bracket and stack is empty: return false
        #if closing bracket and stack: if stack[-1] matches , pop()
        s_dict = { 
            '}':'{',
            ']':'[',
            ')':'('
        }

        stack = []
        if len(s) == 1:
            return False

        for b in s:

            if b not in s_dict:
                stack.append(b)
            
            if b in s_dict and not stack:
                return False
            
            if b in s_dict and stack:
                if stack[-1] == s_dict[b]:
                    stack.pop()
                else:
                    return False
                
           
        return True if not stack else False
                                                    