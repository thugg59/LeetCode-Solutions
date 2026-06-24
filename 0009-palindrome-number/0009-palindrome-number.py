class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        prev = x
        rev = 0

        while x:

            digit = x % 10
            rev = rev * 10 + digit
            x //= 10
        
        return prev == rev