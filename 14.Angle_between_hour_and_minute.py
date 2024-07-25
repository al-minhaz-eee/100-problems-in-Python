# 14. Angle between hour and minute hand

class Solution:
    def getAngle(self, H, M):
        Angle1 =abs(H * 30 - M * 11/2)
        Angle2 = abs(360 - Angle1)

        if Angle1 > Angle2:
            min_angle = Angle2
            max_angle = Angle1
        elif Angle1 < Angle2:
            min_angle = Angle1
            max_angle = Angle2
        else:
            min_angle = Angle1
            max_angle = Angle1
        return int(min_angle)

find = Solution()
print(find.getAngle(9, 0))