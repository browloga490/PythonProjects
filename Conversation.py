import time

delay = time.sleep

print ("Welcome to Logan's interactive text simulation")

name = input("What is your name? ")

while name == "":
    print ("Sorry, I didn't hear you.")
    name = input("What is your name? ")

if name == "":
    print ("Sorry, I didn't hear you.")
else:
    print ("Hi", name + ".", "My name is I.T.S.")

Q1 = input("How are you today?(Good/Okay/Bad) ")

while Q1 == "":
    print ("Sorry, I didn't hear you.")
    Q1 = input("How are you today?(Good, Okay, Bad) ")

if Q1 == "Good":
    print ("I'm glad to hear that you are doing well.")
elif Q1 == "Okay":
    print ("Alright. That's nice to hear.")
elif Q1 == "Bad":
    print ("Oh, I'm sorry to hear that.")
else:
   print (Q1 + "?", "What does that even mean? Just... nevermind.")
   
def form_2():
    a = input("If you were stranded on an island, name one thing that you would like to be stuck with?")
    while a == "":
        print("I couldn't here, please speak up.") or ("Sorry didn't catch that.") or ("What was that?") or ("Pardon me?")
        a = input("If you were stranded on an island, name one thing that you would like to be stuck with?")
    print ("I think I would want to be stuck on an island with", a, "to", name + ".")

    b = input("Do you want to play a game?(Yes/No)")
    
    while b == "":
        print("I couldn't here, please speak up.") or ("Sorry didn't catch that.") or ("What was that?") or ("Pardon me?")
        b = input("Do you want to play a game?(Yes/No)")

    if b == "No":
        b_sub1 = input("Are you sure?(Yes/No)")
        while b_sub1 == "":
            print("I couldn't here, please speak up.") or ("Sorry didn't catch that.") or ("What was that?") or ("Pardon me?")
            b_sub1 = input("Are you sure?(Yes/No)")
        if b_sub1 == "No":
            print("Awesome! :)")
        elif b_sub1 == "Yes":
            print("Well... to bad. :)")
        else:
            print("Sorry",name + ","," I don't understand what",b_sub1, "means...")
            delay(2)
            print("... i'm just going to assume that you want to play.")
            

    print("[*INITIALIZING GAME START UP SEQUENCE*]")
    delay(5)
    print("[*RETRIEVING DATA FILES*]")
    delay(1.5)
    print("...")
    delay(1.5)
    print("...")
    delay(1.5)
    print("[*DATA FILES RETRIEVED*]")
    delay(1)
    print("[*COMPILING DOCUMENTS*]")
    delay(1.5)
    print("...")
    delay(1.5)
    print("[*DOCUMENTS COMPILLED*]")
    delay(1)
    print("[*JUCIFYING PLOT*]")
    delay(1.5)
    print("...")
    delay(1.5)
    print("...")
    delay(1.5)
    print("...")
    delay(1.5)
    print("[*PLOT JUCIFIED*]")
    delay(1)
    print("[*FEEDING CHICKENS*]")
    delay(1.5)
    print("...")
    delay(1.5)
    print("...")
    delay(1.5)
    print("...")
    delay(1.5)
    print("...")
    delay(1.5)
    print("[*CHICKENS FED... BUT AT WHAT COST*]")
    delay(1.5)
    print("...")
    delay(1.5)
    print("[*(-___<->)*]")
    delay(2)
    print("...")
    delay(1.5)
    print("[*CALIBRATING MONSTERS*]")
    delay(1.5)
    print("...")
    delay(1.5)
    print("...")
    delay(1.5)
    print("[*MONSTERS CALIBRATED*]")
    delay(1)
    print("[*ENJOYING SATISFYING RESULTS*]")
    delay(1.5)
    print("...")
    delay(1.5)
    print("...")
    delay(1.5)
    print("[*FEELS GOOD*]")
    delay(1)
    print("[*GAME INITIALIZATION COMPLETE*]")
    delay(2)
    import Slither
    c = input("Hey... you still there?(Yes/No)")
    while c == "":
        print("Pardon me,",name,"?")


form_2()

