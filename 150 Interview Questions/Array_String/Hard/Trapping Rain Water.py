class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        ans = 0

        while left <= right:
            if height[left] <= height[right]:
                if height[left] < leftMax:
                    ans += leftMax - height[left]
                else:
                    leftMax = height[left]
                left += 1
            else:
                if height[right] < rightMax:
                    ans += rightMax - height[right]
                else:
                    rightMax = height[right]
                right -= 1

        return ans
