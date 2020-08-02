def main():
    from sys import stdin, stdout
    from itertools import permutations

    n = int(stdin.readline())
    for _ in range(n):
        string = stdin.readline().strip()
        non_distinct = permutations(string, len(string))
        # print(sorted(set(non_distinct)))  # debug
        stdout.write('\n'.join(''.join(permutation) for permutation in sorted(set(non_distinct))))
        stdout.write('\n\n')
main()
