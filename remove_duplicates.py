class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        if(len(nums) == 0):
            return 0
        else:
            count = 1
            current = nums[0]
            while(i < len(nums)):
                if(nums[i] != current):
                    nums[count] = nums[i]
                    current = nums[i]
                    count += 1
                i += 1
            return count

a = Solution()
list1 = [1, 1, 1, 2, 2, 3, 4, 4, 4]
print(a.removeDuplicates(list1))
