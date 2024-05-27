import random

# Constants
OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 5

def generate_problem():

    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = f"{left} {operator} {right}"
    answer = eval(expr)
    return expr, answer

def math_quiz():
    wrong = 0
    print("Press enter to start!")
    input()
    print("..............................................!")

    for i in range(TOTAL_PROBLEMS):
        expr, answer = generate_problem()
        while True:
            guess = input(f"Problem {i + 1}: {expr} = ")
            if guess == str(answer):
                print("Correct!")
                break
            else:
                print("Incorrect. Try again.")
                wrong += 1

    print("...................................................................")
    print("Nice work!")
    print(f"You had {wrong} wrong attempts.")

# Run the quiz
math_quiz()
