# 1149 - Summing Consecutive Integers
input_list = []
result = 0
input_list = input().split()
A = int(input_list[0])
N_list = input_list[1:]

for i in N_list:
    if int(i) > 0:
        N = int(i)
        break

for j in range(0, N):
    result = result + A + j
print(result)
