# https://en.wikipedia.org/wiki/Euler%27s_totient_function#Other_formulae
# summation of k coprime numbers = 1/2 * n * phi(n)
phi = int(input())
print(sum(map(int, input().split())) * 2 // phi)
