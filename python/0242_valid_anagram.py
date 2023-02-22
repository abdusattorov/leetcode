class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if sorted(t) == sorted(s) else False


if __name__ == '__main__':
    test = Solution()
    print(test.isAnagram("anagram", "nagaram"))