# 438. Find All Anagrams in a String
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len: int = len(s)
        p_len: int = len(p)
        sorted_p = "".join(sorted(p))
        res: List[int] = []
        for i in range(s_len - p_len + 1):
            new_s = "".join(sorted(s[i:i + p_len]))
            if new_s == sorted_p:
                res.append(i)
        return res

    def findAnagrams1(self, s: str, p: str) -> List[int]:
        p_counter = Counter(p)
        s_len: int = len(s)
        p_len: int = len(p)
        res: List[int] = []
        for i in range(s_len - p_len + 1):
            s_counter = Counter(s[i:i + p_len])
            if s_counter == p_counter:
                res.append(i)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))
    print(s.findAnagrams("abab", "ab"))

    print(s.findAnagrams1("cbaebabacd", "abc"))
    print(s.findAnagrams1("abab", "ab"))
