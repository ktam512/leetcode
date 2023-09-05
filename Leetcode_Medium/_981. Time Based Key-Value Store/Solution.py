class T:
    def __init__(self, value, timestamp):
        self.value = value
        self.timestamp = timestamp

class TimeMap:
    def __init__(self):
        self.map = {}

    def set(self, key, value, timestamp):
        if key not in self.map:
            self.map[key] = []
        self.map[key].append(T(value, timestamp))

    def get(self, key, timestamp):
        if key not in self.map:
            return ""

        A = self.map[key]
        l = 0
        r = len(A)

        while l < r:
            m = (l + r) // 2
            if A[m].timestamp > timestamp:
                r = m
            else:
                l = m + 1

        return "" if l == 0 else A[l - 1].value