import unittest
from math_quiz import function_Random, function_operation, function_Calculation


class TestMathGame(unittest.TestCase):

    def test_function_random(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for i in range(1000):  # Test a large number of random values
            rand_num = function_ops(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_operation(self):
        # TODO
        listOps=['+' , '-' , '*' , '/' , '%']
        for i in listOps:
            available_ops = function_ops(random.choice(['+', '-', '*']))
            self.assertTrue(i==available_ops)
        pass

    def test_function_Calculation(self):
            test_cases = [
                (3, 2, '+', '3 + 2', 5),
                (5, 5, '-', '5 - 5', 0),
                (8, 5, '*', '8 * 5', 40),
                (6, 6, '+', '6 + 6', 12)
            ]

            for num_1, num_2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                check_vals = function_Calculation(num_1, num_2, operator)
                self.assertTrue(expected_answer == ANSWER )
                pass

if name == "main":
    unittest.main()
