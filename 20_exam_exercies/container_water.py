class Solution:
    def max_area(heights: list[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            max_area = max(max_area, width * height)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area


area = Solution
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(area.max_area(heights))