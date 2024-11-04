class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = s.lower()
        sentence = []
        
        for t in tmp:
            if t.isalnum():
                sentence.append(t)
        
        left, right = 0, len(sentence) - 1
        
        while left <= right:
            if sentence[left] == sentence[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True