# 1

n = 5

badges = [10, 20, 30, 40, 50]
returned = [10, 20, 40, 50]

returned_hashmap = set(returned)

for i in badges:
    if i not in returned_hashmap:
        print(i)

# 2

grades = [1, 5, 3, 3]

if (sum(grades) % 2 != 0):
    print('No')