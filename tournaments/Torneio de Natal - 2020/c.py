def main():
    n = int(input())
    gnomes = sorted((input().split() for _ in range(n)), key=lambda g: (-int(g[1]), g[0]))
    teams = [[] for _ in range(n // 3)]
    i = 0
    while i != n:
        for team in teams:
            team.append(gnomes[i])
            i += 1
    for i, team in enumerate(teams):
        print(f'Time {i + 1}')
        print('\n'.join(f"{gnome[0]} {gnome[1]}" for gnome in team))
        print()
main()
