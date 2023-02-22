class Solution:
    # Solution 1 | Sorting | Runtime: 60.58% & Memory: 10.73%
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return True if sorted(t) == sorted(s) else False

    # Solution 2 | Count | Runtime: 88.24% & Memory: 61.66%
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
                return False

        for ch in set(s):
            if s.count(ch) != t.count(ch):
                return False
        return True 


if __name__ == '__main__':
    test = Solution()
    print(test.isAnagram("anagram", "nagaram"))
    print(test.isAnagram("rat", "car"))