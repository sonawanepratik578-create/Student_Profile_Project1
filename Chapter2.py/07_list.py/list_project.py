print("==========List Analyzer==========")
numbers = [10, 25, 30, 45, 50, 60]
even_count = 0
odd_count = 0
total = sum(numbers)
count = len(numbers)
average = total/count
largest = max(numbers)
smallest = min(numbers)

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

        
print("Total=",total)
print("Average=",average)
print("Largest num=",largest)
print("Smallest num=",smallest)
print("Even Count=",even_count)
print("Odd Count=",odd_count)