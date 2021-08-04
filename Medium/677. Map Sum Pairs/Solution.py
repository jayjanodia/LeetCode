# Brute Force Solution

#Runtime: 28 ms, faster than 88.81% of Python3 online submissions for Map Sum Pairs.
#Memory Usage: 14.4 MB, less than 56.87% of Python3 online submissions for Map Sum Pairs.
class MapSum:
    def __init__(self):
        self.map = {}

    def insert(self, key, val):
        self.map[key] = val

    def sum(self, prefix):
        for key, val in self.map.items():
            count = 0
            if key.startswith(prefix):
                count += val
        return count

# Second solution Remaining
# Trie solution Remaining