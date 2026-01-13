# challenge 1
# lst = ['ram','11','shyam','22','hari','77']
# a = list(filter(lambda x: not x.isdigit(),lst))
# print(a)

# challenge 2
# products = [
#  {'id': 1, 'name': 'laptop', 'category': 'electronics', 'price': 1200, 'instock': True},
#  {'id': 2, 'name': 'smartphone', 'category': 'electronics', 'price': 800, 'instock':
# False},
#  {'id': 3, 'name': 'pc', 'category': 'electronics', 'price': 15000, 'instock': True}
# ]
# a = list(filter(lambda x : x['instock'] == True,products))
# print(a)

# challenge 3

# a = int(input("Enter a initial range : "))
# b = int(input('Enter the final range : '))
# def calculate_sum(x,y) :
#     total=0
#     c = range(x,y+1)
#     for i in c :
#         total+=i
#     print(total)       
# calculate_sum(a,b)

# challenge 4
# def calculator () :
#     while True : 
#         a = int(input('Enter 1st number : '))
#         b = int(input("Enter 2nd number : "))
#         print('press 1 for add, 2 for subtract, 3 for multiply, 4 for divide')
#         choice = int(input("Enter your choice (0 for exit) : "))
#         if choice== 0 :
#             break
#         if choice == 1 :
#             def add(x,y) :
#                 return x+y
#             print(add(a,b))
#         if choice == 2 :
#             def sub(x,y) :
#                 return x-y
#             print(sub(a,b)) 
#         if choice == 3 :
#             def multiply(x,y) :
#                 return x*y
#             print(multiply(a,b))  
#         if choice == 4 :
#             def divide(x,y) :
#                 if b == 0 :
#                     print("zero error. Enter valid input")    
#                 return x/y
#             print(divide(a,b))  
# calculator()   

# challenge 5

# course = [{'title': 'Modern World History', 'genre': 'history'},
#           {'title': 'Modern World ', 'genre': 'scifi'},
#           {'title': 'Modern  History', 'genre': 'fiction'},
#           {'title':  'World History', 'genre': 'history'}]
# a = list(filter(lambda x : x['genre'] == 'history',course))
# print(a)

# challenge 6


# emails = ['ram.sharma@gmail.com', 'spam@hooya.com', 'virus@malware.net',
# 'shyam.kumar@workcorp.com']
# blacklist = ('@hooya.com', '@malware.net')
# a = list(filter(lambda x : x.endswith(blacklist),emails))
# print(a)

# challenge 7

# price = [100,50,200,75]
# a = list(map(lambda x : x*0.8,price))
# print(a)

# challenge 8
# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# def skip_two (a) :
#     new_list = []
#     for i in a[:12:2] :
#         new_list.append(i)
#     return new_list    
        

# print(skip_two(lst))

# challenge 9
# lst = [1,2,3,4,5,6,7,8,9,10]
# index_remove = int(input("Enter a inex you want to remove : "))
# def remove_at_idx(a,b) :
#     a.pop(b)
#     return a

# print(remove_at_idx(lst,index_remove))

# challenge 10
# user_input = input("Enter a string : ")
# def data_cleaning(x) :
#     a = x.maketrans('@#!%*$^&()','##########')
#     b = x.translate(a)
#     print(b)
# data_cleaning(user_input)

# challenge 11
  
# user_db = {'av' : {'email' : 'AA','password' :'v'},
#            'bv' : {'email' : 'bb','password' :'vv'},
#            'cv': {'email' : 'cc','password' :'vvv'},
#            'dv' : {'email' : 'dd','password' :'vvvv'}
#           }

# user_db = {}
# def register_user(a) :
#                 USERNAME = input("Enter username :  ")
#                 EMAIL = input("Enter email : ")
#                 PASSWORD = input('Enter  password : ')
#                 if USERNAME in a :
#                     print("Username already exist.")
#                 else :
#                     a[USERNAME] = {'email':EMAIL, 'password' : PASSWORD}
#                 print(f'registration successfull for {USERNAME}')
#                 print(a)   
# def login_user(a) :
#                 USERNAME = input("Enter username :  ")
#                 EMAIL = input("Enter email : ")
#                 PASSWORD = input('Enter  password : ')
#                 if USERNAME not in a :
#                     return 'username not found'
#                 elif a[USERNAME]['password']!= PASSWORD :
#                     return 'invalid password'
#                 else :
#                     return f'login successfull for {USERNAME}'
# while True : 
#         choice = input("1. register 2.login 3.exit ")
#         if not choice.isdigit() :
#             print('invalid input')
#         else : 
#             choice = int(choice) 
#             if choice == 1 :
#                 print(register_user(user_db))
#             elif choice == 2 :
#                 print(login_user(user_db) )   
#             elif choice == 3 :
#                 break
#             else :
#                 print('Invalid choice')

# challenge 12

# inventory = [{'name': 'Laptop', 'price': 50000,
# 'quantity': 5},{'name': 'comp', 'price': 20000,
# 'quantity': 2},{'name': 'pc', 'price': 10000,
# 'quantity': 3},{'name': 'phone', 'price': 30000,
# 'quantity': 4}]
# def add(a):
#     NAME = input("Enter product name : ")
#     PRICE = input("Enter product  price : ")
#     QUANTITY = input("Enter product quantity : ")
#     for i in a :
#         if i['name']== NAME :
#             print('Product already exist')
#             return
#     a.append({'name': NAME, 'price' :PRICE, 'quantity' :QUANTITY})
#     print('product added')
#     print(a)
                                   
# def view(a):
#     print("Product Name", "Price", "Quantity", sep = '     ')
#     print("-" * 35)
#     for i in a:
#         print(i['name'],i['price'],i['quantity'],sep = '            ')
# def update(a) :
#     name = input("Enter product name to update: ")
#     for item in a:
#         if item['name'] == name:
#             new_price = int(input("Enter new price: "))
#             new_quantity = int(input("Enter new quantity: "))

#             item['price'] = new_price
#             item['quantity'] = new_quantity

#             print("Product updated successfully")
#             return
#     else : 
#         print("Product not found")
    
# def delete(a) :
#     delete_input = input("Enter the name of product to delete: ")
#     for item in a:
#         if item['name'] == delete_input:
#             a.remove(item)
#             print("Product deleted successfully")
#             return a  
#     print("Product not found")
# def total(a) :
#     total = 0 
#     for i in a :
#         total+=i['price']*i['quantity']
#     print(total)    
        
# while True  :
#           choice = input('1. add new product 2.view all product 3.update product details 4. delete a product 5. calculate total inventory value 6. exit ')
#           if not choice.isdigit() :
#                 print('invalid input')
#           else : 
#                 choice = int(choice) 
#                 if choice == 1 :
#                     add(inventory)
#                 elif choice == 2 :
#                     view(inventory) 
#                 elif choice == 3 :
#                     update(inventory)
#                 elif choice == 4 :
#                     delete(inventory)
#                 elif choice == 5 :
#                     total(inventory)
#                 elif choice == 6 :
#                     break    
#                 else :
#                     print('Invalid choice')

# challenge 13
contacts = [
    {'name': 'Ram kc', 'phone': '9801234567', 'email': 'ram@email.com'}
]
def add_contact(contacts):
    name = input("Enter name: ")
    for c in contacts:
        if c['name'].lower() == name.lower():
            print("Contact already exists")
            return
    phone = input("Enter phone (10 digits): ")
    if not (phone.isdigit() and len(phone) == 10):
        print("Invalid phone number. Must be 10 digits.")
        return
    email = input("Enter email (must contain @ and .): ")
    if '@' not in email or '.' not in email:
        print("Invalid email format")
        return
    contacts.append({'name': name, 'phone': phone, 'email': email})
    print("Contact added successfully")
def display_contacts(contacts):
    if not contacts:
        print("No contacts found")
        return
    print("\n{:<20} {:<12} {:<25}".format("Name", "Phone", "Email"))
    print("-" * 60)
    for c in contacts:
        print("{:<20} {:<12} {:<25}".format(c['name'], c['phone'], c['email']))
def search_contact(contacts):
    name = input("Enter name to search: ")
    for c in contacts:
        if c['name'].lower() == name.lower():
            print("Contact found:")
            print(c)
            return
    print("Contact not found")
def update_contact(contacts):
    name = input("Enter name to update: ")
    for c in contacts:
        if c['name'].lower() == name.lower():
            phone = input("Enter new phone (10 digits): ")
            if not (phone.isdigit() and len(phone) == 10):
                print("Invalid phone number. Must be 10 digits.")
                return

            email = input("Enter new email (must contain @ and .): ")
            if '@' not in email or '.' not in email:
                print("Invalid email format")
                return

            c['phone'] = phone
            c['email'] = email
            print("Contact updated successfully")
            return
    print("Contact not found")
def delete_contact(contacts):
    name = input("Enter name to delete: ")
    for c in contacts:
        if c['name'].lower() == name.lower():
            contacts.remove(c)
            print("Contact deleted successfully")
            return
    print("Contact not found")
def sort_contacts(contacts):
    contacts.sort(key=lambda x: x['name'].lower())
    # n = len(contacts)
    # for i in range(n):
    #     for j in range(0, n-i-1):
    #         if contacts[j]['name'].lower() > contacts[j+1]['name'].lower():
    #             contacts[j], contacts[j+1] = contacts[j+1], contacts[j]
    # print("Contacts sorted alphabetically (manual method)")

    print("Contacts sorted alphabetically")
while True:
    print("\n1. Add Contact")
    print("2. Display All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Sort Contacts")
    print("7. Exit")
    
    choice = input("Enter choice: ")
    if not choice.isdigit():
        print("Invalid input")
        continue

    choice = int(choice)
    
    if choice == 1:
        add_contact(contacts)
    elif choice == 2:
        display_contacts(contacts)
    elif choice == 3:
        search_contact(contacts)
    elif choice == 4:
        update_contact(contacts)
    elif choice == 5:
        delete_contact(contacts)
    elif choice == 6:
        sort_contacts(contacts)
    elif choice == 7:
        print("Exiting program")
        break
    else:
        print("Invalid choice")

      








       





















































































































