# Part 1: Your original sarcastic greeting
print("aaaaaaahhhh")
print("what do you want?")

print("Hurry up and Pick what calculations you want to do?")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter the number of your choice (1-5): ")

#Addition
if choice == '1':
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = num1 + num2

    print(result)
    print("Oh my, you can't event figure out simple addition. ridiculous.")

#Subtraction
elif choice == '2':
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = num1 - num2

    print(result)
    print("Geez someone's a slow learner.")

#Multiplication
elif choice == '3':
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = num1 * num2

    print(result)
    print("Oh, look at that. You figured out multiplication.")

#Division
elif choice == '4':
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = num1 /num2

    print(result)
    print("So very stupid.")
        
  
