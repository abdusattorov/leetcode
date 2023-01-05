class Solution:
    def longestCommonPrefix(self, strs) -> str:

        res = ""
        shortest = min(strs, key = len)

        for i in range(len(shortest)):

            temp = shortest[i]

            for j in range(len(strs)):
                if temp == strs[j][i]:
                    pass
                else:
                    return res
                    
            res += temp

        return res


if __name__ == '__main__':
    test = Solution()
    print(test.longestCommonPrefix(["flower","flow","flight"]))
    print(test.longestCommonPrefix(["dog","racecar","car"]))