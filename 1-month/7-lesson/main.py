# salom = ["s", "a", "l", "o", "m"]
# l = 0
# r = len(salom) - 1
# while l < r:
#     salom[l], salom[r] = salom[r], salom[l]
#     l += 1
#     r -= 1
# print(salom)

# salom = ["s", "a", "l", "o", "m"]
# salom.sort(reverse=True)
# # print(salom)

# capitalize() = capitalize va title() ni farqi,
# title ma'salan u gaplardagi har bir sozni boshidegi harfni kattaqilib beradi
# capitalize esa u gapdagi faqat birinchi harfni yozib beradi.


def faktorial_hisoblash():
    faktorial = int(input("Son kiriting >>> "))
    alif = 1
    for a in range(1, faktorial + 1):
        alif *= a

    print(f"Faktorial hisob : {faktorial} soni = {alif} teng")

faktorial_hisoblash()
# 1)