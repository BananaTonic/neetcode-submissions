class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold_revenue = 0
        for i, current in enumerate(prices):
            if i == 0:
                prev_low = current # 昨日までの最安値

            revenue = current - prev_low
            # 今日の取引価格の方が保有より大きい時
            if hold_revenue < revenue:
                hold_revenue = revenue

            # 昨日までの最安値より安い
            if current < prev_low:
                prev_low = current
        return hold_revenue