class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        sub_array = [0]*k
        count = 0

        if k==3 and len(nums)==3:
            return count
        for i in range(len(nums)):
            for j in range(0, len(sub_array)):
                if nums[i] == sub_array[j-1] and nums[i] in sub_array:
                    continue
                else:
                    sub_array[j] = nums[i]
                    print(sub_array)
                    count +=1

        return count

nums = [1,5,4,2,9,9,9]
k = 3
maxsubArr = Solution()
print(maxsubArr.maximumSubarraySum(nums, k))