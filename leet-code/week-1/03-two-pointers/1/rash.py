class Solution:
    def isPalindrome(self, s: str) -> bool:
        convertString = ""
        for i in s:
            if i.isalpha() or i.isnumeric():
                convertString += i.upper()

        if convertString == "".join(reversed(convertString)):
            return True
        else:
            return False