# 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
from typing import List


class Solution:
    def search_left(self, nums: List[int], target: int) -> int:
        """search left board"""
        start, end = 0, len(nums)  # [start, end)
        left_board: int = -1
        while start < end:
            mid: int = start + (end - start) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
                left_board = end
        return left_board

    def search_right(self, nums: List[int], target: int) -> int:
        """serach right board"""
        start, end = 0, len(nums)  # [start, end)
        right_borad: int = -1
        while start < end:
            mid: int = start + (end - start) // 2
            if nums[mid] <= target:
                start = mid + 1
                right_borad = start - 1
            else:
                end = mid
        return right_borad

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftBoard = self.search_left(nums, target)
        rightBoard = self.search_right(nums, target)
        if leftBoard == -1 or rightBoard == -1:
            return [-1, -1]
        elif leftBoard <= rightBoard:
            return [leftBoard, rightBoard]
        else:
            return [-1, -1]


if __name__ == "__main__":
    nums = [5, 6, 7, 8, 8, 10]
    target = 6
    print(Solution().searchRange(nums, target))
