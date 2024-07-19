class Solution(object):
    def removeElement(self, nums, val):
        count = 0
        for i in range (0, len(nums)):
            if(nums[i] != val):
                nums[count] = nums[i]
                count += 1
        return count


a = Solution()
numList = [0,1,2,2,3,0,4,2]
val = 2
print(a.removeElement(numList, val))