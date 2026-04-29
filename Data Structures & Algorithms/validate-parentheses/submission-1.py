class Solution:
    def isValid(self, s: str) -> bool:
        char ={')':'(',']':'[','}':'{'}
        stack = []
        # if len(s)%2 != 0:
        #     return False

        for a in s:#Loop over all characters
            if a in char:#Check if the character is a closing character ),},]
                if stack and stack[-1]==char[a]:#Check if the last charcter in stack is the same as the dictionary mapping of the character
                    stack.pop() #Removes the last charcter and continues
                else:
                    return False
            else:
                stack.append(a)
        return True if not stack else False

#simulatuion of [({})]
#after first loop ,stack becomes = ['[']
#after second loop, stack = ['[','(',]
#after third loop, stack -['[','(','{']
#after 4th loop , a('}') is a closing charcter do it checks whether the last character in stack is the same as what it has in the dictionary
#stack[-1] = '{' and char['}'] = '{'
#it is true so we remove the opening charcter and contine the loop
#At the end if stack has 0 elements it is true else False