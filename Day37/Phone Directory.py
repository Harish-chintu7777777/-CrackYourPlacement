class Node:
    def __init__(self):
        self.d = {}
        self.isEnd = False
        self.isPrefix = False
class Solution:
    def displayContacts(self, n, contact, s):
        # code here
        root = Node()
        contact = list(set(contact))
        contact.sort()

        curr = root
        for letter in s:
            if letter not in curr.d:
                curr.d[letter] = Node()
            curr = curr.d[letter]
            curr.isPrefix = True
        curr.isEnd = True
        curr.isPrefix = True

        ans = [[]] * len(s)

        for word in contact:
            curr = root
            count = 0
            for letter in word:
                if letter not in curr.d:
                    curr.d[letter] = Node()
                curr = curr.d[letter]
                if curr.isPrefix:
                    if ans[count]:
                        ans[count].append(word)
                    else:
                        ans[count] = [word]
                    count += 1
            curr.isEnd = True

        for l in ans:
            if not l:
                l.append(0)

        return ans
