#! usr/bin/env python3

print("\nLISTCOMP: ")
# 2D list comp
[[print("{} ---- {}".format(n1, n2)) for n2 in range(7)] for n1 in range(7)]

# 2D generator
big_gen = (((n1, n2) for n2 in range(7)) for n1 in range(7))

print("\nGENERATOR: ")
for i in big_gen:
    for j in i:
        print(j)
