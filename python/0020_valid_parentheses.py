class Solution:
    # wrong answer
    # def isValid(self, s: str) -> bool:
    #     brackets = {
    #         'p': 0,
    #         'c': 0,
    #         's': 0
    #     }
    #     for i in range(len(s)):
    #         if s[i] == '(':
    #             brackets['p'] = 1
    #         elif s[i] == ')':
    #             brackets['p'] = 0
    # 
    #         if s[i] == '{':
    #             brackets['c'] = 1
    #         elif s[i] == '}':
    #             brackets['c'] = 0
    # 
    #         if s[i] == '[':
    #             brackets['s'] = 1
    #         elif s[i] == ']':
    #             brackets['s'] = 0
    # 
    #     return 1 not in brackets.values()

    # neetcode
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen [c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

if __name__ == '__main__':
    test = Solution()
    print(test.isValid("()[]{}"))
    print(test.isValid("(]"))
    print(test.isValid("([)]"))