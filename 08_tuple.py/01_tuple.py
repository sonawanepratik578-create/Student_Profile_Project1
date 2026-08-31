print("=============Tuple Analyzer Project=============")

numbers = (10, -5, 20, 30, -8, 40, 50)

count = len(numbers)
total = sum(numbers)
average = total / count
largest = max(numbers)
smallest = min(numbers)

positive_count = 0
negative_count = 0

for number in numbers:
    if number > 0:
        positive_count += 1
    else:
        negative_count += 1

print("Total =", total)
print("Average =", average)
print("Largest =", largest)
print("Smallest =", smallest)
print("Positive Count =", positive_count)
print("Negative Count =", negative_count)