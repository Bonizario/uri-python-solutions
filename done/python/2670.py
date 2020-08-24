# 2670 Coffee Machine
def calculateTime(A1, A2, A3, machine_position):
    # modeling equations
    time1 = abs((1 - machine_position) * 2) * A1
    time2 = abs((2 - machine_position) * 2) * A2
    time3 = abs((3 - machine_position) * 2) * A3
    return time1 + time2 + time3


A1 = int(input())
A2 = int(input())
A3 = int(input())
machine_floor1 = calculateTime(A1, A2, A3, 1)
machine_floor2 = calculateTime(A1, A2, A3, 2)
machine_floor3 = calculateTime(A1, A2, A3, 3)
print(min(machine_floor1, machine_floor2, machine_floor3))
