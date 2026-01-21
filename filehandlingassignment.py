# challenge 1
# def extract_firstwords() :
#     with open('a.txt') as  f:
#         a = f.readlines()
#         b = []
#         c=[]
#         for i in a :
#             b.append(i.split())
#         for i in b :
#             c.append(i[0])
#         print(c)        
        
# extract_firstwords()

# challenge 2

# with open('a.txt','r') as f1 :
#     a = f1.read()
# with open('c.txt','w') as f2 :
#     for i in a :
#         f2.write(i)  

# challenge 3
# with open('a.txt','r') as f :
#     a = f.readlines()
#     b=[]
#     for i in a :
#       b.append(i.split())
#     print(b)
#     i=0
#     for i in range(len(b)) :
#         print('line', i+1,':',len(b[i]))

# challenge 4
# with open('a.txt','r') as f :
#     a = f.readlines()
#     print(len(a))

# challenge 5
# with open('employyes.txt','r') as f :
#     a = f.readlines()
# with open('management.txt','w') as m :
#     for i in a :
#         if 'python' in i :
#             m.write(i)

# challenge 6
# with open('numbers.txt','r') as n :
#     a = n.readlines()
#     b=[]
#     for i in range(len(a)) :
#         print(a[i])
#         for j in a[i] :
#             if j.isdigit() :
#                 b.append(j)
#     print(b)           
# with open('squared.txt','w') as s:
#     c = []
#     for i in b :
#         c.append(str(int(i)*int(i)))
#     for i in c :
#         s.write(i)  
#         s.write(' ')
             
            
# CHALLENGE 7
# with open('x.txt','a') as n :
#     while True : 
#         message = input('Enter your message(0 for exit) : ')
#         if message =='0' :
#             break
#         n.write(message + '\n')

# challenge 8

# with open('input.txt','r') as f :
#     data = f.readlines()
#     for i in data :
#         print(i.upper())
       
         


        
    
    
         
    

