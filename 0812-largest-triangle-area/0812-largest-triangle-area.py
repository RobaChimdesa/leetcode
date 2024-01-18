from itertools import combinations

class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        return max(
            abs(getVector(a, b, c)) / 2
            for a, b, c in combinations(getBoundary(points), 3)
        )
def getBoundary(points):
    points = [(a, b) for a, b in points]
    points.sort(key=lambda x: (x[0], x[1]))

    upper = []
    lower = []

    for point in points:

        while len(lower) >= 2 and getVector(lower[-2], lower[-1], point) < 0:
            lower.pop()
        lower.append(point)

        while len(upper) >= 2 and getVector(upper[-2], upper[-1], point) > 0:
            upper.pop()
        upper.append(point)

    return list(set(upper + lower))

def getVector(a, b, c):
    return (b[0] - a[0]) * (b[1] - c[1]) - (b[1] - a[1]) * (b[0] - c[0])