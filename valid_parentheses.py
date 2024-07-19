class Solution(object):
    def isValid(self, s):
        stack = []
        for x in range(0, len(s)):
            stack.append(s[x])
            if(len(stack) == 1):
                pass
            elif((s[x]) == ')'):
                if(ord(stack[-1]) - 1 == ord(stack[-2])):
                    stack.pop()
                    stack.pop()
            else:
                if(ord(stack[-1]) - 2 == ord(stack[-2])):
                    stack.pop()
                    stack.pop()
        return len(stack) == 0

    def isValid2(self, s):
        stack = []
        openp = 0
        closep = 0
        for x in range(0, len(s)):
            if(s[x] == '(' or s[x] == '[' or s[x] == '{'):
                stack.append(s[x])
                openp += 1
            else:
                closep += 1
                if(s[x] == ')' and len(stack) > 0):
                    if(ord(s[x]) - 1 == ord(stack[-1])):
                        stack.pop()
                elif((s[x] == ']' or s[x] == '}') and len(stack) > 0):
                    if(ord(s[x]) - 2 == ord(stack[-1])):
                        stack.pop()
                else:
                    pass
        return (len(stack) == 0 and (closep == openp))
            

a = Solution()
print(a.isValid2("]"))

