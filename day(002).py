class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        Ans = [-1] * N

        for i in range(N):
            if nums[i] == 2:
                continue

            n = nums[i]
…
            Ans[i] = n

        return Ans
                       
