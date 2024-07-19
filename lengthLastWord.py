class Solution(object):
    def lengthOfLastWord(self, s):
        index = 0
        curCount = 0
        lastCount = 0
        while(index < len(s)):
            if(s[index] == " "):
                if(s[index-1] == " "):
                    pass
                else:
                    lastCount = curCount
                    curCount = 0
            else:
                curCount += 1
            index += 1
        if(s[index-1] == " "):
            return lastCount
        else:
            return curCount

    def lengthOfLastWord2(self,s):
        index = len(s)-1
        count = 0
        while(index >= 0 and s[index] == " "):
            index -= 1
        while(index >= 0 and s[index] != " "):
            count+=1
            index-=1
        return count
    
a = Solution()
result = a.lengthOfLastWord2("a")
print(result)