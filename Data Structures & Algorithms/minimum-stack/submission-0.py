class MinStack:
    def __init__(self):
        self.__data = []

    def push(self, val: int) -> None:
        mn = val
        if self.__data:
            last = self.__data[-1]
            mn = min(last[1], val)
        self.__data.append((val, mn))

    def pop(self) -> None:
        self.__data.pop()

    def top(self) -> int:
        v, _ = self.__data[-1]
        return v

    def getMin(self) -> int:
        _, mn = self.__data[-1]
        return mn
