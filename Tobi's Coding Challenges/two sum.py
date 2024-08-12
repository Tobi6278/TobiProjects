class Solution(object):
    def twoSum(self,nums,target):
        ind1 = 0
        ind2 = 0
        sum = 0
        for i in nums:
            for i in nums:
                if ind2 > len(nums) - 1:
                    ind2 = 0
                if ind1 == ind2:
                    ind2 += 1
                sum = nums[ind1] + nums[ind2]
                if sum == target:
                    return [ind1,ind2]
                else:
                    ind2 += 1
            ind2 = 0
            ind1 += 1


    
twosum = Solution()
print(twosum.twoSum([3,2,3],6))