class Solution:
    def reverse(self, x: int) -> int:

        sign = False

        if x < 0:
            sign = True
            x = -x

        rev = 0

        while x:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10

        if sign:
            if rev > 2147483648:
                return 0
            else:
                return -rev
        else:
            if rev > 2147483647:
                return 0
            else:
                return rev