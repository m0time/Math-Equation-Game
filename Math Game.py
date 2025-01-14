import random #needed to create random equations

rangelimit = [-15, 15] #range the equations will be within for simplicity sake
operators = ['+', '-', '/', '*'] #operators that can be chosen by the equation generator

def random_num_gen():
    #this function creates the random digits. makes it easy to grab new random integers
    return random.randint(rangelimit[0], rangelimit[1]) 

def random_operator():
    #similar to the random number generator other than the fact that it is choosing from our list of operators
    return random.choice(operators)

def replacement_process():
    #this is used to mask one integer allowing the equation to become a problem to the user
    return 'x'

def construction():
    score = 0 #keeps track of score
    for question_num in range(1, 11):  #loops 10 times before game ends 
        num_to_replace = random.randint(0, 2)  

        #creation of both numbers and operators
        number_1 = random_num_gen()
        number_2 = random_num_gen()
        operator = random_operator()

        #tells code what to do based on operator to get the last number in equation
        if operator == '+':
            number_3 = number_1 + number_2
        elif operator == '-':
            number_3 = number_1 - number_2
        elif operator == '/':
            while number_2 == 0:
                number_2 = random_num_gen()
            number_3 = round(number_1 / number_2, 2)  # Rounded for cleaner division output (simplify user choice)
        elif operator == '*':
            number_3 = number_1 * number_2
        
        #necessary to create 'x' as a filler for one of the numbers
        choices_to_replace = [number_1, number_2, number_3]
        #chosen one becomes the 'answer' as the user will be trying to solve this 'x'
        answer = choices_to_replace[num_to_replace]

        #returning all as string to enable simple print statements for the user to see the equation
        if num_to_replace == 0:
            equation_final = f"x {operator} {number_2} = {number_3}"
        elif num_to_replace == 1:
            equation_final = f"{number_1} {operator} x = {number_3}"
        elif num_to_replace == 2:
            equation_final = f"{number_1} {operator} {number_2} = x"

        print(f"Question {question_num}: Solve the equation: {equation_final}")

        #try method used for the user to enter the solution
        try:
            user_input = float(input("Enter your answer: "))
            if user_input == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect! The correct answer was: {answer}")
        except ValueError:
            print(f"Invalid input! The correct answer was: {answer}")

    print(f"\nYou completed the quiz! Your total score is: {score}/10")


#prints out the main function and keeps everything within a function
construction()
