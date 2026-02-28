# 1
#
# n = 5
#
# badges = [10, 20, 30, 40, 50]
# returned = [10, 20, 40, 50]
#
# returned_hashmap = set(returned)
#
# for i in badges:
#     if i not in returned_hashmap:
#         print(i)

# 2

grades = [1, 5, 2, 3, 3]

if (sum(grades) % 2 != 0):
    print('No')
else:
    halfsum = sum(grades) // 2
    firstSum = 0
    for grade in grades:
        firstSum += grade
        if firstSum == halfsum:
            print('Yes')
            break
        elif firstSum > halfsum:
            print('No')
            break


# 3
# n = int(input())
# votes = list(map(int, input().split()))
#
# candidate = None
# count = 0
# for v in votes:
#     if count == 0:
#         candidate = v
#         count = 1
#     elif v == candidate:
#         count += 1
#     else:
#         count -= 1
#
# if votes.count(candidate) > n // 2:
#     print(candidate)
# else:
#     print(-1)

# 4

# n = 8
# marks = [5, 5, 4, 4, 4, 3, 3, 5]
#
# maxLen = 0
# previous = 0
# tempMax = 1
# for i in marks:
#     if i == previous:
#         tempMax += 1
#     else:
#         tempMax = 1
#     maxLen = max(maxLen, tempMax)
#     previous = i
#
# print(maxLen)