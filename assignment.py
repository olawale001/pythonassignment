# #1 maximum of three number
# def find_maximum(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3

# number1 = float(input("Enter the first number: "))
# number2 = float(input("Enter the second number: "))
# number3 = float(input("Enter the third number: "))

# maximum = find_maximum(number1, number2, number3)
# print("Maximum number is:", maximum)




#2Sum of number
numbers = (8, 2, 3, 0, 7)

total = 0
for i in numbers:
    total += i
print("The sum of numbers: ", total )    



#3Multiply of number
numbers = [8, 2, 3, -1, 7]
result = 1
for num in numbers:
    result *= num
print('Result of nums:', result)  


#4String reverse
sample_string = "1234abcd"
def reverse_string(input_string):
    return input_string[::-1]


reversed_string = reverse_string(sample_string)

print("Original string:", sample_string)
print("Reversed string:", reversed_string)

#5 Factorial number
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

number = int(input("Enter a non-negative integer: "))
print("Factorial of", number, "is:", factorial(number))


#6 Python function to check whether a number falls within a given range

def is_in_range(number, start, end):
    return start <= number <= end

number_to_check = float(input("Enter a number to check: "))
range_start = float(input("Enter the start of the range: "))
range_end = float(input("Enter the end of the range: "))

if is_in_range(number_to_check, range_start, range_end):
    print(number_to_check, "falls within the given range.")
else:
    print(number_to_check, "does not fall within the given range.")



#7 Python function that accepts a string and counts the number of upper and lower case letters.

def count_upper_lower_case(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

sample_string = 'The quick Brow Fox'
upper_count, lower_count = count_upper_lower_case(sample_string)
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)



#8 Python function that takes a list and returns a new list with distinct elements from the first list.
number1 = [1,2,3,3,3,3,4,5]
number2 =[]
for nums in number1:
    if nums not in number2:
         number2.append(nums)
print(number2)

#9 Python function that takes a number as a parameter and checks whether the number is prime or not. 
number_to_check = int(input("Enter a number to check if it's prime: "))
def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

if is_prime(number_to_check):
    print(number_to_check, "is a prime number.")
else:
    print(number_to_check, "is not a prime number.")



#10 Python program to print the even numbers from a given list.

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def print_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    print("Even numbers:", even_numbers)

print_even_numbers(sample_list)



