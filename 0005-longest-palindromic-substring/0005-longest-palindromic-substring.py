class Solution:
    def longestPalindrome(self, s: str) -> str:

        chars = {}
        max_len = 1

        for i in range(len(s)):
            if s[i] not in chars:
                chars[s[i]] = [i]
            else:
                chars[s[i]].append(i)

                for j in range(len(chars[s[i]]) - 1):

                    if len(s[chars[s[i]][j]:i + 1]) > max_len and s[chars[s[i]][j]:i + 1] == s[chars[s[i]][j]:i + 1][::-1]:
                        max_pal = s[chars[s[i]][j]:i + 1]
                        max_len = len(max_pal)

        if max_len == 1:
            return s[0] 
        else:           
            return max_pal     

s = "babbab"

chars = {
    "b" : [0, 2, 3, 5],
    "a" : [1, 4]
}