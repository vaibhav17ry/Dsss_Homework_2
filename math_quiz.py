import random


def function_Random(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)

def function_operation():
    return random.choice(['+', '-', '*'])

def function_Calculation(num_1, num_2, operation):
    Cal = f"{num_1} {operation} {num_2}"
    if operation == '+': a = num_1 + num_2
    elif operation == '-': a = num_1 - num_2
    else: final_result = num_1 * num_2
    return Cal, final_result

def math_quiz():
    Points = 0
    Total_questions = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for i in range(total_questions):
        num_1 = function_Random(1, 10); num_2 = function_Random(1, 10); operation = function_operation()

        PROBLEM, ANSWER = function_C(num_1, num_2, operation)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            points += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {points}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
