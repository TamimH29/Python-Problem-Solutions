class Solution(object):
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums)-1
        while(low <= high):
            mid = (low+high)//2
            if(nums[mid] == target):
                return mid
            elif(nums[mid] < target):
                low = mid + 1
            else:
                high = mid - 1
        return high+1

a =  Solution()
numList = [1,60,70,100]
tar = 110
print(a.searchInsert(numList, tar))