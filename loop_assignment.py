
#1
# for i in range(1,6) :
#     if i %2 == 0 :
#         print(f'Number {i} is even')
#     else :
#         print(f'Number{i} is odd')    
    
#2
# running_total = 0
# list = [10,20,30,40]
# for i in list :
#     running_total+=i
#     print('added',i,'Running total is',running_total)
    

# print('Total sum : ',running_total)    

#3
# print('--Email greetings generated--')
# student_names = ['Ram','Hari','Sita']
# for i in range(len(student_names)) :
#     print('Hi',student_names[i],'your course approval is ready')

#4
# print('--Book Chapter Summary--')
# count = 0
# chapters = [45,30,50,40]
# for i in range(len(chapters)) :
#     count+=1
#     print('chapter',count, 'has ',chapters[i],'pages')

#5
# count = 1
# lists = [4,5,3,2]
# for i in lists :
#   count = count*i
  
# print(count)  

# 6
# for i in range(1,11) :
#     print(f'{11}','*',i,'=',11*i)

#7
# students = [{'name' : 'hari','math_grade':43},
#             {'name' : 'ram','math_grade':65},
#             {'name' : 'sita','math_grade':90},]

# for i in students : 
#    if i['math_grade']>70 :
#        i['status']='approved'
#    else :
#        i['status']='rejected'

# print(students)

#8
# list1 = [1,2,3,4,5]
# list2 = [3,4,5,6,7]
# for i in list1 :
#     for j in list2 :
#         if i==j :
#             print(i)

#9
# lst = [1,2,3,4]
# for i in lst :
#     if i == 2 or i==3 :
#         continue
#     else :
#         print(i)

#10
# lst = [1,2,3,4]
# for i in lst :
#     if i == 3:
#         continue
#     else :
#         print(i)

#11



# lst = [1,2,3,4]
# for i in lst :
#    if i == 3 :
#        lst.remove(3)
# lst.insert(1,'a')      
# print(lst)  

#12
# odd = []
# even = []
# lST = [1,2,3,4,5] 
# for i in lST :
#     if i%2 == 0 :
#         even.append(i)
#     else :
#         odd.append(i)
        
# print(odd)
# print(even)

# 13
# flag = False
# prime = int(input("Enter your number :"))
# for i in range(2,prime) :
#     if prime%i == 0 :
#         flag = True
#         break
    
        
# if flag :
#        print("not prime")
# else :
#     print('prime')
 
#14
# string_1 = []
# intgr = []
# lst = [1,2,3,4,'a','b']
# for i in lst :
#     if type(i) == str :
#         string_1.append(i)
#     else :
#         intgr.append(i)
        
# print(string_1)
# print(intgr)

#15
# intgr = 0
# strng= 0
# program = 'wwe12467ramshyam'
# for i in program :

#     if i.isdigit() :
#         intgr+=1
#     else :
        
#        strng+=1
# print(intgr,'digits')
# print(strng,'letters')

#16
# user_name = 'bikrant'
# password = 'bikrant123'
# for i in range(3) :
#     user = input("Enter your username : ")
#     passw = input("Enter your password : ")
#     if user == user_name and  passw== password :
#         print(f"welcome {user}!!")
#         break
#     else :
#         print('Invalid username or password')    
                 
# else :
#     print("Too many failed attempt. Account locked.")

#17
# number = int(input("Enter a number : "))
# if number%2 == 0 :
#     print("even")
# else :
#     print('odd')    

#18
# fact = 1
# number = int(input("Enter a number for factorial  : "))
# for i in range(1,number+1) :
#     fact = fact*i
    
# print(fact) 

#19
# for i in range(1,9) :
#     for j in range(1,11) :
#         print(i,"*",j,"=",i*j)

#20
# lst = [1,2,3,4]
# for i in lst :
#     if i == 2 or i ==1 :
#         print(i)
#     else :
#         continue 

#21
# sum = 0
# range_ = int(input('Enter a number for range of odd numbers  : '))
# for i in range(1,range_+1) :
#     if i%2 == 0 :
#         continue
#     else :
#         sum+=i
        
# print("total sum of odd numbers : ",sum) 

#22    

# sum = 0
# range_ = int(input('Enter a number for range of even numbers  : '))
# for i in range(1,range_+1) :
#     if i%2 == 0 :
#          sum+=i
#     else :
#       continue
        
# print("total sum of even numbers : ",sum) 

#23
# count = 0
# stringggg = input("Enter a string  : ")
# for i in stringggg :
#     if i == " " :
#         count+=1
#     else :
#         continue
    
# print(count) 

#24
# lst = [1, 2, 3, 4]
# result = []

# for i in lst:
#     result.append(i ** 3)

# print(result)

#25
# a = "programming"
# rev = ""

# for i in a:
#     rev = i + rev

# print(rev)

#26

# for i in range(50) :
#     if i == 8 :
#         break
#     else :
#         print(i)

#27

# strng = 'programming language'
# for i in strng :
#     print(i)

#28

# lst = ['ram','hari','shyam','geeta']
# for i in lst :
#     print(f'hello!,{i}.')

#29

# lst = ['ram','shyam','hari','geeta']
# result = []
# for i in lst :
#     result.append('dr.'+i)
    
# print(result)

#30

# lst = [1,3,6,4,8,9]
# result = []
# for i in lst :
#     result.append(i*i) 
    
     
# print(result)

#31

# lst1 = [111,32,-9,-45,-17,9,85,-10]
# odd_lst = []
# for i in lst1 :
#     if i>0 :
#       odd_lst.append(i)
      
# print(odd_lst)     

#32

# lst = [0,1,2,3,4,5,6]
# for i in lst : 
#     if i ==3 or i == 6 :
#         continue
#     else :
#         print(i) 

#33

# lst1 = ['ram',1,2,'hari',1.25,4+5j]
# lst2 = []
# for i in lst1 :
#     lst2.append(type(i))

# print(lst2) 

#34
# for i in range(20)  :
#     print(i)
# else :
#     print('Done')     

#35
# for i in range(105,6,-7) :
#     print(i,end=' ')


#36
# bad_chars = [';', ':', '!', '*']
# string = "py;th* o:n ! ;py * t*h:o !n"
# result = ""
# for i in string:
#     if i not in bad_chars and i != " ":
#         result += i

# print(result)

#37

# lst = [1,2,3,4,5,6,7,8,9,11,2,3,45,6,7,78,54]
# odd = 0
# even = 0
# for i in lst :
#     if i%2 == 0 :
#         even+=1
#     else :
#         odd+=1
        
# print("odd : ",odd)
# print('even :',even)           

#38

# total = 0

# for i in range(3, 100):
#     if i % 3 == 0 or i % 5 == 0:
#         total += i

# print("Sum =", total)

#39

# even_sum = 0
# odd_sum = 0

# for i in range(1, 101):
#     if i % 2 == 0:
#         even_sum += i
#     else:
#         odd_sum += i

# print("Sum of even numbers:", even_sum)
# print("Sum of odd numbers:", odd_sum)
    
#40

# num = int(input("Enter a number: "))
# temp = num
# rev = 0

# for _ in range(len(str(num))):
#     digit = temp % 10
#     rev = rev * 10 + digit
#     temp //= 10

# if num == rev:
#     print("Palindrome number")
# else:
#     print("Not a palindrome number")

#41

# num = int(input("Enter a number: "))
# temp = num
# cubes = 0
# digits = len(str(num))

# for _ in range(digits):
#     digit = temp % 10
#     cubes += digit ** digits
#     temp //= 10

# if cubes == num:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")

#42

vowels = ['a','e','i','o','u']
stringgg = 'aeiouprogrammingpython' 
for i in stringgg :
    if i not in vowels :
        print(i,end='')
    else :
        continue    






      
        
        

    
        
    
    

       

   


        
    



        
        
        
                  

    
        
            



        
    
           
      
        


    

