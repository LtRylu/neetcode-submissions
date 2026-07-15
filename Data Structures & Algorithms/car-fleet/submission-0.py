class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        order = []
        for i in range(len(position)):
            order.append([position[i], speed[i]])
        order.sort(reverse = True)

        fleets = [(target - order[0][0]) / order[0][1]]

        for car in order:
            # if faster than curFleet
            time = (target - car[0]) / car[1]

            if time > fleets[-1]:
                fleets.append(time)
        
        return len(fleets)
