
# import random
# import time

# jokes=["abc","pqr","xyz","hij","opqr"]

# while True:
#     num=random.randint(0,4)
    
#     print("New Random Number: "+ str(num))
#     print(jokes[num])
#     time.sleep(3)

import time

questions = ["kbkbds",
             "nknlnl",
             "sdfafewe"]

Answers=["a","b","a"]

for i in range(3):
    
    if i==1:
        break
    print(questions[i])
    ans= input("your Answer: ")
    if ans == Answers[i]:
        print("Correct Answer")
    else:
        print("Wrong")
        
    time.sleep(2)

