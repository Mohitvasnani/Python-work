from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        s = self.binary(nums, target, True)
        e = self.binary(nums, target, False)
        ans = [s, e]
        return ans

    def binary(self, arr, target, isfirst):
        ans = -1
        s = 0
        e = len(arr) - 1
        while s <= e:
            m = s + (e - s) // 2
            if target < arr[m]:
                e = m - 1
            elif target > arr[m]:
                s = m + 1
            else:
                ans = m
                if isfirst:
                    e = m - 1
                else:
                    s = m + 1
        return ans

# outside the class
nums = [5, 5, 7, 7, 8, 8, 8, 8, 9, 10]
sol = Solution()                        # create object
print(sol.searchRange(nums, 8))         # call method on object