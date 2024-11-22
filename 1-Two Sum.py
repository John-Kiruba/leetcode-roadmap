class Solution:
    def twoSum(self, nums, target):
        hm = {}
        l = len(nums)
        for i in range(l):
            if nums[i] not in hm:
                hm[nums[i]] = i

        for i in range(l):
            complement = target - nums[i]
            if complement in hm and hm[complement] != i:
                return [hm[nums[i]], hm[complement]]

        return []

s = Solution()
print(s. twoSum(nums=[2,7,11,15], target=9))

