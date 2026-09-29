try:
    num_1 = int(input("Enter a number: "))
    print("The first number is ", num_1)
    num_2 = int(input("Enter another number: "))
    print("The second number is ", num_2)
    result = num_1 / num_2
    print("The result of the division is", result)
except ValueError:
    print("That wasn't a valid number")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
except Exception as ex:
    print("Exception: ", ex)
else:
    print("No exceptions")
finally:
    print("This will execute no matter what")