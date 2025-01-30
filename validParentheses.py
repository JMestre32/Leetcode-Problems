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

# Conceptual Answer:

# Create a dictionary that has keys of closed parentheses and values of their corresponding open parentheses. 
# Create a stack that will hold all open parentheses. If you encounter a closed parenthesis, see if it matches with the top of the stack. If it doesn't, return False. 
# Otherwise continue til the end of the string, if by the end the stack is not empty, it means a open parenthesis never had a matching closing parenthesis, return False. 
# If stack is empty, return True. 