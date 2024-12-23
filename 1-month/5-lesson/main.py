# while True:

#     def salomberish(name): 
#         question = input("Enter your name >>>")
#         return f"What's up, {question}"

#     ismm = salomberish("khushnud")
#     print(ismm)

# def infoberish(username, password, birthdate, number, adress=None):
#         """Account create qilish funkstsiyasi, va shuningde'k instruktsiyalar""" 
#         info = {
#             "username": username,
#             "password": password,
#             "birthdate": birthdate,
#             "number": number,
#             "adress": adress
#         }
#         return info

# print("\nSaytmizda Account yaratamiz.\n")
# account = []

# while True:
#         alif = input("Ma'lumotlaringizni kiritish uchun (keyingi) ni kiring / chiqib ketish uchun (Exit) ni kiriting >>> ")
#         if alif in ["dalley", "daley", "keyingi"]:
#                 username = input("\nIsmi: ")
#                 password = int(input("\nParol: "))
#                 birthdate = int(input("\nTug'ilgan sana: "))
#                 number = int(input("\nTelefon raqami: "))
#                 adress = input("\nMa'nzili: ")
#                 yangi_account = infoberish(username, password, birthdate, number, adress)
#                 account.append(yangi_account)
        
#         elif alif in ["yuq", 'exit', 'net', 'no', "Exit"]:
#                 print("Dastur yopildi !")
             
#         break    
# question = input("Ya'na account ochish ni hohlaysizmi? (ha/yuq) ")
#         if question in  ['ha', 'allbata']:
#                 username = input("\nIsmi: ")
#                 password = int(input("\nParol: "))
#                 birthdate = int(input("\nTug'ilgan sana: "))
#                 number = int(input("\nTelefon raqami: "))
#                 adress = input("\nMa'nzili: ")
#                 account.append(infoberish(username, password, birthdate, number, adress))
        
#         elif question in ['no', 'net', 'yuq']:
#                 print("Dastur yopildi !")
#         else:
#                 print("Notugri buyruq, qaytadan urinib kuring")  
#         break

# # for info in account:
# #     if info['adress']:
# #         adress = info['adress']
# #     else:
# #         adress = "Nomalum"

# #     def infoberish1():
# #         print(f"{info['username'].title ,{info["password"].title}}") 


def infoberish(username, password, birthdate, number, adress=None):
    """Account yaratish funktsiyasi va shuningdek instruktsiyalar"""
    info = {
        "username": username,
        "password": password,
        "birthdate": birthdate,
        "number": number,
        "adress": adress
    }
    return info


print("\nSaytimizda Account yaratamiz.\n")
account = []

while True:
    alif = input("Ma'lumotlaringizni kiritish uchun (keyingi) ni kiriting / chiqib ketish uchun (Exit) ni kiriting >>> ")
    
    if alif.lower() in ["dalley", "daley", "keyingi"]:
        username = input("\nIsmi: ")
        password = int(input("\nParol: "))
        birthdate = int(input("\nTug'ilgan sana: "))
        number = int(input("\nTelefon raqami: "))
        adress = input("\nManzili: ")
        yangi_account = infoberish(username, password, birthdate, number, adress)
        account.append(yangi_account)
        
        print("\nAccount yaratildi! Ma'lumotlar:")
        print(yangi_account)

    elif alif in ["yuq", 'exit', 'net', 'no', "Exit"]:
        print("Dastur yopildi!")
    
    else:
        print("Notog'ri buyruq berdingiz iltimos, qaytadan urinib ko'ring!")
        break