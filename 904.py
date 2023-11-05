# 904. Fruit Into Baskets
# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

from collections import Counter
from typing import List, Counter


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets: Counter = Counter()  # Counter位字典的字类，统计专用，key为被统计元素，val为key的统计次数
        left: int = 0
        res: int = 0
        for right, item in enumerate(fruits):
            baskets[item] += 1
            while len(baskets) > 2:
                baskets[fruits[left]] -= 1
                if baskets[fruits[left]] == 0:
                    baskets.pop(fruits[left])
                left += 1
            res = max(res, right - left + 1)
        return res


if __name__ == "__main__":
    s = Solution()
    frutis1 = [1, 2, 1]
    frutis2 = [0, 1, 2, 2]
    frutis3 = [1, 2, 3, 2, 2]
    print(s.totalFruit(frutis1))
    print(s.totalFruit(frutis2))
    print(s.totalFruit(frutis3))
