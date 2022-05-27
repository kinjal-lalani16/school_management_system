L = [1,2,3,4,5,6,7,8,9,10]
even_numbers = []
odd_numbers = []
for number in l:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
print(even_numbers)
print(odd_numbers)
