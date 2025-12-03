# question 1
# num1 = int(input("Enter 1st number : "))
# num2 = int(input("Enter 2nd number : "))
# num3 = int(input("Enter 3rd number : "))
# if num1> num2 and num1> num3 :
#     print(num1," is greatest among 3")
# elif num2> num1 and num2> num3 :
#     print(num2," is greatest among 3")
# else:
#     print(num3, "is greatest among 3")
    
# challenge 2 
# month = int(input("Enter a month you want to print name of (1-12) : "))
# dict = {
#     1 : "January",
#     2 : "Feb",
#     3 : "March",
#     4 : "April",
#     5 : "May",
#     6 : "June",
#     7 : "July",
#     8 : "August",
#     9 : "September",
#     10 : "OCT",
#     11 : "NOV",
#     12 : "Dec",    
# }   
# if month in dict :
#     print(dict[month]) 
    
# challenge 3

# num1 = int(input("Enter 1st number : "))
# num2 = int(input("Enter 2nd number : "))
# temp = num1
# num1 = num2
# num2 = temp
# print(num1)
# print(num2)

# challenge 4

# age = int(input("Enter your age : "))
# membership = eval(input("Enter True or False : ").strip())
# if age< 12 :
#     print("You dont have to pay for ticket")
# elif 12<=age<=60 :
#     if membership :
#         print("You have to pay RS. 150 as ticket price")
#     else : 
#         print("You have to pay RS.200 as ticket price")
# else :
#     print("You have senior citizen discount!! You have to only pY RS. 100")            

# challenge 5
# unit_consumed = int(input("Enter total units utilized : "))
# if unit_consumed < 100 :
#     cost = unit_consumed*5
#     print("Total Cost : RS.",cost,sep="")
# if 100<=unit_consumed<=300 :
#     cost = 500 + (unit_consumed-100)*8
#     print("Total Cost : RS.",cost,sep="")
# elif unit_consumed>300 :
#     cost = 500 + 1600 + (unit_consumed-300)*10
#     print("Total Cost : RS.",cost,sep="")  

# challenge 6
# player1 = input("Enter either rock, paper or scissor for 1st player : ").strip().lower()
# player2 = input("Enter either rock, paper or scissor for 2nd player : ").strip().lower()
# if player1 == "rock" :
#    if player2 == "paper" :
#     print("player1 won")
#    elif player2 == "scissor" :
#     print("player2 won")
#    elif player2 == "rock" :
#     print("tie") 
# elif player1 == "paper" :
#    if player2 == "paper" :
#     print("tie")
#    elif player2 == "scissor" :
#     print("player2 won")
#    elif player2 == "rock" :
#     print("player2 won")
# elif player1 == "scissor" :
#    if player2 == "paper" :
#     print("player 1 won")
#    elif player2 == "scissor" :
#     print("tie")
#    elif player2 == "rock" :
#     print("player2 won") 
# else :
#     print("Enter only either rock,paper or scissor ")    

# challenge 7
# a = int(input("Enter total no. of students in 1st class : "))
# b = int(input("Enter total no. of students in 2nd class : "))
# c = int(input("Enter total no. of students in 3rd class : "))
# if a % 2 == 0 :
#     desk1 = a/2
# else : 
#     desk1 = a//2 +1 
    
# if b% 2 == 0 :
#     desk2 = b/2
# else : 
#     desk2 = b//2 +1 
     
# if c % 2 == 0 :
#     desk3 = c/2
# else : 
#     desk3 = c//2 +1 
# print("The smallest possible number of desks that can be purchased : ",desk1+desk2+desk3)         
             
    
     
  
# challenge 8
# current_floor = 5
# user_pressed = 3
# if user_pressed < current_floor :
#     print("down")
# elif user_pressed > current_floor :
#     print("up")
# else : 
#     print("same floor")        

# challenge 9

# user = int(input("Enter  a number : "))
# if user > 0 :
#     print("positive") 
#     if user % 2 == 0 :
#         print("EVEN")
#     else :
#         print("ODD")    
# elif user < 0 :
#     print("negative")
# else :   
#   print("Enter a positive number")    

# challenge 10

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter 2nd number : "))
# if num1 > num2 :
#     print(f"{num1} greater")
# elif num1 == num2 : 
#     if num1 or num2 > 0 :
#         print("positive")
#     elif num1 or num2 < 0 :
#         print("negative")
#     else :
#         print("zero")            

# else : 

#     print(f"{num2} is greater") 

# challenge 11

# user = int(input(" Enter a number : "))
# if user % 3 == 0 and user % 5 == 0 :
#     print("fizz Buzz")
# elif user % 3 == 0  :
#     print("fizz")
# elif  user % 5 == 0 :
#     print(" Buzz")

# else : 
#     print(user)  

# challenge 12

# import random
# a = [0,1,2,3,4,5]
# b = random.choice(a)

# if b == 0 :
#     print("Flamingos turn pink from eating shrimp")
# elif b == 1 :
#     print("The only food that doesn't spoil is honey") 
# elif b == 2 :
#     print("Shrimp can only swim backwards")
# elif b == 3:
#     print("A taste bud's life span is about 10 days")
# elif b == 4 :
#     print("It is impossible to sneeze while sleeping")
# else : 
#     print("It is illegal to  sign off-key in North Carolina")

# challenge 13


# membership_input = input("Enter True or False: ").strip().lower()

# if membership_input == "true":
#     membership = True
# elif membership_input == "false":
#     membership = False
# else:
#     print("Invalid input! Please enter True or False.")
#     exit()

# total_purchase_amount = int(input("Enter the total purchase amount: "))

# if membership:
#     if total_purchase_amount > 1000:
#         discount = 0.20 * total_purchase_amount
#         print("Final amount after discount:", total_purchase_amount - discount)
# else:
#     if total_purchase_amount > 1000:
#         discount = 0.10 * total_purchase_amount
#         print("Final amount after discount:", total_purchase_amount - discount)

# challenge 14

# user_weight = float(input("Enter your weight on Earth (kg): "))
# planet_number = int(input("Enter planet number (1–7): "))

# planets = {
#     1: {'name': 'Mercury', 'gravity': 0.38},
#     2: {'name': 'Venus',   'gravity': 0.91},
#     3: {'name': 'Mars',    'gravity': 0.38},
#     4: {'name': 'Jupiter', 'gravity': 2.53},
#     5: {'name': 'Saturn',  'gravity': 1.07},
#     6: {'name': 'Uranus',  'gravity': 0.89},
#     7: {'name': 'Neptune', 'gravity': 1.14}
# }

# if planet_number in planets:
#     planet = planets[planet_number]
#     dest_weight = user_weight * planet['gravity']
    
#     print(planet['name'])
#     print("Destination Weight:", dest_weight, "kg")
# else:
#     print("Enter a number from 1–7 only.")
            
# challenge 15

 
# sub1 = int(input(" Enter marks in first subject : "))
# sub2 = int(input(" Enter marks in second subject : "))
# sub3 = int(input(" Enter marks in third subject : "))
# sub4 = int(input(" Enter marks in fourth subject : "))
# total_marks = (sub1+sub2+sub3+sub4)
# print("total marks obtained : ",total_marks)
# percentage = total_marks/4
# print("percentage obtained : ",percentage,"%")
# if percentage > 70 :
#     print("distinction")
# elif 60< percentage <70 :
#     print("first") 
# elif 40< percentage <60 :
#     print("pass")
# else :
#     print("fail")
 
# challenge 16    


# cost = int(input("Enter the price of the bike : "))
# if cost > 100000 :
#     print("tax to be paid : ",0.15*cost)
# elif 50000<cost<=100000 :
#     print("tax to be paid : ",0.10*cost)
# else:
#     print("tax to be paid : ",0.05*cost)

# challenge 17


# salary = int(input("Enter your salary : "))
# year_worked = int(input("Enter the years worked : "))
# if year_worked > 10 :
#     print("Bonus : ",0.1*salary)
# elif 6<year_worked<=10:
#     print("Bonus : ",0.08*salary)
# else :
#     print("Bonus : ",0.05*salary)

# challenge 18

# subject_score = int(input("Enter your subject score : "))
# if subject_score > 90 :
#     print("congratulations")
# elif 50<=subject_score<=90 :
#     print("Improvement needed")
# else : 
#     print("Consider retaking the course")
            
# challenge 19

# age = int(input("Enter your age : "))
# work_experience = float(input("Enter your work experience in years : "))
# degree_input = input("Enter True or False: ").strip().lower()

# if degree_input == "true":
#     degree = True
# elif degree_input == "false":
#     degree = False
# else:
#     print("Invalid input! Please enter True or False.")
#     exit()
# if age>= 18 :
#     if degree : 
#         if work_experience> 3 :
#             print("Highly eligible")
#         elif 1<=work_experience<=3 :    
#             print("Eligible")
#         else :
#             print("Under review")    
#     else :
#         print("Not eligible due to not havinga degree")
# else :
#     print("Not eligible due to age less than 18")

# challenge 20

# age = int(input("Enter your age : "))
# gender = input("Enter your gender(m/f) :").strip().lower()
# if 18<=age<30 :
#     if gender == 'm' :
#         print("Your wage is RS. 700")    
#     else : 
#         print('Your wage is RS. 750') 
# elif 30<=age<=40 :
#     if gender == 'm' :
#         print("Your wage is RS. 800")
#     else : 
#         print("Your wage is RS. 850")
# else : 
#     print("You are outside the range")  

# challenge 21   
                 
# is_valid = True
# user_pin = int(input("Enter your pin : "))
# initial_account_balance = 50000
# correct_pin = 123
# if correct_pin == user_pin :
#     print("1. Withdraw")
#     print("2. Check Balance")
#     print("3. Exit")
#     user_value = int(input("Enter a number for valid operation : "))
#     if user_value == 1 :
#         deduction_amount = int(input(" amount : "))
#         remaining_balance = initial_account_balance - deduction_amount
#         print("Remaining Balance : RS.",remaining_balance)
#     elif user_value == 2 :
#         print("Current Balance : RS.",initial_account_balance)  
#     elif user_value == 3 :
#         print("Thank you for visiting.")
#     else :
#         print("Enter only number from (1-3)")          
    
# else :
#     print("INCORRECT PIN!!!!!!!!")

# challenge 22

# print("Welcome to the Magic Forest ")
# northorsouth = input("Enter north or south : ").strip().lower()
# if northorsouth == 'south' :
#     print("game over!")
# elif northorsouth == 'north' :
#     riverorpath = input("you want to cross the river or follow the path? ")
#     if riverorpath == 'cross the river' :
#         print("game over!")
#     elif riverorpath == 'follow the path' :
#         fairy_ogre_elf = input("Enter either fairy or ogre or elf :").strip().lower()
#         if fairy_ogre_elf == 'ogre' :
#             print("Game over!")
#         elif fairy_ogre_elf == 'fairy' :
#             print("Game over!")
#         elif fairy_ogre_elf == 'elf' :
#             print("You Win!")
#         else :
#             print("Enter only valid option!!")        
#     else :
#         print("Enter only valid option!!")    
        
# else :
#     print("Enter only north or south!!")    

# challenge 23


print("Welcome to the Haunted House")
upordown = input("Enter you want to go upstairs or downstairs : ").strip().lower()
if upordown == 'downstairs' :
    print("game over!")
elif upordown == 'upstairs' :
    roomorout = input("you want to enter the room or stay outside? ")
    if roomorout == 'enter the room' :
        print("game over!")
    elif roomorout == 'stay outside' :
        ghost_vampire_werewolf = input("Enter either ghost or vampire or werewolf :").strip().lower()
        if ghost_vampire_werewolf == 'ghost' :
            print("Game over!")
        elif ghost_vampire_werewolf == 'vampire' :
            print("Game over!")
        elif ghost_vampire_werewolf == 'werewolf' :
            print("You Win!")
        else :
            print("Enter only valid option!!")        
    else :
        print("Enter only valid option!!")    
        
else :
    print("Enter only upstairs or downstairs!!")    
          




          
    


    

          
    
     




    
     
    
    
            