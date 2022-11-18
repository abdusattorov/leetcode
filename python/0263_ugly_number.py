class Solution:
    # Time Limit Exceeded
    # def isUgly(self, n: int) -> bool:
    #     if n == 1:
    #         return True
    #     elif n >= 2:
    #         aSet = {2, 3, 5}
    #         primeFactors = set()

    #         # find the prime factors of n
    #         c = 2
    #         while n > 1:
    #             if n % c == 0:
    #                 primeFactors.add(c)
    #                 n /= c
    #             else:
    #                 c += 1

    #         # find if primeFactors is a subset of aSet
    #         return primeFactors <= aSet

    def isUgly(self, n: int) -> bool:
        pass


if __name__ == '__main__':
    test = Solution()
    print(test.isUgly(6))
    print(test.isUgly(1))
    print(test.isUgly(14))
    