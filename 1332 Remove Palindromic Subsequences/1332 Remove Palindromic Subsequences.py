class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s: return 0
        for i in range((len(s)+1)//2):
            if s[-i-1] != s[i]:
                return 2
        return 1