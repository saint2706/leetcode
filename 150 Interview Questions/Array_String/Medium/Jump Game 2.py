class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        jumps = 1
        curr_max_reach = nums[0]
        next_max_reach = nums[0]

        for i in range(1, n):
            if curr_max_reach < i:
                jumps += 1
                curr_max_reach = next_max_reach

            next_max_reach = max(next_max_reach, i + nums[i])

        return jumps
