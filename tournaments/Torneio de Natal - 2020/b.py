def main():
    e = {'bonecos': 0, 'arquitetos': 0, 'musicos': 0, 'desenhistas': 0}
    for _ in range(int(input())):
        _, group, hours = input().split()
        e[group] += int(hours)
    print(e['bonecos']//8 + e['arquitetos']//4 + e['musicos']//6 + e['desenhistas']//12)
main()
