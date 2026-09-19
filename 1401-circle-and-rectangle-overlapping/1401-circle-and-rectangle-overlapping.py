class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Closest x-coordinate on rectangle
        closestX = max(x1, min(xCenter, x2))

        # Closest y-coordinate on rectangle
        closestY = max(y1, min(yCenter, y2))

        # Distance squared between circle center and closest point
        dx = xCenter - closestX
        dy = yCenter - closestY

        return dx * dx + dy * dy <= radius * radius