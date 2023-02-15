class Solution:
    def addToArrayForm(self, num, k):
        temp = ""
        for i in num:
            temp += str(i)
        temp = int(temp) + k
        res = list(map(int, str(temp)))
        return res


if __name__ == '__main__':
    test = Solution()
    print(test.addToArrayForm(num = [1,2,0,0], k = 34)) # [1,2,3,4]
    print(test.addToArrayForm(num = [2,7,4], k = 181)) # [4,5,5]