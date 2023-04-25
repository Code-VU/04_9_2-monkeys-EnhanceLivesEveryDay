def calculateTime():
    
    # This first line is provided for you
    monkey_one = input("Is the first monkey smiling?:  ")
    monkey_two = input("Is the second monkey smiling?: ")

    if (monkey_one == "y" and monkey_two == "y") or (monkey_one == "n" and monkey_two == "n"):
        answer = ("Uh Oh! We're in trouble!")
    elif (monkey_one == "y" and monkey_two == "n") or (monkey_one == "y" and monkey_two == "n"):
        answer = ("Yay! We're going to have a good day!")
    else: answer = ("Yay! We're going to have a good day!")
    print (answer)
        
    # end assignment

## If you want to test locally run > python monkeyCalculator.py

if __name__ == "__main__":
    calculateTime()
    
