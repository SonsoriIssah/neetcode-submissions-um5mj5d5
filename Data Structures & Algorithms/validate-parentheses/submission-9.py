class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            ')':'(',
            ']' : '[',
            '}' : '{'
        }
        stack = []

        for val in s:
            if val in match:
                if stack and stack[-1]==match[val]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(val)
        return True if not stack else False




        