# 350. Intersection of Two Arrays II
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = {}
        res = []
        for num in nums1:
            table[num] = table.get(num, 0) + 1

        for num in nums2:
            if num in table:
                if table[num] > 0:
                    res.append(num)
                    table[num] = table[num] - 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
    print(s.intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
