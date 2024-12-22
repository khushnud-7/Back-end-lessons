# mylist = [12, 14, 15, 16]
# leaf = []
# for x in mylist:
#         i = 2
#         x *= i
#         leaf.append(x)
# print(leaf)  

# for kitob in library:
#         print(library[kitob])

# if prompt in library:
#     print("Name of book:", library[prompt]['name'])
#     print("Price of book:", library[prompt]['Price'])
#     print("Plot of book:", library[prompt]['Plot'])
#     print("Author of book:", library[prompt]['Author'])
#     print("Book's Published year:", library[prompt]['Published_Year'])

# f"""{i}: {library[prompt][i]}"""

# books = {
#     "men": {
#         "narxi": 15,
#         "tavsif": "Kitob tavsifi",
#         "soni": 20,
#         "muallif": "Fotih Duman"
#     },
#     "sen": {
#         "narxi": 10,
#         "tavsif": "Kitob tavsifi",
#         "soni": 10,
#         "muallif": "Fotih Duman"
#     }
# }

# while True:
#     kitob = input("Kitob nomini yozing (chiqish uchun exit): ")
    
#     if kitob == "exit" or kitob == "Exit":
#         print("Dastur tugatildi.")
#         break
    
#     if kitob in books:
#         text = f"Kitob nomi: {kitob}\n"
#         for i in books[kitob]:
#             text += f"{i}: {books[kitob][i]}\n"
#         print(text)
#     else:
#         print("Bu kitob mavjud emas.")
#         savol = input("Shu kitobni qo'shishni xohlaysizmi? (ha/yo'q): ").lower()
#         if savol == "ha":
#             narxi = int(input("Narxi: "))
#             soni = int(input("Soni: "))
#             jami = soni * narxi
#             books[kitob] = {
#                 'narxi': int(narxi),
#                 'soni': int(soni),
#                 "jami": jami
#             }
            
#             print(f"{kitob}ning jami narxi: {books[kitob]['jami']}")
#             print(f"{kitob} kitobi muvaffaqiyatli qo'shildi.")
            
#         elif savol == "yo'q" or savol == "no":
#             print("Tushunarli, davom etamiz.")
#             break

# quantity_soni = int(input("How many copies do you want to buy? >>> "))

# library = {
#     "me": {
#         "name": "Roman",
#         "Price": 12,
#         "quantity": 5,
#         "Plot": "About Love",
#         "Author": "Pushkin",
#         "Published_Year": 1871,
#         "sum": []
#     },
#     "u": {
#         "name": "Automn",
#         "Price": 15,
#         "quantity": 5,
#         "Plot": "About countryside",
#         "Author": "Tolstoy",
#         "Published_Year": 1872,
#         "sum": []
#     }
# }

# while True:
#     prompt = input("Search for a book >>> ")

#     if prompt in library:
#         text = f"The name of book: {prompt}\n"

#         for i in library[prompt]:
#             text += f"{i}: {library[prompt][i]}\n"

#         print(text)
#     else:
#         print("There is no book that you want.")
    
#     question = input("Do u want to add a book to this list [yes/no]? ")
#     if question == "yes":
#         name = input("Enter the name of the book: ")
#         price = int(input("Enter the price of the book: "))
#         plot = input("Enter the plot of the book: ")
#         author = input("Enter the author of the book: ")
#         published_year = int(input("Enter the published year of the book: "))
#         quantity = int(input("Enter the available quantity of the book: "))

#         library[prompt] = {
#             "name": name,
#             "Price": price,
#             "quantity": quantity,
#             "Plot": plot,
#             "Author": author,
#             "Published_Year": published_year,
#             "sum": []
#         }
#         print(f"Book: '{name}' has been added to the library:")
#         print(f"   Name: {name}")
#         print(f"   Price: {price}")
#         print(f"   Quantity: {quantity}")
#         print(f"   Plot: {plot}")
#         print(f"   Author: {author}")
#         print(f"   Published Year: {published_year}\n")
    
#     narxi = int(input("Narxi: "))
#     soni = int(input("Soni: "))
#     jami = soni * narxi
#     library[prompt] = {
#     'narxi': int(narxi),
#     'soni': int(soni),
#     "jami": jami
#     }       
#     print(f"{prompt}ning jami narxi: {library[prompt]['total_price']}")
#     print(f"{prompt} kitobi muvaffaqiyatli qo'shildi.")
    
#     elif question == "no" or question == 'yuq':
#     print("\nNo new book was added to the library.")
#     break

# while True:
#     library = {
#     "me":{
#         "name":"Roman",
#         "Price":12,
#         "quantity":5,
#         "Plot":"About Love",
#         "Author":"Pushkin",
#         "Published_Year":1871,
#         "sum":[]
#     },
#     "u":{
#          "name":"Automn",
#          "Price":15,
#          "quantity":5,
#          "Plot":"About countryside",
#          "Author":"Tolstoy",
#          "Published_Year": 1872,
#          "sum":[]
#     }
# }

#     prompt = input("Search for a book >>> ").title()
 
#     if prompt in library: 
#         text = f"\nThe name of book: {prompt}\n"
    
#         for i in library[prompt]:
#             text += f"{i}: {library[prompt][i]}\n"                
#             print(text)
                
#     quantity_soni = int(input("How many copies do you want to buy? >>> "))
#     if quantity_soni <= library[prompt]["quantity"]:
#         total_price = quantity_soni * library[prompt]["Price"]
#     library[prompt]["sum"].append(total_price)
#     print(f"Total price of {quantity_soni} copies: {total_price}\n")
#     else:
#     print(f"Sorry, only {library[prompt]['quantity']} copies are available.\n")
    
#     else:
#     print("There is no books that you want")
#     question = input("Do u want to add a book to this list? ")
#     if question == 'yes' or question == "da" or question == 'ha':
#             name = input("Enter the name of the book: ")
#             price = input("Enter the price of the book: ")
#             plot = input("Enter the plot of the book: ")
#             author = input("Enter the author of the book: ")
#             published_year = input("Enter the published year of the book: ") 
#             library[prompt] = {
#         "name": name,
#         "price": price,
#         "plot": plot,
#         "author": author,
#         "published_year": published_year,
#     }
#             print(f" Book: '{name}' has been added to the library:")
#             print(f"   Name: {name}")
#             print(f"   Price: {price}")
#             print(f"   Plot: {plot}")
#             print(f"   Author: {author}")
#             print(f"   Published Year: {published_year}\n")
        
#     elif question == 'yuq' or question == 'net' or question == "no": 
#         print("\nNo new book was added to the library")  
#         break

# library = {
#     "me": {
#         "name": "Roman",
#         "Price": 12,
#         "quantity": 5,
#         "Plot": "About Love",
#         "Author": "Pushkin",
#         "Published_Year": 1871,
#         "sum": []
#     },
#     "u": {
#         "name": "Autumn",
#         "Price": 15,
#         "quantity": 5,
#         "Plot": "About countryside",
#         "Author": "Tolstoy",
#         "Published_Year": 1872,
#         "sum": []
#     }
# }

# while True:
#     prompt = input("Search for a book [Exit]  >>> ").title()
#     if prompt == "Exit":
#         print("Program was finished")
#         break;
        
#     if prompt in library:
#         text = f"The name of the book: {prompt}"
#         for i in library[prompt]:
#             text += f"{i}: {library[prompt][i]}\n"
#             print(text)
            
#         quantity_soni = int(input("How many copies do u want to buy >>> "))
        
#         if quantity_soni <= library[prompt]["quantity"]:
#                 total_price = quantity_soni * library[prompt]["Price"]
#                 library[prompt]["sum"].append(total_price)  
#                 library[prompt]["quantity"] -= quantity_soni  
#                 print(f"Total price of {quantity_soni} copies: {total_price}")
#                 print(f"Remaining copies: {library[prompt]['quantity']}\n")
#         else:
#                 print(f"Sorry, only {library[prompt]['quantity']} copies are available.\n")
    
#     else:
#         print("There is no book that you want.\n")
#         question = input("Do you want to add a book to this list? [yes/no]>>> ").lower()
        
#         if question in ['yes', 'da', 'ha']:
#             name = input("Enter the name of the book: ").title()
#             price = int(input("Enter the price of the book: "))
#             quantity = int(input("Enter the quantity of the book: "))
#             plot = input("Enter the plot of the book: ")
#             author = input("Enter the author of the book: ")
#             published_year = int(input("Enter the published year of the book: "))
            
#             library[name] = {
#                 "name": name,
#                 "Price": price,
#                 "quantity": quantity,
#                 "Plot": plot,
#                 "Author": author,
#                 "Published_Year": published_year,
#                 "sum": []
#             }
#             print(f"Book '{name}' has been added to the library:\n"
#                   f"   Name: {name}\n"
#                   f"   Price: {price}\n"
#                   f"   Quantity: {quantity}\n"
#                   f"   Plot: {plot}\n"
#                   f"   Author: {author}\n"
#                   f"   Published Year: {published_year}\n")
        
#         elif question in ['no', 'net', 'yuq']:
#             print("\nNo new book was added to the library.\n")
#             break
        
numbers = [11, 12, 140, 214, 215, 516, 17, 18]
number1 = [12, 15, 50, 320, 120, 15, 18, 20]
juft = []
tog = []
let = numbers + number1

for s in let:
    if s % 2 == 0:
        juft.append(s)
    else:
        tog.append(s)

print("Juft sonlar:", (juft))
print("Toq sonlar:", (tog))
