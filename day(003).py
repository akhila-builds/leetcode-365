class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        next_node = list(range(1, len(nums) + 1))
        next_node[-1] = None
        count = 0

        while len(nums) - count > 1:
            curr = 0
            target = 0
            target_adj_sum = nums[target] + nums[next_node[target]]
…            if is_ascending:
                break
            count += 1
            next_node[target] = next_node[next_node[target]]
            nums[target] = target_adj_sum

        return count
