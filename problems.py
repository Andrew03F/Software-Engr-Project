from os import urandom
import random

class Problem:
    def __init__(self, low, high):
        # For now just say each problem has two terms
        # which range from [0, 10)
        self.nums = get_rand_nums(2, low, high)
        self.bins = to_binary(self.nums)
        self.solution = sum(self.nums)
        self.bin_solution = format(self.solution, 'b')

    def __str__(self):
        return f"{self.nums} or {self.bins} = {self.solution} or {self.bin_solution}"

    def test(self):
        guess = input(f"{self.bins[0]} + {self.bins[1]} = ")
        if guess == self.bin_solution:
            print("Correct!")
        else:
            print("Incorrect")

    def test_prompt(self):
        return f"{self.bins[0]} + {self.bins[1]} = "


def get_rand_nums(count, low, high):
    # Initialize the random number generator with a 
    # random number acquired from the os.urandom() method
    random.seed(urandom(1024))
    # Iterator variable is irrelevant, so assign to '_'
    terms = [random.randrange(low, high) for _ in range(count)]
    return terms

def to_binary(terms):
    # format returns a string in the specified format
    # In this case, that is 'b'inary
    return [format(term, 'b') for term in terms]


test = Problem(0, 10)
print(test)
test.test()

