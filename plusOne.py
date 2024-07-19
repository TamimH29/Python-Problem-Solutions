class Solution(object):
    def plusOne(self, digits):
        places = len(digits)
        i = len(digits)-1
        carry = True
        while(carry):
            digits[i] += 1
            if(digits[i] >= 10):
                if(i == 0):
                    digits[i] %= 10
                    digits.insert(0,1)
                    carry = False
                else:
                    digits[i] %= 10
                    i -= 1
            else:
                carry = False
        return digits
    
a = Solution()
result = a.plusOne([4,3,9,9])
print(result)
            