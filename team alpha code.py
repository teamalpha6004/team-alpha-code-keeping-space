import random
import time
import webbrowser as wb
print("Welcome to Boredom App")

resume="y"

score=1

queSet=0
question={1:["Que 1","Que 2","Que 3","Que 4","Que 5","Que 6","Que 7","Que 8"],
          2:["Que 11","Que 12","Que 13","Que 14","Que 15","Que 16","Que 17","Que 8"],
          3:["Que 21","Que 22","Que 23","Que 24","Que 25","Que 26","Que 27","Que 8"]
          }

ans={1:["ans1","ans2","ans3","ans4","ans5","ans6","ans7","ans8"],
     2:["ans1","ans2","ans3","ans4","ans5","ans6","ans7","ans8"],
     3:["ans1","ans2","ans3","ans4","ans5","ans6","ans7","ans8"]}

# set1=["Que 1","Que 2","Que 3","Que 4","Que 5","Que 6","Que 7","Que 8"]
# set2=["Que 1","Que 2","Que 3","Que 4","Que 5","Que 6","Que 7","Que 8"]
# set1ans=["ans1","ans2","ans3","ans4","ans5","ans6","ans7","ans8"]
# set2ans=["ans1","ans2","ans3","ans4","ans5","ans6","ans7","ans8"]

calnum=50
lolimit=0
uplimit=100
step=0
user_response = 0

numset=0

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
        print("2. Take up a Quiz")
        print("3. Guess the Number Game")
        print("4. Memory Game")
        
        gameChoice=int(input("Enter your choice: "))
        
        if gameChoice==1:
            print("List of Games")
            
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
                
        elif gameChoice==3:
            print("Select a number in your mind, select greater than, lesser than or equal symbols for the questions asked")

            while user_response!= "=":
                step=step+1
                
                calnum = int((uplimit+lolimit)/2)
                user_response = input("is your num :"+ str (calnum)+ " ")
                
                if user_response == '<' :
                    uplimit = calnum
                    
                if user_response == '>' :
                    lolimit = calnum
                    
            print("your num is " + str(step) + " steps")
            
        elif gameChoice==4:
            
            numset=numset+1
            score=0
            numlist={1:[9,300,12,30,80,70,87,96,89,10],
                     2:[1,2,4,5,7,4,2,1,3,5],
                     3:[],
                     4:[],
                     5:[],}
            
            userlist=[0,0,0,0,0,0,0,0,0,0]
            
            print("memorize the sequence")
            time.sleep(1)
            
            for num in range (10):
                
                print(numlist[numset][num])
                time.sleep(1)
                
            for e in range(50):
                print("\\"*e)
               
            for j in range(10):
                userlist[j]=int(input("number"+str(j+1)+":"))
                if userlist[j]==numlist[numset][j]:
                   score=score+1
    #score
            if score<=3:
                print("you need to eat soaked almoonds")
            elif score<=5:
                print("you need practice but still good")
            elif score<=8:
                print("good job,nice memory")
            else:
                print("very good memory,ithink you eat soaked almods everyday")
                  
            print("your score is :"+str(score))
            
            time.sleep(3)
        
                            
    elif choice==3:     
            print("categories")
            category=int(input("Enter category:"))
            if category==1:
                wb.open("https://youtu.be/uN1EJJvJYYM")
            elif category==2:
                wb.open_new_tab("https://github.com/TechClubPro/Python-Reference-Codes/blob/master/BoredomApp.py")
        
        
        
    elif choice==4:
        break
    
    
print("Thanks for using our app")
print("Meet you again!!")
            
                
            
            
            