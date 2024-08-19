class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        dict = {}
        for i,word in enumerate(words):
            dict[word[::-1]] = i
        ans = []
        for i,word in enumerate(words):
            if word in dict and dict[word] != i:
                ans.append([i, dict[word]])

            if word != "" and "" in dict and word == word[::-1]:
                ans.append([dict[""],i])
                ans.append([i,dict[""]])

            for j in range(len(word)):
    
                if word[:j] in dict and word[j:] == word[:j-1:-1]:
                    ans.append([i,dict[word[:j]]])
  
                if word[j:] in dict and word[:j] == word[j-1::-1]:
                    ans.append([dict[word[j:]],i])
        return ans

                


        
