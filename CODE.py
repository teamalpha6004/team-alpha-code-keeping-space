import random
import time


print("Welcome to Boredom App")

resume="y"

score=1

queSet=0
question={1:["1. Who Is This Personility ","2. Who Is This Personility","3. Who Is This Personility","4.Who Is This Personility","5. Who Is This Personility","6. Who Is This Personility","7. Who Is This Personility","8. Who Is This Personility","9. Who Is This Personility","10. Who Is This Personility"],
          2:["1. Who Is This Personility","2. Who Is This Personility","3. Who Is This Personility","4. Who Is This Personility","5. Who Is This Personility","6.Who Is This Personility","7. Who Is This Personility","9. Who Is This Personility","9. Who Is This Personility","10. Who Is This Personility"],
          3:["1. Who Is This Personility","2. Who Is This Personility","3. Who Is This Personility","4. Who Is This Personility","5. Who Is This Personility","6. Who Is This Personility","7. Who Is This Personility","8. Who Is This Personility","9. Who Is This Personility","10. Who Is This Personility"]}
          

ans={1:["ans1","ans2","ans3","ans4","ans5","ans6","ans7","ans8","ans9","ans10"],
     2:["ans1","ans2","ans3","ans4","ans5","ans6","ans7","ans8","ans9","ans10"],
     3:["ans1","ans2","ans3","ans4","ans5","ans6","ans7","ans8","ans9","ans10"]}

 #set1=["Que 1","Que 2","Que 3","Que 4","Que 5","Que 6","Que 7","Que 8"]
 #set2=["Que 1","Que 2","Que 3","Que 4","Que 5","Que 6","Que 7","Que 8"]
 #set1ans=["ans1","ans2","ans3","ans4","ans5","ans6","ans7","ans8"]
 #set2ans=["ans1","ans2","ans3","ans4","ans5","ans6","ans7","ans8"]

while resume=="y":
    print("We have different options for You:")
    print("1. Jokes")
    print("2. Game")
    print("3.Learning Platform")
    print("4. Exit")
    
    choice= int(input("Enter your choice: "))
    
    
    jokes=["Joke 1","Joke 2","joke 3","joke 4","joke 5"]
    
    # while choice!=4:
        
    if choice==1:
        print(" Welcome to jokes Module:")
        
        for i in range(2):
            num = random.randint(0,4)
            
            print(jokes[num])
            time.sleep(2)
        resume=input("Do you wish to continue? y/n")
        
    elif choice==2:
        print("Welcome to Game module")
        print("Choose your option:")
        print("1. Suggestions on interesting Games")
        print("2. Play game with me")
        
        gameChoice=int(input("Enter your choice: "))
        
        if gameChoice==1:
            print("List of Games")
            print ("1. Ponginator "
                   "2. Hanky Panky"
                   "3. Ball Drop"
                   "4. Breakfast Scramble "
                   "5. Elephant March")
        elif gameChoice==2:
            queSet=queSet+1
            
            if queSet==4:
                queSet=1
            
            for que in range(5):
                            
                print(question[queSet][que])
                option=input("Your Answer: ")
                
                if option==ans[queSet][que]:
                    print("Correct Answer")
                    score=score+2
                else: 
                    print("Wrong Answer!!")
                    score=score-1
            print("Your score is: "+ str(score))
            
            if score>=3:
                print("you are genius!!")
            
            elif score<3 and score>=1:
                print("You know little bit of History")
            else:
                print("Do you sleep in History class!!")
                
            
            
        
        
        
    elif choice==4:
        break
    
    
print("Thanks for using our app")
print("Meet you again!!")
            