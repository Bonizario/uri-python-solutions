# 1131 - Grenais
another_grenal = 1
inter_victories = 0
gremio_victories = 0
draws = 0
total_of_grenais = 0
while another_grenal != 2:
    inter, gremio = map(int, input().split())
    if (inter > gremio):
        inter_victories += 1
    elif (gremio > inter):
        gremio_victories += 1
    elif (gremio == inter):
        draws += 1
    total_of_grenais += 1
    print("Novo grenal (1-sim 2-nao)")
    another_grenal = int(input())

print("{} grenais".format(total_of_grenais))
print("Inter:{}".format(inter_victories))
print("Gremio:{}".format(gremio_victories))
print("Empates:{}".format(draws))
if (inter_victories > gremio_victories):
    print("Inter venceu mais")
elif (inter_victories < gremio_victories):
    print("Gremio venceu mais")
if (inter_victories == gremio_victories):
    print("Não houve vencedor")
