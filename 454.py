# 4Sum II
# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples(i, j, k, l) such that:
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_map1 = dict()
        count = 0
        for i in nums1:
            for j in nums2:
                sum_map1[i + j] = sum_map1.get(i + j, 0) + 1

        for i in nums3:
            for j in nums4:
                count += sum_map1.get(-i - j, 0)

        return count


if __name__ == "__main__":
    solution = Solution()
    # nums1 = [1, 2]
    # nums2 = [-2, -1]
    # nums3 = [-1, 2]
    # nums4 = [0, 2]
    nums1 = [0]
    nums2 = [0]
    nums3 = [0]
    nums4 = [0]
    print(solution.fourSumCount(nums1, nums2, nums3, nums4))
