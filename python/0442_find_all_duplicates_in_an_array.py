class Solution:
    def findDuplicates(self, nums):
        aDict = {}
        
        for num in nums:
            if num not in aDict:
                aDict[num] = 1
            else:
                aDict[num] += 1
                
        return [x for x in aDict if aDict[x]==2]


if __name__ == '__main__':
    test = Solution()
    print(test.findDuplicates([4,3,2,7,8,2,3,1]))