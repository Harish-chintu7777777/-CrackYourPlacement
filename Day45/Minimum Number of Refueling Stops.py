
class Solution:             
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:

        fuel, heap, count = startFuel, [], 0            
        
        stations.append([target, 0])                   

        while stations:
            if fuel >= target: return count                       

            while stations and stations[0][0] <= fuel:  
                _, liters = stations.pop(0)
                heappush(heap,-liters)

            if not heap: return -1                     
            fuel-= heappop(heap)

            count+= 1
