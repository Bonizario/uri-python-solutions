# Solução 1
countries = []
for _ in range(int(input())):
    name, *medals = input().split()
    gold, silver, bronze = map(int, medals)
    countries.append({ 'name': name, 'medals': (gold, silver, bronze) })

countries.sort(key=lambda country: (*map(lambda x: -x, country['medals']), country['name']))

for country in countries:
    print('{} {} {} {}'.format(country['name'], *country['medals']))


# Solução 2
class Country:
    def __init__(self, name, medals):
        self.name = name
        self.medals = medals

    def __lt__(self, country2):
        if self.medals == country2.medals:
            return self.name < country2.name
        return self.medals > country2.medals

    def __str__(self):
        return '{} {} {} {}'.format(self.name, *self.medals)


countries = []
for _ in range(int(input())):
    name, *medals = input().split()
    medals = list(map(int, medals))
    country = Country(name, medals)
    countries.append(country)

countries.sort()

for country in countries:
    print(country)
