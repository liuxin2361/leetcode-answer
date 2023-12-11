# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record: List[int] = [0] * 26
        for i in s:
            record[ord(i) - ord('a')] += 1
        for i in t:
            record[ord(i) - ord('a')] -= 1
        for i in range(26):
            if record[i] != 0:
                return False
        return True


if __name__ == "__main__":
    print(ord("a"))
    print(ord("A"))
    print(True)
