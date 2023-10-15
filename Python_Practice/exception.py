try:
    num = int(input("Enter a number to divdie: "))
    den = int(input("Enter a number to divide by: "))
    result = num/den
    print(result)
except ZeroDivisionError as e:
    print(e)
    print ("You can't divide by zero")
except ValueError as e:
    print(e)
    print("Enter only numbers")
except Exception as e:
    print(e)
    print ("Something went wrong")