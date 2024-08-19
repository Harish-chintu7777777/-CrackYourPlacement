Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class WordDictionary:
... 
...     def __init__(self):
...         self.trie = {}
...     def addWord(self, word: str) -> None:
...         node = self.trie
...         for i in word:
...             node = node.setdefault(i, {})
...         node["isWord"] = word
... 
...     def search(self, word: str) -> bool:
...         def dfs(i, root):
...             if i == len(word):
...                 if  "isWord" in root:
...                     return True
...                 return False
... 
...             if word[i] != ".":
...                 if word[i] not in root:
...                     return False
...                 return dfs(i+1, root[word[i]])
...             else:
...                 for key in root:
...                     if key != "isWord":
...                         if dfs(i+1, root[key]):
...                             return True
...                 return False
... 
...         return dfs(0, self.trie)
... 
... 
... 
... # Your WordDictionary object will be instantiated and called as such:
... # obj = WordDictionary()
... # obj.addWord(word)
