class Solution(object):
    def isPalindrome(self, s):
        txt = str(s)
        newStr = ''.join(filter(str.isalnum, txt)).lower()

        if newStr.count == 0:
            return true
        else:
            st = 0
            ed = len(newStr) - 1
            isPalindrome = True
            while st < ed:
                if newStr[st] == newStr[ed]:
                    st += 1
                    ed -= 1
                else:
                    isPalindrome = False
                    break
            
            return isPalindrome
            
            
            
