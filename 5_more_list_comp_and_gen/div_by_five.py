#! usr/bin/env python3


input_list = [2, 5, 1, 153, 15, 20, 13, 200, 10]


def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False


# Create a generator
div_5_gen = (li for li in input_list if div_by_five(li))


# normal
for li in div_5_gen:
    print(li)

# one liner
[print(li) for li in div_5_gen]
