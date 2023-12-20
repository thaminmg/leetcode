class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        twosum = prices[0] + prices[1]
        if twosum <= money:
            return money - twosum
        return money
        