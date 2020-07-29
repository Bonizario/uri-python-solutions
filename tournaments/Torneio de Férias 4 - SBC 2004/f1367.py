def main():
    from sys import stdin, stdout
    from collections import defaultdict
    while True:
        n = int(stdin.readline())
        if not n:
            break

        problems = defaultdict(int)
        total_time = total_correct = 0
        for _ in range(n):
            problem, time, value = stdin.readline().split()

            if value == 'incorrect':
                problems[problem] += 20
            else:
                total_time += int(time) + problems[problem]
                total_correct += 1

        stdout.write('{} {}\n'.format(total_correct, total_time))

main()
