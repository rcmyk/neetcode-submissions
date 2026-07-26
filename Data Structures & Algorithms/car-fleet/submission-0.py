class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data = []
        for i in range(len(position)):
            data.append((position[i], speed[i]))
        data.sort()

        fleet = 0
        while data:
            y, v = data.pop()
            tb = (target - y) / v
            while data:
                x, u = data[-1]
                ta = (target - x) / u
                if ta <= tb:
                    data.pop()
                else: break
            fleet += 1
        return fleet



