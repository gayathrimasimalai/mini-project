print ("welcome to quiz game!")

gamer = input("You want to start the game?")
if gamer.lower() != "yes":
    exit()
print("Lets GO")

score=0

question = input("What is the world's longest river?")
if question.lower()  == "amazon river":
    print("Good Job")
    score = score+1
else:
    print("You Failed")



question = input("What is the largest continent?")
if question.lower()  == "asia":
    print("Good Job")
    score = score+1
else:
    print("You Failed")
    
question = input("What is the majority of the Earth covered by?")
if question.lower()  == "ocean":
    print("Good Job")
    score = score+1
else:
    print("You Failed")
    
question = input("Africa is home to how many deserts?")
if question.lower()  == "three":
    print("Good Job")
    score = score+1
else:
    print("You Failed")
    
question = input(" Where is the driest place on Earth?")
if question.lower()  == "antarctica":
    print("Good Job")
    score = score+1
else:
    print("You Failed")
    
print("Your Score "+ str(score))