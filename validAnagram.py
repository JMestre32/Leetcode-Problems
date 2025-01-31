class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        if countS != countT:
            return False
        return True
    

#Topics:
# Hashmaps


# Conceptual Answer:
# You want to build a hashmap that holds the characters in s and t as keys and the number of times each character appears in the string as values. 
# Once you've built the hashmaps, compare them, if they're not equal return False, otherwise return True.
# You NEED to use the .get method in order for you to not get an error if they key does not exist in the hashmap yet. What it does is either increment the value if it 
# already exists, otherwise it initializes that value to 0 and adds the character as a key. 