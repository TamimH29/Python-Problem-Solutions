class Solution(object):
    def gcdOfStrings(self, str1, str2):
        strDiv = []
        i = min(len(str1),len(str2))
        while(i>0):
            if(len(str1)%i==0 and len(str2)%i==0):
                strDiv.append(i)
            i -= 1
        for j in range(0,len(strDiv)):
            if(str1[0:strDiv[j]] == str2[0:strDiv[j]]):
                repeat = 2
                current = strDiv[j]
                found = True
                if(len(str1)>len(str2)):
                    bigger = str1
                    smaller = str2
                else:
                    bigger = str2
                    smaller = str1
                while(strDiv[j]*repeat <= len(bigger)):
                    if(strDiv[j]*repeat > len(smaller)):
                        if(bigger[0:strDiv[j]] != bigger[current:repeat*strDiv[j]]):
                            found = False
                            break    
                    else:
                        if(bigger[0:strDiv[j]] != bigger[current:repeat*strDiv[j]] or smaller[0:strDiv[j]] != smaller[current:repeat*strDiv[j]]):
                            found = False
                            break
                    current = repeat*strDiv[j]
                    repeat += 1
                if(found):
                    return str1[0:strDiv[j]]
        return ""

a = Solution()
result = a.gcdOfStrings("AAAAAAAAA", "AAACCC")
print(result)