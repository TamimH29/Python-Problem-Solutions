class Solution(object):
    def romanToInt(self, s):
        symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        length = len(s)
        total = 0
        stack = []
        prev = ''
        for i in range(0, length):
            if(len(stack) == 0):
                total = total + symbols[s[i]]
            elif(symbols[prev] < symbols[s[i]]):
                total = total - symbols[prev]
                total = total + (symbols[s[i]] - symbols[prev])
            else:
                total = total + symbols[s[i]]
            prev = s[i]
            stack.append(prev)
        return total
            
a = Solution()
print(a.romanToInt("MCMXCIV"))           

