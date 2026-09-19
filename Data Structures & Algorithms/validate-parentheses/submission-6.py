class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            ')':'(',
            ']' : '[',
            '}' : '{'
        }
        char = [')',']','}']
        stack = []

        for index,val in enumerate(s):
            if stack and val in char and stack[-1]==match[val]:
                stack.pop()
            else:
                stack.append(val)
        return not bool(stack)




        