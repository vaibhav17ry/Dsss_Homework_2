import random


def function_Random(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)

def function_operation():
    return random.choice(['+', '-', '*'])


def function_Calculation(n1, n2, o):
    Cal = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: final_result = n1 * n2
    return Cal, final_result

def math_quiz():
    Points = 0
    Total_questions = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for i_ in range(total_questions):
        n1 = function_Random(1, 10); n2 = function_Random(1, 10); o = function_operation()

        PROBLEM, ANSWER = function_C(n1, n2, o)
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
