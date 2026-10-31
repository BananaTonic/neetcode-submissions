class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # 最初は全部1にしておく
        left = [1] * n
        right = [1] * n
        result = [1] * n

        # 自分より左にある数字の積
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        # 自分より右にある数字の積
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        # 左の積と右の積を掛ける
        for i in range(n):
            result[i] = left[i] * right[i]

        return result