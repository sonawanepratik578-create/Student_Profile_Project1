print("===========Duplicate Remover===========")

numbers = input("Enter numbers seperated by space:")

numbers = numbers.split()
numbers = [int(number) for number in numbers]

unique_numbers = set(numbers)

original_count = len(numbers)
unique_count = len(unique_numbers)
duplicate_count = original_count - unique_count

if duplicate_count > 0:
    print("Duplicate found")
else:
    print("Duplicate not found")
    
print("Original:",numbers)
print("Unique:",unique_numbers)
print("Original count:",original_count)
print("unique_count:",unique_count)
print("duplicate Count:",duplicate_count)