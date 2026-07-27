import bisect

class MedianFinder:

    def __init__(self):
        self.numbers = []
    
    def addNum(self, num: int) -> None:
        bisect.insort(self.numbers, num)

    def findMedian(self) -> float:
        n = len(self.numbers)

        if n % 2 != 0:
            return self.numbers[n//2]

        return (self.numbers[(n//2)-1] + self.numbers[(n//2)]) / 2.0
