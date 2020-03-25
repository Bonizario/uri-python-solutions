# 1291 Is This Integration?
import math

while True:
    try:
        a = input()
        if not a:
            break
        a = float(a)
        striped_region = (a**2)*(1 - 3**0.5 + math.pi/3)
        quadriculated_region = 4*(a**2)*(1 - (3**0.5)/4 - math.pi/6)
        dotted_regions = a**2 - striped_region - quadriculated_region
        print("{:.3f} {:.3f} {:.3f}".format(
            striped_region, dotted_regions, quadriculated_region))
    except EOFError:
        break
