#Quiz game

print ("Welcome to my computer parts quiz")
playing = input ("Do you wanna play? ").lower() #.lower function converts the input to lowercase

if playing != "yes":
    quit ()

score = 0

print ("\nOkay, let's play then!\n")

answer = input ("What does CPU stands for? ").lower()
if answer == "central processing unit": #conditional
    print ("Correct!\n") #Condition met = true
    score += 1 #adds 1 to the score variable if this condition is met. Could also be "score = score + 1"
else:
    print ("Uh-oh, that's wrong!\n") #condition not met = false

answer = input ("What does GPU stands for? ").lower()
if answer == "graphics processing unit":
    print ("Very good\n")
    score += 1
else:
    print ("Incorrect!\n")

answer = input ("What does PSU stands for? ").lower()
if answer == "power supply unit":
    print ("Yeah!\n")
    score += 1
else:
    print ("Nope!\n")

answer = input ("What does RAM stands for? ").lower()
if answer == "random access memory":
    print ("Brilliant!\n")
    score += 1
else:
    print ("Totally wrong!\n")

answer = input ("What is called the peripheral you use to type? ").lower()
if answer == "keyboard":
    print ("THAT'S A BINGO!!\n")
    score += 1
else:
    print ("I'm afraid not.\n")

answer = input ("What is does SSD stands for? ").lower()
if answer == "solid state drive":
    print ("GREAT!\n")
    score += 1
else:
    print ("I don't think so...\n")

answer = input ("What is does OS stands for? ").lower()
if answer == "operating system":
    print ("Excellent\n")
    score += 1
else:
    print ("No, it's not.\n")

answer = input ("What is called the peripheral you use to control the cursor? ").lower()
if answer == "mouse":
    print ("""Thank god you're not stupid enough to call it "mice".\n""") #used three double quotation marks to be able to include " and ' inside the string
    score += 1
else:
    print ("Nah!\n")

answer = input ("Is Linux an operating system? ").lower()
if answer == "yes":
    print ("You got it!\n")
    score += 1
else:
    print ("Unfortunately you're incorrect.\n")

answer = input ("Is MAC OS indicated for gaming? ").lower()
if answer == "no":
    print ("Thank god! I was about to beat you to death!\n")
    score += 1
else:
    print ("I'm calling an ambulance to pickup your corpse by the time I finish beating you to death using a baseball bat. \n")

print ("You got " + str(score) + " questions correct!\n") #converting the variable "score" to string to be able to concatenate with another string
print ("That is " + str((score/10)*100) + "%.") #calculating percentage of the score