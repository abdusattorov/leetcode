class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            'p': 0,
            'c': 0,
            's': 0
        }
        for i in range(len(s)):
            if s[i] == '(':
                brackets['p'] = 1
            elif s[i] == ')':
                brackets['p'] = 0

            if s[i] == '{':
                brackets['c'] = 1
            elif s[i] == '}':
                brackets['c'] = 0

            if s[i] == '[':
                brackets['s'] = 1
            elif s[i] == ']':
                brackets['s'] = 0

        return 1 not in brackets.values()