import random
eror = "!!! Error !!!"
while True:
    print("\n" + "="*30)
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Exit")
    print("="*30)
    question = input("Choose the game level: ")
    if question.isdigit():
        if int(question) in [1,2,3,4]:
            question = int(question)
        else:
            print("")
            print(eror)
            print("~~~~ Round cannot be zero ~~~~")
            print(eror)
            print("")
            
    else:
        print("")
        print(eror)
        print("~~~~ Please enter a number ~~~~")
        print(eror)
        print("")
        
    if  question == 4:
        print("~"*15)
        print("Goodbye")
        print("~"*15)
        break
    elif    question == 1:
        print("\n" + "="*30)
        print("!!. At this level you have 10 chances to guess .!!")
        print("!!. Rhere should be a distance of 10 from the first number to the second number  .!!")
        print("="*30)
        Back = input("Type 'back' to return to the main page and 'continue' to continue: ")
        Back = Back.lower()
        if Back == "back":
            break
        elif Back == "continue":
            a = int(input("Start number: "))
            b = int(input("End number: "))
            rand = random.randint(a,b)
            c = a - b
            hs = {
                
            }
            if (a+9) == b:
                for _ in [1,2,3,4,5,6,7,8,9,10,11]:
                    if _ == 11:
                        print("~"*20)
                        print("!!! You Lost !!!")
                        print(f"Ai number : {rand}")
                        print("~"*20)
                        break
                    elif _ != 11:
                        print("\n" +"    " + "="*20)
                        print("  "+f"{ _ } guess out of 10 guesses")
                        print("    " + "="*20)
                        guess = int(input(f"guess {_}: "))
                        if guess == rand:
                            print(" ")
                            print("~"*40)
                            print(f"you win!, you number : {guess}, Ai number : {rand}")
                            print("~"*40)
                            print(" ")
                            for num,_ in hs.items():
                                print(f"{num} : {_}")
                            break
                        else:
                            hs[f"num {_}"] = guess
                            if guess > rand:
                                print(f"{_} guess wrong")
                                print(f" you number : {guess}, Smaller!!!!")
                            else:
                                    print(f" you number : {guess}, Bigger!!!!")
            else:
                print("There is no gap of 10 between the selected number")
                
    elif    question == 2 :
        print("\n" + "="*30)
        print("!!. At this level you have 5 chances to guess .!!")
        print("!!. Rhere should be a distance of 10 from the first number to the second number .!!")
        print("="*30)
        Back = input("Type 'back' to return to the main page and 'continue' to continue: ")
        Back = Back.lower()
        if Back == "back":
            break
        elif Back == "continue":
            a = int(input("Stard number: "))
            b = int(input("End number: "))
            rand = random.randint(a,b)
            hs = {
                
            }
            if a+10 == b:
                for _ in [1,2,3,4,5,6]:
                    if _ == 6:
                        print("~"*20)
                        print("!!! You Lost !!!")
                        print(f"Ai number : {rand}")
                        print("~"*20)
                        break
                    elif _ != 6:
                        print("\n" +"    " + "="*20)
                        print("    "+f"{ _ } guess out of 5 guesses")
                        print("    " + "="*20)
                        guess = int(input(f"guess {_}? : "))
                        if guess == rand:
                            print(" ")
                            print("~"*40)
                            print(f"you win!, you number : {guess}, Ai number : {rand}")
                            print("~"*40)
                            print(" ")
                            for num,_ in hs.items():
                                print(f"{num} : {_}")
                            break
                        else:
                            hs[f"num {_}"] = guess
                            if guess > rand:
                                print(f"{_} guess wrong")
                                print(f" you number : {guess}, Smaller!!!!")
                            else:
                                    print(f" you number : {guess}, bigger!!!!")
                else:
                    print("There is no gap of 10 between the selected number")
    elif    question == 3:
        print("\n" + "="*30)
        print("!!. At this level you have 3 chances to guess .!!")
        print("!!. Rhere should be a distance of 10 from the first number to the second number .!!")
        print("="*30)
        Back = input("Type 'back' to return to the main page and 'continue' to continue: ")
        Back = Back.lower()
        if Back == "Back":
            break
        elif Back == "continue":
            a = int(input("Stard number: "))
            b = int(input("End number: "))
            rand = random.randint(a,b)
            hs = {
                
            }
            if a+10 == b:
                for _ in [1,2,3,4]:
                    if _ == 4:
                        print("~"*20)
                        print("!!! You Lost !!!")
                        print(f"Ai number : {rand}")
                        print("~"*20)
                        break
                    elif _ != 4:
                        print("\n" +"    " + "="*20)
                        print("    "+f"{ _ } guess out of 5 guesses")
                        print("    " + "="*20)
                        guess = int(input(f"guess {_}? : "))
                        if guess == rand:
                            print(" ")
                            print("~"*40)
                            print(f"you win!, you number : {guess}, Ai number : {rand}")
                            print("~"*40)
                            print(" ")
                            for num,_ in hs.items():
                                print(f"{num} : {_}")
                            break
                        else:
                            hs[f"num {_}"] = guess
                            if guess > rand:
                                print(f"{_}Guess wrong")
                                print(f" you number : {guess}, smaller!!!!")
                            else:
                                    print(f" you number : {guess}, bigger!!!!")
                else:
                    print("There is no gap of 10 between the selected number")
