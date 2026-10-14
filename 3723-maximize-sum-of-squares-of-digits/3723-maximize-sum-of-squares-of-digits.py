class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        
        ans = ""
        
        for i in range(num):
            digit = min(9, sum)
            
            if i == 0 and digit == 0:
                return ""
            
            ans += str(digit)
            sum -= digit
        
        if sum > 0:
            return ""
        
        return ans
