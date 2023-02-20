class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        temp = ""
        for i in range(len(s)):
            if s[i].lower() in alpha:
                temp += s[i]
        return temp.lower() == temp[::-1].lower()