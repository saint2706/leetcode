import random


class RandomizedSet:
    def __init__(self):
        self.vals = []
        self.indexes = {}

    def insert(self, val):
        if val in self.indexes:
            return False

        self.vals.append(val)
        self.indexes[val] = len(self.vals) - 1
        return True

    def remove(self, val):
        if val not in self.indexes:
            return False

        index = self.indexes[val]
        last_val = self.vals[-1]

        self.vals[index] = last_val
        self.indexes[last_val] = index

        self.vals.pop()
        del self.indexes[val]
        return True

    def getRandom(self):
        return random.choice(self.vals)
