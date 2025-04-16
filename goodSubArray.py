from collections import defaultdict

class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        count = defaultdict(int)
        total_pairs = 0
        left = 0
        result = 0

        for right in range(len(nums)):
            total_pairs += count[nums[right]]
            count[nums[right]] += 1

            while total_pairs >= k:
                result += len(nums) - right
                count[nums[left]] -= 1
                total_pairs -= count[nums[left]]
                left += 1

        return result

# Large input test
nums = [3,1,4,3,2,2,4]
k = 2

print(Solution().countGood(nums, k))
