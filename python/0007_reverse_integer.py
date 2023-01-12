class Solution:
    # Link: https://leetcode.com/problems/reverse-integer/description/
    # Time spent solving: ~70 mins
    # Runtime 35 ms Beats 81.64% | Memory 13.9 MB Beats 62.90%
    def reverse(self, x: int) -> int:
        res = 0
        isNegative = False

        if x < 1:
            isNegative = True
            x = abs(x)

        while x >= 1:
            y = x / 10
            x //= 10
            remainder = y - x
            res *= 10
            res = round(res)
            res = res + remainder * 10

        if (-2**31) < res < (2**31 - 1):
            if isNegative:
                return int(round(-res))
            else:
                return int(round(res))
        else:
            return 0


if __name__ == '__main__':
    test = Solution()
    print(test.reverse(-2147483412))
    print(test.reverse(-2147483648))
    print(test.reverse(-123))
    print(test.reverse(120))