class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            ans = ""

            for i in range(0, len(s), k):
                group = s[i:i+k]

                total = 0
                for digit in group:
                    total += int(digit)

                ans += str(total)

            s = ans

        return s
