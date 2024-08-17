

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        t = Solution.t
        to_angle = Solution.to_angle            
        
        points_at_location = 0
        angles = []
        for point in points:
            x1,y1 = t(*point, *location)
            if x1 == 0 and y1 == 0:
                points_at_location += 1
                continue
            ang = to_angle(x1,y1) 
            angles.append(ang)

            if ang >= 0 and ang < angle:
                angles.append(ang+360)
        angles = sorted(angles)
        max_s = 0
        j = 0
        for i in range(0, len(angles)):
            
            while angles[i]-angles[j] > angle:
                j += 1

            max_s = max(i-j+1, max_s)
        return max_s + points_at_location


    def t(x,y, x0,y0):
        x1 = x-x0
        y1 = y-y0
        return x1,y1
    
    def to_angle(x,y):
        angle = (math.atan2(y,x)/(math.pi))*180 
        if angle < 0:
            angle += 360
        return angle
