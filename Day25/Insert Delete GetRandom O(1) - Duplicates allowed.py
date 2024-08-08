import random

class RandomizedCollection:

    def __init__(self):
        self.v = []  
        self.mymap = {}  

    def insert(self, val: int) -> bool:
        inserted_new = val not in self.mymap
        if val not in self.mymap:
            self.mymap[val] = set()
        self.mymap[val].add(len(self.v))
        self.v.append(val)
        return inserted_new

    def remove(self, val: int) -> bool:
        if val not in self.mymap or not self.mymap[val]:
            return False
        
        index_to_remove = self.mymap[val].pop()
        last_element = self.v[-1]

        self.v[index_to_remove] = last_element
        self.mymap[last_element].add(index_to_remove)
        self.mymap[last_element].remove(len(self.v) - 1)

        self.v.pop()
        if not self.mymap[val]:
            del self.mymap[val]
        
        return True

    def getRandom(self) -> int:
        if self.v:
            return random.choice(self.v)

# Example usage:
# obj = RandomizedCollection()
# param_1 = obj.insert(1)
# param_2 = obj.remove(1)
# param_3 = obj.getRandom()
