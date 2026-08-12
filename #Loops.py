#Loops
#while Loops
# count = 1
# while count <= 5:
#     print("pratik")
#     count += 1
    
# print(count)


# i = 1
# while i <= 5:
#     print(i)
#     i += 1
    
# i = 5
# while i >= 1:
#     print(i)
#     i -= 1


#print 1 to 100

# i = 1
# while i <= 100:
#     print(i)
#     i += 1

#print numbers 100 to 1

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

#multiplication table

# n = 17
# i = 1
# while i <= 10:
#     print(n*i)
#     i += 1

#qes4
# nums = [1,4,9,16,25,36,49,64,81,100]

# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1

# nums = (1,4,9,16,25,36,49,64,81,100)
# x = 64
# i = 0
# while i < len(nums):
#     if (nums[i] == x):
#         print("Found At index:",i)
    
#     i += 1


#Break and continue function
# i = 1
# while i <= 5:
#     print(i)
#     if (i == 3):
#         break
#     i += 1
#     print("end of loop")
    
# i = 0
# while i <= 5:
#     if(i == 3):
#         i += 1
#         continue
#     print(i)
#     i += 1

# i = 0
# while i <= 10:
#     if(i%2 != 0):
#         i += 1
#         continue
#     print(i)
#     i += 1


#FOR loops

# nums = [1, 3, 4, 5, 6, 7]

# for val in nums :
#     print(val)
    
# tup = (1,2,4,6,7)

# for val in tup:
#     print(val)


# string = ["pratik", "rushi", "vikky", "chetan"]

# for name in string:
#     print(name)


#problem 

# nums = [1,4,9,16,25,36,49,64,81,100]

# for val in nums:
#     print(val)
    
    
# found x

# nums = (1,4,9,16,25,36,49,64,81,100,36)

# x = 36
# idx = 0
# for el in nums:
#     if(el == x):
#      print ("number is found at idx", idx)
#      break
#     idx += 1
    
    
#range function 
# for i in range (10):
#     print(i)

# for i in range (1, 10):#(start,stop)
#     print(i)
# for i in range (3,10):
#     print(i)


# for i in range (2,11,2):#(start,stop,step)
#     print(i)

#problems
#1)print 1 to 100 numbers

# for i in range(1,101):
#     print(i)
    
#2)print 100 to 1 numbers 

# for i in range(100, 0, -1):
#     print(i)

#3)multipication table

# n = int(input("enter your number:"))

# for i in range(1,11):
#     print(n*i)

#pass statement
# for i in range(5):
#     pass     #apne margi se ham code ko stop kar dete hai kuch time ke liye
# print("pratik")

#4) print all sum numbers(using while  loop)

# n = 5
# sum = 0
# i = 1
# while i <= n:
#  sum += i
#  i += 1
#  print("the sum of numbers", sum)
 
#5) find the factorial of n numbers(using for loop)
#while loop
# n = 5
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1
#     print("the factorial",fact)


#for loop    
# n = 5 
# fact = 1
# for i in range (1,n+1):
#     fact *= i
#     print("factorial=",fact)

