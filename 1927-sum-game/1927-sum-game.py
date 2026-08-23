class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        sum1 = 0
        sum2 = 0
        a1 = 0
        a2 = 0
        for i in range(half):
            if num[i] == '?':
                a1 += 1
            else :
                sum1 += int(num[i])
        for i in range(half,n):
            if num[i] == '?':
                a2 += 1
            else :
                sum2 += int(num[i])
        if (a1 + a2)  % 2 == 1:
            return True
        return sum1 - sum2 != 9 * (a2 - a1) // 2
                