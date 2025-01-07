class LRUCache:
    def __init__(self, capacity: int):
        self.data = [-1 for _ in range(capacity)];
        self.book = {};
        self.maxCapacity = capacity;
        self.lastIndex = 0;

    def get(self, key: int) -> int:
        if (key not in self.book): return -1;
        return self.book[key];

    def put(self, key: int, value: int) -> None:
        self.book[key] = value;
        self.lastIndex = key;
        self.data[key % self.maxCapacity]