numbers = []
zero = 0
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
while len(my_list) > zero:
    if my_list[0] > zero:
        numbers.append(my_list.pop(0))
        continue
    elif my_list[0] <= zero:
        my_list.pop(0)
        continue
    else:
        break

print(numbers)
