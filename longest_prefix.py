class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""
        for x in range(0, len(strs)):
            current = strs[x]
            if(x == 0):
                prefix = current
            else:
                newprefix = ""
                for y in range(0, len(prefix) if (len(prefix) < len(current)) else len(current)):
                    if(current[y] == prefix[y]):
                        newprefix += current[y]
                    else:
                        break
                prefix = newprefix
        return prefix

a = Solution()
print(a.longestCommonPrefix2(["car", "cir"]))

