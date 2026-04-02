from typing import List



def removeDuplicates(nums: List[int]) -> int:
    i = 0
    count = 1
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
            count += 1

    return count


nums = [1, 1, 2, 2, 3]

print(removeDuplicates(nums))