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


