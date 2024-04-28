class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split() #first removing spaces and than splitting string into words
        
        if not words:
            return 0
        
        return len(words[-1])