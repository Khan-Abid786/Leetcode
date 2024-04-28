import re
class Solution(object):
    def isPalindrome(self, s):
        s = re.sub(r"[^a-zA-Z0-9]", "", s)
        s = s.lower()
        reversed_string = s[::-1]
        if s == reversed_string: 
            return True 
        else: 
            return False
