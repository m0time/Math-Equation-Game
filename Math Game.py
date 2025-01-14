import random

rangelimit = [-15, 15]
operators = ['+', '-', '/', '*']

def random_num_gen():
    return random.randint(rangelimit[0], rangelimit[1])

def random_operator():
    return random.choice(operators)

def replacement_process():
    return 'x'

def construction():
    score = 0
    for question_num in range(1, 11):
        num_to_replace = random.randint(0, 2)

        number_1 = random_num_gen()
        number_2 = random_num_gen()
        operator = random_operator()

        if operator == '+':
            number_3 = number_1 + number_2
        elif operator == '-':
            number_3 = number_1 - number_2
        elif operator == '/':
            while number_2 == 0:
                number_2 = random_num_gen()
            number_3 = round(number_1 / number_2, 2)  # Rounded for cleaner division output
        elif operator == '*':
            number_3 = number_1 * number_2

        choices_to_replace = [number_1, number_2, number_3]
        answer = choices_to_replace[num_to_replace]

        if num_to_replace == 0:
            equation_final = f"x {operator} {number_2} = {number_3}"
        elif num_to_replace == 1:
            equation_final = f"{number_1} {operator} x = {number_3}"
        elif num_to_replace == 2:
            equation_final = f"{number_1} {operator} {number_2} = x"

        print(f"Question {question_num}: Solve the equation: {equation_final}")

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

construction()
