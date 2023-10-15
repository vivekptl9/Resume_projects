try:
    num = int(input("Enter a number to divdie: "))
    den = int(input("Enter a number to divide by: "))
    result = num/den
    print(result)
except ZeroDivisionError:
    print ("You can't divide by zero")
except ValueError:
    print("Enter only numbers")
except Exception:
    print ("Something went wrong")