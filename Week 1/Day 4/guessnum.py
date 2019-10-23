# #### Pair Problem #1
#
# For your Metis application you wrote a program that let's
# the user guess a number between 1 and 100.
# Can you write a program that does the reverse.
# Write a function that takes in a number between 1 and 100 and tries to guess it.
# Based on whether a guess is larger or smaller than the input number,
# the code would come up with a new guess until it gets it right.
# def guess(13) would return "I got it right in 8 tries."


# def guessnum(num):
#     import random
#     count = 0
#     secret_number_list = []
#     while num in secret_number_list:
#         secret_number_list.append(*random.sample(range(100), 1))
#         for number in secret_number_list:
#             if number in secret_number_list:
#                 pass
#             else:
#                 count += 1
#     print(f'I guessed it in {count} tries.')


def guessnum2(num):
    """
    Returns the number of tries the computer takes (without replacement) to randomly guess
    an integer from 0-100.
    :param num: int
    :return: tries: int
    """
    import random
    guess_list = [i for i in range(1, 101)]  # generates a list of integers from 1-100
    tries = 0
    guess = random.choice(guess_list)  # randomly selects a number from guess_list
    while guess != num:
        guess_list.remove(guess)  # removes the randomly guessed number from the list
        guess = random.choice(guess_list)  # makes another random guess
        tries += 1
    print(f'I got it right in {tries} tries.')


def guessnum3(num):
    """
    This is a binary search algorithm. (This is the more efficient one)
    O log(N) - log base 2
    N = len(list)
    k - times to halve
    :param num:
    :return:
    """
    low = 1  # lowest number we could guess
    high = 101  # highest number plus 1
    tries = 0

    # use a for loop instead of a while
    # guarantees we won't get stuck
    for _ in range(100): # we can replace the i with an '_' because we don't care about using the index
        my_guess = (low+high) // 2  # this is the mean rounded down
        tries += 1
        if my_guess == num:
            return tries  # breaks loop
        elif my_guess > num:
            high = my_guess   # this readjusts the higher portion of the halving algorithm
        else:  # when your guess is lower than the number
            low = my_guess + 1  # readjusts the lower portion of the halving algorithm

print(guessnum3(25))