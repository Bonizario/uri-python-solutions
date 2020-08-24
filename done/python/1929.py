def main():
    from sys import stdin, stdout
    from itertools import combinations

    nums = tuple(map(int, stdin.readline().split()))
    triples = combinations(nums, 3)
    possible = False
    for triple in triples:
        a, b, c = triple[0], triple[1], triple[2]
        if a < b + c and b < a + c and c < a + b:
            possible = True
    stdout.write('%s\n' % ('S' if possible else 'N'))

main()
