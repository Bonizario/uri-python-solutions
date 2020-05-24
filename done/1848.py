# 1848 - Counting Crow
blinks = 0
screams = 0
while screams < 3:
    sample = input()
    if sample == 'caw caw':
        print(blinks)
        screams += 1
        blinks = 0
        continue
    if sample[2] == '*':
        blinks += 1
    if sample[1] == '*':
        blinks += 2
    if sample[0] == '*': # --- are ignored
        blinks += 4
