import random
import time
import webbrowser as wb
import datetime
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
        print("5. quiz 1")
        print("6. quiz 2")
        print("7. quiz 3")
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
        
        elif gameChoice == 5:
            score1=0
            print("you have 4 seconds to ans the question")
            time. sleep(2)
            
            t1=datetime.datetime.now()
            print("A. bhubaneswarB.mumbaiC.dehli.dubai")
            time.sleep(2)
            ans=input("what is the capital of odisha")
            
            if ans=="a"or ans=="A":
                print("correct ans")
                score1=score1+1
            else:
                print("wrong ans")
                score1=score1-1
            t2= datetime.datetime.now()
            
            delay=t2-t1
            
            if delay.total_seconds()>5:
                print("sorry you took more time ,so 'bye'")
                print("time taken"+str(delay.total_seconds()))
            else:
                print("you are quick")
                
        elif gameChoice==6:
            score2=0
            print("are you bored of sitting at home, take a quiz")
            time.sleep(1)
            
            print("question1")      
            print("which is the largest bone in human body?")
            print("A.scull: B.femur: C.sineal cod D.ribs")
            ans=input("whats your answer:")
            time.sleep(5)
            if ans=="c" or "C":
                print("correct ans")
                score2=score2+1
            else:
                print("wrong ans")
                score2=score2-1
            # question 1 over
                
            print("question2")      
            print("in which city was jesus born?")
            print("A.medina: B.mecca: C.bethlehem D.istanbul")
            time.sleep(5)
            if ans=="c" or "C":
                print("correct ans")
                score2=score2+1
            else:
                print("wrong ans")
                score2=score2-1
            # question 2 over
                
            print("question3")      
            print("in which country is cape town located?")
            print("A.south africa: B.mongolia: C.chaina D.USA")
            ans=input("whats your answer:")
            time.sleep(5)
            if ans=="a" or "A":
                print("correct ans")
                score2=score2+1
            else:
                print("wrong ans")
                score2=score2-1
            # question 3 over
                
            print("question4")      
            print("what food gets its name from the hugarian herdsmen who used to eat it??")
            print("A.mussaka: B.souvalki: C.goulash D.tazatazaki")
            ans=input("whats your answer:")
            time.sleep(5)
            if ans=="c" or "C":
                print("correct ans")
                score2=score2+1
            else:
                print("wrong ans")
                score2=score2-1
            # question 4 over
                
            print("question 5")      
            print("which holly wood flim director feld to france in 1978?")
            print("A.steven pielberg: B.roman polanciki: C.martin scorese D.chirtopher nolan")
            ans=input("whats your answer:")
            time.sleep(5)
            if ans=="B" or "b":
                print("correct ans")
                score2=score2+1
            else:
                print("wrong ans")
                score2=score2-1
            # question 5 over
                
            print("question6")      
            print("which north afroican city has a name which merans'white house'in spanish?")
            print("A.mellia: B.casabalanca: C.ceuta D.ogoobu")
            ans=input("whats your answer:")
            time.sleep(5)
            if ans=="b" or "B":
                print("correct ans")
                score2=score2+1
            else:
                print("wrong ans")
                score2=score2-1
            # question 6 over
                
            print("question7")      
            print("a geyser is what?")
            print("A. hot spring: B.flight: C.water fall D.a helicopter")
            ans=input("whats your answer:")
            time.sleep(5)
            if ans=="a" or "A":
                print("correct ans")
                score2=score2+1
            else:
                print("wrong ans")
                score2=score2-1
            # question 7 over
                
            print("question8")      
            print("glaglow is a city in which european country")
            print("A.england: B.ireland: C.iceland D.sctchland")
            ans=input("whats your answer:")
            time.sleep(5)
            if ans=="d" or "D":
                print("correct ans")
                score2=score2+1
            else:
                print("wrong ans")
                score2=score2-1
            # question 8 over
                
            print("question9")      
            print("into which lifeless sea does the river jordon flow?")
            print("A.dead sea: B.red sea: C.black sea D.caspian sea")
            ans=input("whats your answer:")
            time.sleep(5)
            if ans=="a" or "A":
                print("correct ans")
                score2=score2+1
            else:
                print("wrong ans")
                score2=score2-1
            # question 9 over
                
            print("question10")      
            print("ameerica is song about which of these?")
            print("A.a death: B.a marriage: C.an alcohlic D.a road trip")
            ans=input("whats your answer:")
            time.sleep(5)
            if ans=="d" or "D":
                print("correct ans")
                score2=score2+1
            else:
                print("wrong ans")
                score2=score2-1
            # question 10 over
                
            
                
            print("your score is"+str(score2))
            if score2==10:
                print("you are inteligent")
            elif score2>5:
                print("you are but litle studys will work")
            elif score2<3:
                print("you need lots of studys")
            elif gameChoice==7:
                score=0

                print("question1")      
                print("who did the monkeys tell to cheer to cheer up in'daydream bealiver'?")
                print("A.sleepy jenny: B.SLEEPY janet C.SLEEPY JON D.sleepy jean")
                ans=input("whats your answer:")
                time.sleep(5)
                if ans=="d" or "D":
                    print("correct ans")
                    score=score+1
                else:
                    print("wrong ans")
                    score=score-1
                # question 1 over
                    
                print("question2")      
                print("first indian bowler to take hatrick in odi match?")
                print("A.kapil dev: B.harbhan singh: C.mohmad shami D.chetan sharma")
                ans=input("whats your answer:")
                time.sleep(5)
                if ans=="D" or "d":
                    print("correct ans")
                    score=score+1
                else:
                    print("wrong ans")
                    score=score-1
                # question 2 over
                    
                
                print("question3")      
                print("which state is the highest time winner of santosh trophy in football?")
                print("A.goa: B.kerala: C.west bengal D.uttar pradesh")
                ans=input("whats your answer:")
                time.sleep(5)
                if ans=="C" or "c":
                    print("correct ans")
                    score=score+1
                else:
                    print("wrong ans")
                    score=score-1
                # question 3 over
                    
                print("question4")      
                print("who was the player to be first ODI captain for india ?")
                print("A.kapil dev: B.ravi shastri: C.ajit wadekar D.sunil gavaskar")
                ans=input("whats your answer:")
                time.sleep(5)
                if ans=="D" or "d":
                    print("correct ans")
                    score=score+1
                else:
                    print("wrong ans")
                    score=score-1
                # question 4 over
                
                print("question5")      
                print("first indian cricketer to score 75 tests and centuries?")
                print("A.kapil dev: B.sachin tendulkar: C.sourav ganguly D.sunil gavaskar")
                ans=input("whats your answer:")
                time.sleep(5)
                if ans=="A" or "a":
                    print("correct ans")
                    score=score+1
                else:
                    print("wrong ans")
                    score=score-1
                # question 5 over
                
                print("question6")      
                print("who is captain of team india?")
                print("A.kapil dev: B.sachin tendulkar: C. virat kohli D.mahendra singh dhoni")
                ans=input("whats your answer:")
                time.sleep(5)
                if ans=="A" or "a":
                    print("correct ans")
                    score=score+1
                else:
                    print("wrong ans")
                    score=score-1
                # question 6 over
                
                print("question7")      
                print("where is the 2020 IPL foing to be?")
                print("A.UAE: B.India: C. Usa D.Canada ")
                ans=input("whats your answer:")
                time.sleep(5)
                if ans=="A" or "a":
                    print("correct ans")
                    score=score+1
                else:
                    print("wrong ans")
                    score=score-1
                # question 7 over
                    
                print("question8")      
                print("which is the latest windows version?")
                print("A.2010 B.2013 C.2020  D.2019 ")
                ans=input("whats your answer:")
                time.sleep(5)
                if ans=="A" or "a":
                    print("correct ans")
                    score=score+1
                else:
                    print("wrong ans")
                    score=score-1
                # question 8 over
                print("question9")      
                print("what is a colouring book?")
                print("A. a drawing in which we need to colour : B.a paper: C. food D. company ")
                ans=input("whats your answer:")
                time.sleep(5)
                if ans=="A" or "a":
                    print("correct ans")
                    score=score+1
                else:
                    print("wrong ans")
                    score=score-1
                # question 9 over
                
                print("question10")      
                print(" which is india's famous plane?")
                print("A. air india B. spice jet C.indigo  D. quatar")
                ans=input("whats your answer:")
                time.sleep(5)
                if ans=="A" or "a":
                    print("correct ans")
                    score=score+1
                else:
                    print("wrong ans")
                    score=score-1
                # question 10 over
                
                print("your score is"+str(score))
                if score==10:
                    print("you are inteligent")
                elif score>5:
                    print("you are but litle studys will work")
                elif score<3:
                    print("you need lots of studys")
    elif choice==3:     
        print("Showing you subjects")
        print("1. Science")
        print("2. Maths")
        print("3. hindi")
        print("4. english")
        h=int(input("enter subject number: "))
        if h==1:
            print("Showing you Science")
            wb.open("https://www.youtube.com/channel/UCKuZYmp_lpsIN4WkRB4bECw?view_as=subscriber")
            print("showing you site of this channel")
            wb.open("https://sites.google.com/view/infoon-techhome")
        elif h == 2:
            print("Showing you Maths")
            wb.open("https://www.youtube.com/watch?v=i7AFqlaZmZA")
        elif h == 3:
            print("Showing you hindi")
            wb.open("https://www.youtube.com/watch?v=cWxgxRhUgR8")
        elif h == 4:
            print("showing you english")
            wb.open("https://www.youtube.com/watch?v=Cy1J9cos9FI")
    elif choice==4:
        break
    
    
print("Thanks for using our app")
print("Meet you again!!")          