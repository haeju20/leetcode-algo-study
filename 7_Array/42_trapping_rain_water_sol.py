class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        left, right = 0, len(height) - 1 # pointer moves from both ends
        left_max, right_max = height[left], height[right]
        while left < right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
            # pointer moves to the side with higher bar
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume
