class Solution:
    def isValid(self, s: str) -> bool:
        validDict = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        parenStack = []

        for char in s:
            if char in validDict and parenStack:
                if parenStack[len(parenStack)-1] == validDict[char]:
                    parenStack.pop()
                else:
                    return False
            else:
                parenStack.append(char)
        if parenStack:
            return False
        else: 
            return True
        

# Topics/Data Structures:

# 1. Stack
# 2. Dictionary

# Pitfalls

# 1. The dictionary keys are a bit unconventional, but this is to check for validity of close parenthesis
# 2. Line 12 be sure to check if the parenStack has at least one character "and parenStack" otherwise you fail the case when s = ']'
# 3. Line 15 be sure to pop the top of the stack otherwise you aren't comparing the correct characters and will often return False when it's not