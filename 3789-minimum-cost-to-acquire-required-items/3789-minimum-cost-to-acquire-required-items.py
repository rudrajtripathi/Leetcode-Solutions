class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        def calculate(x):
            return (x * costBoth
                    + max(0, need1 - x) * cost1
                    + max(0, need2 - x) * cost2)

        return min(
            calculate(0),
            calculate(min(need1, need2)),
            calculate(max(need1, need2))
        )