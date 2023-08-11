# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#Q1
def pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
rows = int(input("Enter the number of rows:  \n"))
pattern(rows)

#Q2
def sum_of_numbers(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i
    return sum
number = int(input("Enter a number: \n"))
print( "Sum is : ", sum_of_numbers(number))

#Q3
def print_name(name):
    for i in range(len(name)):
        print(name[i], end=" ")
        print(" " * (len(name) - i - 1))
name = input("Enter your name: \n")
print_name(name)

#Q4
def reverse_word(word):
    return word[::-1]
word = input("Input  word to reverse: \n")
print(reverse_word(word))

#Q5
def descending_order(number):
    for i in range(number, 0, -1):
        print(i)
number = int(input("Enter range: \n"))
descending_order(number)
print("\n")

#Q6
def multiples_of_5():
    for i in range(1, 11):
        print(5 * i)
multiples_of_5()

#Q7
def print_multiples(limit_number, target_number, max_display_on_screen):

  limit_number = int(input("Enter the limit number: "))
  target_number = int(input("Enter the target number: "))
  max_display_on_screen = int(input("Enter the maximum display count: "))

print_multiples(limit_number, target_number, max_display_on_screen)










