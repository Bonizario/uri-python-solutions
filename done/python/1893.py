# 1893 - Moon Phases
first, second = map(int, input().split())
if second <= 2:
    print('nova')
elif second <= 96:
    if first > second:
        print('minguante')
    else:
        print('crescente')
else:
    print('cheia')
