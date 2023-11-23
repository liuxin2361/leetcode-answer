# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".The testcases will be generated such that the answer is unique.


from typing import Dict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        t_dict: Dict[str, int] = dict()
        for item in t:
            if item in t_dict:
                t_dict[item] += 1
            else:
                t_dict[item] = 1

        smallest: str = ""
        left: int = 0
        end: int = len(s)
        matched_count: int = 0

        for right in range(end):
            if s[right] in t_dict:
                if t_dict[s[right]] > 0:
                    matched_count += 1
                t_dict[s[right]] -= 1

            while matched_count == len(t):
                if right - left + 1 < len(smallest) or smallest == "":
                    smallest = s[left:right + 1]
                if s[left] in t_dict:
                    t_dict[s[left]] += 1
                    if t_dict[s[left]] > 0:
                        matched_count -= 1
                left += 1

        return smallest


if __name__ == "__main__":
    s = Solution()
    print(s.minWindow(s="ADOBECODEBANC", t="ABC"))
    print(s.minWindow(s="a", t="a"))
    print(s.minWindow(s="a", t="aa"))
