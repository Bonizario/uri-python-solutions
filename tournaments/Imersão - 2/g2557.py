def main():
    while True:
        try:
            equation = input().strip()
            equation = equation.replace('+', '=')
            equation = equation.split('=')
        except EOFError:
            break
        if 'A' <= equation[0] <= 'Z':
            print(int(equation[2]) - int(equation[1]))
        elif 'A' <= equation[1] <= 'Z':
            print(int(equation[2]) - int(equation[0]))
        else:
            print(int(equation[0]) + int(equation[1]))
main()
