class Solution(object):
    def isPalindrome(self, s):

        s2 = ''

        for i in s:
            if i.isalnum():
                s2 += i.lower()

        l, r = 0, len(s2) - 1


        while r > 0:
            if s2[l] == s2[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True


# ^^ this solution is "cheating" since it uses built-in functions
# the solution below is the neetcode solution and is optimized, in terms of memory

class Solution(object):
    def isPalindrome(self, s):

        l, r = 0, len(s) - 1

        while l < r:
            #Ensure both characters being compared are alphaNum
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            #If the characters aren't equal, after ensuring they are both lowercase return False
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True
            
        
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9'))
    


# Topics:

# Two pointer
# ASCII values

# Conceptual Answer:

# You want to create a function that filters out non alphanumeric characters at each step using the ord function. 
# Once that is made, use a two-pointer approach to compare each character from left to right (incrementing/decrementing respectively).
# If the characters aren't the same, return False it isn't a palindrome. If you reach the end, meaning the left pointer has a greater value than the right
# return True. 