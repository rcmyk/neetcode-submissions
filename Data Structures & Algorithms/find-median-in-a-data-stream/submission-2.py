import bisect

class MedianFinder:

    def __init__(self):
        self.numbers = []
    
    def addNum(self, num: int) -> None:
        self.numbers.append(num)

    def findMedian(self) -> float:
        self.numbers.sort()
        n = len(self.numbers)

        if n % 2 != 0:
            return self.numbers[n//2]

        return (self.numbers[(n//2)-1] + self.numbers[(n//2)]) / 2.0
