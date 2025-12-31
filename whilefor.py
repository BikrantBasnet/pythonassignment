# while for diff
# initialization of i for while is compulsory whereas auto for for loop
# values can be acccessed directly in for loop aswell as  through indexing whereas only through indexing in while loop

# items = [1,2,3,4]
# i = 0
# while i < len(items) :
#     print(items[i])
#     i+=1


# items = [1,2,3,4]
# i = 0
# while i < len(items) :
#     if items[i]%2== 0 :
#         print(items[i])
#     i+=1

# total = 0
# while True :
#     user = int(input("Enter a number : "))
#     if user <0 or user == 0 :
#         break
#     else  :
#         total+=user
        
# print(total)    

# n = int(input("Enter a number : "))
# i = 0 
# while i in range(n,0,-1) :
#     if i == 1 :
#         print("Lower threshold reached")
#         break
#     else : 
#         print(i)
#         i-=1   

# user = int(input('Enter a number : '))
# while user>1 :
#     print(user)
#     user-=1
    
# else :
#     print("Lower threshold reached")    

# import random
# n = random.randint(1,100)

# while True :
#     user = int(input("Enter a number to guess  : "))
#     if user == n :
#         print("Correct")
#         break
#     elif user> n :
#         print("too high")
#     else :
#         print("too low")    


# passwrd = input("Enter your password : ")
# while len(passwrd)<8 :
#     print("password must be 8+ characters")

# total = 0
# counter = 1
# while counter<=50 :
#     total+=counter
#     counter+=1
# print(total)   

# user = int(input("Enter a number for multiplication table : "))
# i = 1 
# while i <11 :
#     print(user,'x',i,'=',user*i)
#     i+=1 

# import random
# randnum = random.randint(1,50)
# i = 0
# tries = 7
# print(randnum)
# while  i<7 :
#     user = int(input("Enter a number to guess (1-50)  : "))
#     i+=1
   
#     if user == randnum :
#         print("correct")
#         break
#     else :
#         print('try again')
#         tries = 7-i
#         print(tries, "tries remaining")
# player1_total = 0
# player2_total = 0
# while True : 
#     player1 = input("Enter either rock, paper or scissor for 1st player : ").strip().lower()
#     player2 = input("Enter either rock, paper or scissor for 2nd player : ").strip().lower()
#     if player1 == player2 :
#         print('tie')
#     if player1 == "rock" :
            
#         if player2 == "scissor" :
#              player1_total+=1
#         elif player2 == "paper" :
#             player2_total+=1
            
#     elif player1 == "paper" :
       
#         if player2 == "scissor" :
#              player2_total+=1
#         elif player2 == "rock" :
#              player1_total+=1
#     elif player1 == "scissor" :
#         if player2 == "paper" :
#              player1_total+=1
#         elif player2 == "rock" :
#            player2_total+=1
           
#     print(f"Score = Player1: {player1_total}, Player2: {player2_total}")
#     if player1_total == 5 :
#         print("Player1 Won")
#         break      
      
#     if player2_total == 5 :
#         print("Player2 Won")
#         break        

# rules = {
#     "rock": "scissors",
#     "scissors": "paper",
#     "paper": "rock"
# }
# p1_score = 0
# p2_score = 0
# while p1_score < 5 and p2_score < 5:

#     p1 = input("Player 1 (rock/paper/scissors): ").lower()
#     p2 = input("Player 2 (rock/paper/scissors): ").lower()
#     if p1 not in rules or p2 not in rules:
#         print("Invalid input! Try again.")
#         continue

#     if p1 == p2:
#         print("Tie round!")

#     elif rules[p1] == p2:
#         p1_score += 1
#         print("Player 1 wins this round!")

#     else:
#         p2_score += 1
#         print("Player 2 wins this round!")
  
#     print(f"Score → Player 1: {p1_score} | Player 2: {p2_score}")

# if p1_score == 5:
#     print(" Player 1 wins the game!")
# else:
#     print(" Player 2 wins the game!")

 # walrus operator
 # while(user:=int(input("Enter a number : ")))>1 :
 # print(user)
 
# while True : 
#     age = int(input("Enter your age : "))   
#     if age<18 :
#         print("You are a minor")
#     elif 18<=age<60 :
#         print("You are an adult")
#     else :
#         print("You are a senior citizen")
    
#     user_stop = input("Do you want to stop? ").strip().lower()
#     if user_stop == 'stop' :
#         break  

# while True : 
#     vehicle = input("Enter vehicle name : ").strip().lower()
#     if vehicle!= "bus" :
#         print("waiting")
#     else :
#         print("Finally the wait is over")
#         break   


# while True : 
#     fruit = input("Enter fruit name : ").strip().lower()
#     if fruit!= "apple" :
#         print("Try again")
#     else :
#         print("You got it!!")
#         break  

# ratings = ['4+','9+','12+','17+','4+','9+','17+','12+','4+','17+']
# current_ratings = {}
# i = 0
# while i <len(ratings) : 
#     if ratings[i] in current_ratings :
#         current_ratings[ratings[i]]+=1
#     # current_ratings[ratings[i]]=current_ratings.get(ratings[i],0)+1
     # while ratings :
     # rating = ratings.pop()
     # current_ratings[rating]=current_ratings.get(rating,0)+1
        
#     else :
#         current_ratings[ratings[i]]=1
        
#     i+=1
    
# print(current_ratings)  

# import random
# total_guess = 0
# number = random.randint(1,10)
# print(number)
# while True : 
#     guess = int(input("Enter a number to guess   : "))
#     if guess>number : 
#         print("Too high")
#         total_guess+=1

#     elif guess<number : 
#         print("Too low")
#         total_guess+=1
#     else :
#         total_guess+=1
#         break    
# print(f'total no. of guess took : {total_guess} ')

# i = 0
# while True : 
#     user= input('Enter your username : ')
#     password = input("Enter your password : ")
#     if user == 'admin' and password == '1234' :
#         print("Login successful!!!!")
#         break
#     else :
#         print("Invalid credentials, Try again")
#     i+=1
#     if i ==3 :
#         print("Too many failed attempts!!!!") 
#         break   

# import random
# num1 = random.randint(1,30)
# num2 = random.randint(1,30)
# print(num1)
# print(num2)
# while True : 
#     guess = int(input("Enter the multipication of the two number : "))
#     if guess == num1*num2 :
#         print("correct")
#         stoppp = input("Do you want to stop? ").strip().lower()
#         if stoppp == 'stop' :
#           break
#         num3 = random.randint(1,30)
#         num4 = random.randint(1,30)
#         print(num3)
#         print(num4)
#         guess = int(input("Enter the multipication of the two number : "))
#         if guess == num3*num4 :
#          print("correct")
#          stoppp = input("Do you want to stop? ").strip().lower()
#          if stoppp == 'stop' :
#           break
        

        
#     else :
#         print("Incorrect, try again")
#     stoppp = input("Do you want to stop? ").strip().lower()
#     if stoppp == 'stop' :
#         break


# while True : 
#     n = input("Enter a number (or exit): ").strip().lower()

#     if n == "exit":
#         break

#     n = int(n)
#     i = 2
#     prime = True

#     if n <= 1:
#         prime = False
#     else:
#         while i < n:
#             if n % i == 0:
#                 prime = False
#                 break
#             i += 1

#     if prime:
#         print("The number is prime.")
#     else:
#         print("The number is not prime.")
    

# secret_word = 'liverpool'
# while True : 
#     guess = input("Enter your guess word (or quit): ").strip().lower()
#     if secret_word== guess :
#         print('congratulations!!!!, you guessed the word')
#         break
#     elif guess == 'quit' :
#         break
#     else :
#         print("Incorrect!! Try again")   


# goodluck_count= 0
# while True :
#     name = input("Enter name : ").strip().lower()
#     if name == 'good luck' :
#         goodluck_count+=1
#         print('you typed good luck',goodluck_count,'times')
    
#     if goodluck_count== 3 :
#         break 


current_floor = 1
while True : 

    user_input = input("Enter the floor you want to go to: ")

    if not user_input.isdigit():
        print("Please enter a valid integer floor number.")
       

    destination_floor = int(user_input)
    if destination_floor == 0 :
        print("Goodbye")
        break
    elif destination_floor>current_floor :
        print("Moving upward")
        current_floor= destination_floor
        print("Now you are in floor no. ",current_floor)
    elif destination_floor<current_floor :
        print("Moving downward")
        current_floor= destination_floor
        print("Now you are in floor no. ",current_floor)
      
    
                
    
    



             
      
    
    
    
        
    
