class Solution:
    def addToArrayForm(self, num, k):
        temp = 0
        for i in num:
            temp += i
        temp += k
        temp = str(temp)
        return list(temp)


if __name__ == '__main__':
    test = Solution()
    print(test.addToArrayForm(num = [1,2,0,0], k = 34))
    print(test.addToArrayForm(num = [2,7,4], k = 181))