def main():
    b = int(input())
    g = int(input())
    balls = round(g / 2) - b
    print('Amelia tem todas bolinhas!' if balls <= 0 else f'Faltam {balls} bolinha(s)')
main()
