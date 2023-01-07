class Solution:
    def containsDuplicate(self, nums) -> bool:
        aDict = {}
        for num in nums:
            if num in aDict:
                aDict[num] += 1
            else:
                aDict[num] = 1
        return max(aDict.values()) > 1


if __name__ == '__main__':
    test = Solution()
    print(test.containsDuplicate([1,2,3,1]))
    print(test.containsDuplicate([1,2,3,4]))
    print(test.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))