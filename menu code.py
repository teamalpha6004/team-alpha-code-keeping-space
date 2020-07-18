#jokes_list['']
print("Welcome to the Boredom app")
print("please choose an option from the given list")
print("1. jokes")
print("2. games")
print("3. learning platform")
print("4. exit")
user_choose=int(input("choose option: "))
    
while user_choose != 4:
    if user_choose == 1:
        print("inside jokes")
    #user_choose=int(input("choose option: "))
    elif user_choose == 2:
        print("inside games")
    elif user_choose == 3:
        print("inside learning platform")
    user_choose=int(input("choose option: "))
print("thankyou for using the app")