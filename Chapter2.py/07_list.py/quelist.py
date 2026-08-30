# numbers = [10,20,30,50,40]
# print(numbers)

#1]
# fruits = ["Apple","Banana","Mango","Orange"]
# print(fruits)
# print(fruits[0])
# print(fruits[2])
# print(fruits[3])

#2]for loop
# fruits = ["Apple","Banana","Mango","Orange"]

# for fruit in fruits:
#     print(fruit,end=", ")

#3]Lists Q3 — append()
# num = [10,20,30]
# num.append(40)
# num.append(50)
# print(num)

#4]Q4 — insert()
# num = [10,20,30,40]
# num.insert(2,50)
# print(num)

#5]remove()
# num = [10,30,40,50]
# num.remove(30)
# print(num)

#Q6 — pop()
# num = [10,30,50,60]
# num.pop(2)
# print(num)

#Q7]sort()
# numbers = [40, 10, 50, 20, 30]
# numbers.sort()
# numbers.sort(reverse=True)
# print(numbers)

#Q8]reverse()
# numbers = [10, 20, 30, 40, 50]
# numbers.reverse()
# print(numbers)

#Q9]len(),sum()
# numbers = [15, 25, 35, 45, 55]
# print("Count:",len(numbers))
# print("Sum",sum(numbers))

#Q10]min(),max()
# numbers = [35, 12, 78, 4, 56, 23]
# print("Smallest number:",min(numbers))
# print("Largest number:",max(numbers))

#Q11]IN operator
# fruits = ["Apple","Mango","Orange","Banana"]
# print("Mango" in fruits)
# print("Apple" in fruits)

#Q12]index()
# fruits = ["Apple","Mango","Orange","Banana"]
# print(fruits.index("Banana"))

#Q13]clear()
# num = [10,20,30,40]
# num.clear()
# print(num)

#Q14]List Slicing
# list = [10,20,30,50,60]
# print(list[0:3])

#Q15]List slicing with step
# list = [10,20,30,40,50,60,90]
# print(list[1:5:2])

#Q16]Reverse List using slicing
# list = [10,20,30,50,60]
# print(list[::-1])

#Q17]copy()
# fruits = ["Apple", "Mango", "Banana"]
# new_fruits = fruits.copy()
# print(fruits)
# print(new_fruits)

#Q18]List + for + if,even numbers
# numbers = [10,15,20,25,30,35,40,45,50]
# for number in numbers:
#     if number % 2 == 0:
#         print(number,end=" ")

#Q19]Odd Numbers
# numbers = [10,15,20,25,30,35,40,45,50]
# for number in numbers:
#     if number % 2 != 0:
#         print(number,end=" ")

#Q20]sum of even numbers
# numbers = [10,15,20,25,30,35,40,45,50]
# total = 0
# for number in numbers:
#     if number % 2 == 0:
#         total += number
        
# print("Even Sum=",total)

#Q21]count even numbers
# numbers = [10,15,20,25,30,35,40,45,50]
# count = 0
# for number in numbers:
#     if number % 2 == 0:
#         count += 1

# print("Total Even numbers:",count)
    
#Q22]largest number
# numbers = [10,20,40,60,70,90,30]
# largest = numbers[0]

# for number in numbers:
#     if number > largest:
#         largest = number

# print("Largest Number=",largest)

#Q23]smallest number
# numbers = [10,13,28,45,11,9,3,45,56]
# smallest = numbers[0]

# for number in numbers:
#     if number < smallest:
#         smallest = number
        
# print("Smallest Num=",smallest)

#Q24]second largest number
# numbers = [10,20,45,43,50,65,42]
# largest = numbers[0]
# second = 0

# for number in numbers:
#     if number > largest:
#         second = largest
#         largest = number
        
# print("Second Largest=",second)

#Q25]duplicate number find
# numbers = [10,20,34,20,34,30,30,20,40,50,55,50]
# unique = []

# for number in numbers:
#     if number not in unique:
#         unique.append(number)
# print(unique)

#Q26]count duplicate number
# numbers = [10,20,10,30,20,10]
# print("20 appears",numbers.count(20),"Times")

#Q27]positive and negative numbers
# numbers = [10, -5, 20, -8, 30, -2, 40]

# for number in numbers:
#     if number > 0:
#         print(number,"= Positive number")
#     else:
#         print(number,"= Negative number")

#Q28]sum of positive numbers
# numbers = [10, -5, 20, -8, 30, -2, 40]
# total = 0

# for number in numbers:
#     if number > 0:
#         total += number
        
# print("Positive Sum=",total)

#Q29]Positive and negative count
# numbers = [10, -5, 20, -8, 30, -2, 40]
# positive = 0
# negative = 0

# for number in numbers:
#     if number > 0:
#         positive += 1
#     else:
#         negative += 1

# print("Positive Count=",positive)
# print("Negative Count=",negative)

#Q30]list average
# numbers = [10, 20, 30, 40, 50]
# total = sum(numbers)
# count = len(numbers)
# print("Average The List=",total/count)