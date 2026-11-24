class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        
        individual = [(target - p) / s for p, s in pair]
        last = 0
        fleet = 0

        for time in individual:
            if time > last:
                last = time
                fleet += 1

        return fleet
