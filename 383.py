# 383. Ransom Note
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record: list[int] = [0] * 26
        for i in magazine:
            record[ord(i) - ord('a')] += 1
        for i in ransomNote:
            record[ord(i) - ord('a')] -= 1
        for i in range(26):
            if record[i] < 0:
                return False
        return True
