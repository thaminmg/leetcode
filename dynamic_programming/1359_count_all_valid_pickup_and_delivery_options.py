class Solution:
    def countOrders(self, n: int) -> int:
        slot = 2 * n
        output = 1

        while slot > 0:
            valid_choices = slot * (slot - 1) // 2
            output *= valid_choices
            slot -= 2
        return output % (10**9 + 7)
        