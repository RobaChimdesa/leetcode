class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result = ""
        store = {}
        for char in s:
            store[char] = store.get(char, 0) + 1
        for char in order:
            if char in store:
                result += char * store[char]
                del store[char]
        for char, count in store.items():
            result += char * count
        return result