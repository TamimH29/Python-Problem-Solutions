class Solution(object):
    def strStr(self, haystack, needle):
        i = 0
        index = -1
        while(i<len(haystack)):
            if(haystack[i] == needle[0]):
                j = i
                needlePos = 0
                mat = True
                while(needlePos < len(needle)):
                    if(j >= len(haystack)):
                        mat = False
                        break
                    if(haystack[j] != needle[needlePos]):
                        mat = False
                        break
                    else:
                        j += 1
                        needlePos += 1
                if(mat):
                    return i
            i+=1
        return index

a = Solution()
haystack = "mississippi"
needle = "issipi"
print(a.strStr(haystack, needle))