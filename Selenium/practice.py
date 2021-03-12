# def fun(num1, num2):
#     if num1 * num2 > 1000:
#         return num1 + num2
#     else:
#         return num1 * num2
#
#
# i = 1
# for i in range(10):
#     if i > 0:
#         print('CurrentNumber:', i, 'Previous Number:', i - 1, 'sum:', i + i - 1)


# str = "Learning Python"
# print(len(str))
#
# i = 0
# for i in range(len(str)):
#     if i % 2 == 0:
#         print(str[i])

# for i in range(0, len(str), 2):
#     print("index[", i, "]", str[i])


str = "Python_Learning"


#
# def removeChars(stringvalue, num):
#     return stringvalue[num:]
#
#
# print(removeChars(str, 4))


def DivisibleBy5(list):
    for i in range(0, len(list)):
        if list[i] % 5 == 0:
            print(list[i])


DivisibleBy5([1, 2, 3, 4, 1, 10, 45, 10])
