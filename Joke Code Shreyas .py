# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 15:29:02 2020

@author: DELL
"""

import time



num1 = ["1.What do you call a dad joke that falls on its head? A: A dud pun."]
num2 = ["2.On Thanksgiving, why did the turkey cross the table? A: To get to the other sides"]
num3 = ["3.What do you call a mermaid on a roof? A: Aerial."] 
num4 = ["4.What does a highlighter say when it answers the phone? A: Yello!"]

print ("Thanks For Chooseing Jokes!!")
time.sleep(1.5)
print ("Printing Joke 1")
time.sleep(1.5)
print (num1)
time.sleep(1.5)
print ("Printing Joke 2 ")
time.sleep(1.5)
print (num2)
time.sleep(1.5)
like2 = input("Do you Want To continue ??")
    
if like2 == "No" :
       print("Thank You !!")
       
        
if like2 == "Yes" :
        
    print(num3)
    
    time.sleep(1.5)
    print(num4)
    time.sleep(1.5)    
print ("Sorry We Dont Have More Jokes Avalible !!")
time.sleep(1)    
print("You May Ask more Jokes In next 5 mins .")
       
    
