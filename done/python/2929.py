from sys import stdin, stdout
def main():
    stack = []
    for _ in range(int(stdin.readline())):
        operation = stdin.readline().rstrip()
        if ' ' in operation:
            operation, new_elem = operation.split()
        if 'PUSH' in operation:
            new_elem = int(new_elem)
            new_min = new_elem if not stack else min(new_elem, stack[-1][1])
            stack.append((new_elem, new_min))
        elif not stack:
            stdout.write('EMPTY\n')
        elif 'MIN' in operation:
            stdout.write(f'{stack[-1][1]}\n')
        else:
            stack.pop()
main()
