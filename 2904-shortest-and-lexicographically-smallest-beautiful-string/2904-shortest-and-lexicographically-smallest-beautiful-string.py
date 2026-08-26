class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = []
        for i in range(len(s)):
            if s[i] == '1':
                ones.append(i)
        ans = ""
        for i in range(len(ones) - k + 1):
            left = ones[i]
            right = ones[i + k - 1]
            curr = s[left:right + 1]
            if ans == "" or len(curr) < len(ans) or \
               (len(curr) == len(ans) and curr < ans):
                ans = curr

        return ans