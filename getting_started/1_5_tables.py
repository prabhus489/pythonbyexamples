# Another example of operators, looping and printing.
# Guess what the program would do?

number = input("Enter a number: ")
number = int(number)

for num in range(11):
    print(str(num), "*" , str(number), "=", str(num*number))

# So, you guessed what the program did without running them even once

# Do It Yourself
# 1. Make the above number work for till "16" and "20" rows
# 2. Try to input a non-integer and see what is happening
# 3. Fix so that the program does not crashes
