numbers_1 = []
numbers_2 = []
numbers_3 = []

for n in range(1,101) :
    if n % 2 == 0 :
        numbers_1.append(n)
    if n % 3 == 0 :
        numbers_2.append(n)
    if n % 5 == 0 :
        numbers_3.append(n)
print(numbers_1)
print(numbers_2)
print(numbers_3)