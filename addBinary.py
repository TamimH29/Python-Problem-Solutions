class Solution(object):
    def addBinary(self, a, b):
        index = 0
        carry = False
        while(len(a)!=len(b)):
            if(len(a)<len(b)):
                a = "0"+a
            else:
                b = "0"+b
        result = ""
        while(index < len(a)):
            if(not carry):
                if(a[len(a)-1-index]=="0" and b[len(b)-1-index]=="0"):
                    result = "0" + result
                    carry = False
                elif(a[len(a)-1-index]=="1" and b[len(b)-1-index]=="1"):
                    result = "0" + result
                    carry = True
                else:
                    result = "1" + result
                    carry = False
            else:
                if(a[len(a)-1-index]=="0" and b[len(b)-1-index]=="0"):
                    result = "1" + result
                    carry = False
                elif(a[len(a)-1-index]=="1" and b[len(b)-1-index]=="1"):
                    result = "1" + result
                    carry = True
                else:
                    result = "0" + result
                    carry = True
            index += 1
        if(carry):
            result = "1"+result
            return result
        else:
            return result

a = Solution()
res = a.addBinary("1","1")
print(res)
                