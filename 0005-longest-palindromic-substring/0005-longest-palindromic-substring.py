# Expand around center approach

class Solution:
    def longestPalindrome(self, s: str) -> str:

        max_size = 1
        cur_len = 1
        start = 0
        r = 0
        l = 0

        for i in range(len(s)):

            for j in range(2):
                if j == 0:
                    # odd
                    l = i - 1
                    r = i + 1
                else:
                    # even
                    l = i
                    r = i + 1


                while l >= 0 and r < len(s):

                    if s[l] == s[r]:
                        cur_len = r - l + 1

                        if cur_len > max_size:
                            max_size = cur_len
                            start = l
                    else:
                        break

                    l -= 1
                    r += 1

        return s[start:start + max_size]