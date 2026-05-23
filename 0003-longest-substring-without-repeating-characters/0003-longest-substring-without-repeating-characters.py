class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = {}
        curr = 0
        rec = 0
        l = 0

        for r in range(len(s)):
            
            if s[r] in seen:
                l = seen[s[r]] + 1 if seen[s[r]] >= l else l 
            
            seen[s[r]] = r
            curr = r - l + 1
            rec = curr if curr > rec else rec

        return rec