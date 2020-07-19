
import random
import time

jokes=["1.What do you call a dad joke that falls on its head? A: A dud pun.",
       "2.On Thanksgiving, why did the turkey cross the table? A: To get to the other sides",
       "3.What do you call a mermaid on a roof? A: Aerial.",
       "4.What does a highlighter say when it answers the phone? A: Yello!"]

while True :
   
    num=random.randint(0,3)
    
    print (" Printing Joke "+ str (num))
    print(jokes[num])
    time.sleep(3)