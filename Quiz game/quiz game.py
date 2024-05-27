print("Welcome to my Computer Quiz")
playing = input("Do you want to play? " )
if playing.lower() != "yes":
    quit()
print("Okay lets play: ")  
score=0
answer = input("What does CPU stand for? ").lower() 
if answer == "central processing unit":
    print('correct!')
    score =+1 
else:
    print("Incorrect!")    
answer = input("What does GPU stand for? ").lower()  
if answer == "Graphics processing unit":
    print('correct!')
    score =+1 

else:
    print("Incorrect!")     
answer = input("What does Ram stand for? ").lower()  
if answer == "Random Access Memory":
    print('correct!')
    score =+1 

else:
    print("Incorrect!") 
answer = input("What does PSU stand for? ")  
if answer == "Power supply unit unit":
    print('correct!')
    score =+1 

else:
    print("Incorrect!") 
print("You got " + str(score)+"questions correct")
       
print("You got " + str((score/4)*100 )+ "%")
      
