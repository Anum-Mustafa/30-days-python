#Example 1
for i in range(1,11):
    print(i)

#Example 2 (while)
counter = 1
while counter<=10:
     print('current value:', counter )
     counter = counter + 1

#Example 3
countries = ['Thailand', 'Vietnam', 'Malaysia', 'UAE']
for country in countries:
    print(country, 'contains', len(country), 'letters!')

#Example 4
my_list=[1,2,3,4,5,6,7,8,9,10]
for my_var in my_list:
    print(my_var)

#Example 5
# Number for which to print the multiplication table
number = 15
# Loop through numbers 1 to 10
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
