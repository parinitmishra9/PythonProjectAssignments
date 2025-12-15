# Exercise - List & Loops
# ---------------------------------
countries = ["India", "Canada", "Brazil", "Germany", "Japan", "Australia"]

#  Count all the countries in the list starting with the letter 'I'
count_i = 0
for country in countries:
    if country.startswith('I'):
        count_i += 1
print("Number of countries starting with 'I':", count_i)
# ---------------------------------
# Create a new list containing only the countries with more than 6 letters
long_countries = []
for country in countries:
    if len(country) > 6:
        long_countries.append(country)
print("Countries with more than 6 letters:", long_countries)
# ---------------------------------
# Print each country in the list in uppercase
print("Countries in uppercase:")
for country in countries:
    print(country.upper())
# ---------------------------------
# Find the longest country name in the list
longest_country = ""
for country in countries:
    if len(country) > len(longest_country):
        longest_country = country
print("The longest country name is:", longest_country)
# ---------------------------------
# Create a new list with the lengths of each country name
country_lengths = []
for country in countries:
    country_lengths.append(len(country))
print("Lengths of each country name:", country_lengths)
# ---------------------------------