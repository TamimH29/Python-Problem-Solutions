
class Solution(object):
    def isPalindrome(self, x):
        num = str(x)
        front = 0
        back = len(num)-1
        while(front <= back):
            if(num[front] != num[back]):
                return False
            front = front + 1
            back = back - 1
        return True

    def isPalindrome2(self,x):
        num = str(x)
        length = len(num)
        mid = len(num)//2
        half1 = num[0:mid]
        if(length % 2 == 1):
            half2 = (num[mid+1:length])[::-1]
        else:
            half2 = (num[mid:length])[::-1]
        return half2 == half1

        """
        :type x: int
        :rtype: bool
        """

a = Solution()
print(a.isPalindrome(121))
print(a.isPalindrome2(1221))

