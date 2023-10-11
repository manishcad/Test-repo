class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge=""
        count=0
        while word1 or word2:
            if count<len(word1):
                merge+=word1[count]
                #word1=word1.replace(word1[count],"")
                #word1=word1[count+1:]
                #del word1[count]
                word1=word1[1:]
            if count < len(word2):
                merge+=word2[count]
                #word2=word2.replace(word2[count],"")
                #del word2[count]
                #word2=word2[count+1]
                word2=word2[1:]
            
        return merge
            
s=Solution()
print(s.mergeAlternately("abc","pqrzaaax"))