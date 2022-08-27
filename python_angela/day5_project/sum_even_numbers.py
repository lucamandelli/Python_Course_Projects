def sum_even_numbers():
    range_num = int(input("Until what even number do you want to sum? "))
    sum = 0
    for num in range(0, range_num + 1, 2):
        sum += num
    print(sum)

sum_even_numbers()
