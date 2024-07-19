class Solution(object):
    def mergeAlternately(self, word1, word2):
        i = 0
        counter = 0
        w1done = False
        w2done = False
        newWord = ""
        while(not (w1done and w2done)):
            if(counter%2==0):
                if(i>=len(word1)):
                    w1done = True
                else:
                    newWord += (word1[i])
                counter += 1
            else:
                if(i>=len(word2)):
                    w2done = True
                else:
                    newWord += (word2[i])
                counter += 1
                i+=1
        return newWord

a = Solution()
result = a.mergeAlternately("a","bd")
print(result)