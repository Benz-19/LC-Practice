class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        results = []

        for i in range(n - k + 1):
            sub = nums[i:i + k]
            is_valid = True

            for j in range(1, k):
                if sub[j] != sub[j - 1] + 1:
                    is_valid = False
                    break

            if is_valid:
                results.append(max(sub))
            else:
                results.append(-1)

        return results



nums = [1, 2, 3, 4, 3, 2, 5]
k = 3

sol = Solution()
print("Output:", sol.resultsArray(nums, k))
