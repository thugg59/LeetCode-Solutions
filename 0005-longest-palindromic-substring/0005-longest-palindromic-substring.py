# Expand around center approach

class Solution:
    def longestPalindrome(self, s: str) -> str:

        max_size = 1
        cur_pal = s[0]
        max_pal = s[0]
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
                        cur_pal = s[l:r + 1]

                        if len(cur_pal) > max_size:
                            max_size = len(cur_pal)
                            max_pal = s[l:r + 1]
                    else:
                        break

                    l -= 1
                    r += 1
                    
        return max_pal