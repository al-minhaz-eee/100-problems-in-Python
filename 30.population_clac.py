"""
 30.The current population of a town is 10000. The population of the town is
 increasing at the rate of 10% per year. You have to write a program to
 find out the population at the end of each of the last 10 years. For eg
 current population is 10000 so the output should be like this:
 10th year- 10000
 9th year- 9000
 8th year- 8100 and so on
"""
def calculate_past_population(current_population = 10000, growth_rate = 10, years = 10):
    populations = []
    for year in range(years, 0, -1):
        populations.append([year, int(current_population)])
        current_population *= (1- growth_rate/100)
    print(populations)
    return populations


current_population = 10000
growth_rate = 10  # 10% per year
years = 10

past_population = calculate_past_population()
print("Population at the end of each of the last 10 years:")
for year, population in past_population:
    print(f"In {year}, populalation {population}")
