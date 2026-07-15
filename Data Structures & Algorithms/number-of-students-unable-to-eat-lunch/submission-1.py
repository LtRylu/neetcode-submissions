

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circle = students.count(0)
        square = students.count(1)

        for i in sandwiches:
            if i == 0:
                if circle > 0:
                    circle -= 1
                else:
                    return square
            else:
                if square > 0:
                    square -= 1
                else:
                    return circle
        return 0