# def mathqilish(a:int, amal, b:int):
#     # """ """ << bu ham hutti comentga olishga uhshedi.
#     a = int(input("Son kiriting ! "))
#     amal = input("Amal kiriting ! ")
#     b = int(input("Son kiriting ! "))
#     if amal == '+':
#         return a + b
#     elif amal == '-':
#         return a - b
#     elif amal == '*':
#         return a * b
#     elif amal == '/':
#         return a / b

# math = mathqilish("a", "amal", "b")
# print(math)


# def toqson_chiqarish(numbers="ism kiritilmadi"):
#     print("Salom:", numbers)


# toqson_chiqarish()

# def toqson_chiqarish(a:int):
#     print("SOn", a)

# toqson_chiqarish()


def toqsoni_chiqarish(numbers: list):

    toq = []
    for i in numbers:
        if i % 2 != 0:
            toq.append(i)
    return toq


number = [1, 3, 5, 2, 6, 8, 34, 55, 100, 31]
toqs = toqsoni_chiqarish(number)
print("Toq sonlar:",  toqs)
