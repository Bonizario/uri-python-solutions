# 1025 - Where is the Marble?
from sys import stdin, stdout

def binary_search_1st_occurence(elements, value, N):
    left, right = 0, N

    while left <= right:
        middle = (left + right) // 2

        if elements[middle] == value:
            """adaptation to find the 1st occurence"""
            while middle >= 0 and elements[middle] == value:
                middle -= 1
            middle += 1
            """end"""
            return middle

        if elements[middle] < value:
            left = middle + 1
        elif elements[middle] > value:
            right = middle - 1


case = 1
while True:
    N, Q = [int(x) for x in stdin.readline().split()]
    if N == 0 and Q == 0:
        break

    stdout.write('CASE# %d:\n' % case)
    marbles = [int(stdin.readline()) for _ in range(N)]
    marbles.sort()

    for _ in range(Q):
        query = int(stdin.readline())
        index = binary_search_1st_occurence(marbles, query, N-1)

        if index is not None:
            stdout.write('%d found at %d\n' % (query, index+1))
        else:
            stdout.write('%d not found\n' % query)

    case += 1
