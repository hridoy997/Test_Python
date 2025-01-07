# user input, while loop

# How to take user input with prompt
# Use of 'while' loop. 
# Use of 'break', 'continue' keywords

while True:
    age = input("Please enter your age, 'q' to quit: ")
    
    if age.lower() == 'q':
        break

    print("You entered your age to be " + age)

    age = int(age)
    if age <= 0:
        print('Sorry, wrong input, try again..')
        continue

    elif age < 18:
        print("Sorry, you are too young for a DL")
    elif age > 70:
        print("Sorry you are too old for a DL")
    else:
        print("Congrats! You are eligible for a DL")

print('Thanks for using our program.')
