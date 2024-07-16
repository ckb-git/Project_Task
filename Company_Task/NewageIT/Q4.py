# Q4. Code should ask 6 city names as input remove vowels 
# from all 6 city names. Sort out the words (after removal of vowels) 
# basis number of characters in word.
cities = []
for i in range(6):
    city = input("Enter Cityname: ")
    cities.append(city)
def remove_vowels(city):
    return ''.join(char for char in city if char.lower() not in 'aeiou')

Res_cities= []
for i in cities:
    Res_cities.append(remove_vowels(i))
print("after remove vowels")
print(Res_cities)

sorted_cities = sorted(Res_cities, key=len)
print ("after sorting cities")
print(sorted_cities)