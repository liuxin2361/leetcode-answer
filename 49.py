# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

from collections import defaultdict
from typing import DefaultDict, List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict: DefaultDict = defaultdict(list)
        for str in strs:
            new_str = ''.join(sorted(str))
            res_dict[new_str].append(str)
        return list(res_dict.values())


if __name__ == "__main__":
    s = Solution()
    test_data1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(s.groupAnagrams(test_data1))

    test_data2 = [""]
    print(s.groupAnagrams(test_data2))

    test_data3 = ["a"]
    print(s.groupAnagrams(test_data3))
