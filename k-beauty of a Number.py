class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s, res = str(num), 0
        for i in range(k, len(s) + 1):
            n = int(s[i - k:i])
            if n and not num % n:
                res += 1
        return res


n = Solution()
print(n.divisorSubstrings(240, 2))