print("====================number analyzer project=================")

n = int(input("Enter your number:"))

even_count = 0
odd_count = 0
even_sum = 0
odd_sum = 0
for i in range(1,n+1):
    if i % 2 == 0:
     even_count = even_count + 1
     even_sum = even_sum + i
     
    else:
        odd_count = odd_count + 1
        odd_sum = odd_sum + i
        
print("Even numbers is:",even_count)
print("Even sum=",even_sum)
print("Odd numbers is:",odd_count)
print("Odd sum=",odd_sum)