class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i, val in enumerate(operations):
            match val:
                case "+":
                    record.append(record[-1] + record[-2])
                case "D":
                    record.append(2*record[-1])
                case "C":
                    record.pop()
                case _:
                    record.append(int(val))
        return sum(record)


        