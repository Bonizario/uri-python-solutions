# 2863 - Umil Bolt
while True:
    try:
        t = int(input())
        fastest = float(input())
        for _ in range(t - 1):
            time = float(input())
            if time < fastest:
                fastest = time
        print(fastest)
    except:
        break
