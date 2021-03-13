def countSubString(Str, substring):
    count = 0
    for i in range(len(Str) - 1):
        if Str[i:i + len(substring)] == substring:
            count = count + 1
    return count


c = countSubString("Sachin is a Good Boy.Sachin is a Programmer", "Sachin")


# print(c)

def pattern1(num):
    for i in range(1, num + 1):
        for j in range(i):
            print(i, end=" ")

        print('\n')


# pattern1(5)
def reverseNum(num):
    reversenum = 0
    while num > 0:
        reminder = num % 10
        reversenum = reversenum * 10 + reminder
        num = num // 10
    return reversenum


print(reverseNum(125))