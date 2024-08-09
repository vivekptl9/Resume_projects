num_1 = (input("Please enter a number between 0 and 100:  "))
if  num_1.isdigit()==False:
    print("Your have not entered integer value")
    num_1 = int(input("Please enter a number between 0 and 100:  "))
elif int(num_1) < 0 or int(num_1) > 100:
    print("Your entered value is out of range")
    num_1 = int(input("Please enter a number between 0 and 100:  "))

num_2 = (input("Please enter a number between 0 and 100:  "))
if num_2.isdigit() == False:
    print("Your have not entered integer value")
    num_2 = int(input("Please enter a number between 0 and 100:  "))
elif int(num_2) < 0 or int(num_2) > 100:
    print("Your entered value is out of range")
    num_2 = int(input("Please enter a number between 0 and 100:  "))

if int(num_2) == int(num_1):
    print("please enter different values of numbers.")
num_1 =int(num_1)
num_2=int(num_2)
if num_1 < num_2:
    for i in range(num_1, num_2+1):
        print(i)
elif num_2<num_1:
    for i in range(num_2,num_1+1):
        print(i)    
