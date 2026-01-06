# Sorting assignment
# Dario Androsevic
# December 3rd 2025

numbers = [-11, 1, 43, 55, 100, 34]

print("Original list:", numbers, "\n")

for i in range(len(numbers) - 1):
    lowest_index = i
    lowest_number = numbers[i]
    print(f"Sorting index {i}: {numbers[i]}")
    print(f"lowest_number = {lowest_number}, lowest_index = {lowest_index}\n")

    for j in range(i + 1, len(numbers)):
        current_number = numbers[j]
        print("First Comparison:" if j == i+1 else "Next Comparison:")
        print("-----------------")
        print(f"current_number = {current_number}")
        print(f"lowest_number = {lowest_number}")
        print(f"lowest_index = {lowest_index}")
        if current_number < lowest_number:
            print(f"current_number is lower than lowest_number! Updating lowest_number and lowest_index")
            lowest_number = current_number
            lowest_index = j
            print(f"New Values: lowest_number = {lowest_number}, lowest_index = {lowest_index}\n")
        else:
            print('"current_number is not lower than lowest_number, move on"\n')

    if lowest_index != i:
        print(f"Swap: numbers[{i}] ({numbers[i]}) <-> numbers[{lowest_index}] ({numbers[lowest_index]})")
        numbers[i], numbers[lowest_index] = numbers[lowest_index], numbers[i]

    print("List after swap:", numbers, "\n")

print("Sorted list:", numbers)
