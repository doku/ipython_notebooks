"""CS 61A Presents The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.


######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS>0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return the
    number of 1's rolled.
    
    >>> test_dice = make_test_dice(4,1,3,2,5)
    >>> roll_dice(3, test_dice)
    
    
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    total_score= 0
    total_ones = 0
    for _ in range(num_rolls):
        roll = dice()
        if roll == 1:
            total_ones += 1
        else:
            total_score += roll
    if total_ones != 0:
        return total_ones
    else:
        return total_score


def free_bacon(opponent_score):
    """Return the points scored from rolling 0 dice (Free Bacon)."""
    # BEGIN PROBLEM 2
    """
    >>> free_bacon(15)
    6
    >>> free_bacon(64)
    7
    >>> free_bacon(98)
    10
    """
    digit1 = opponent_score % 10
    digit2 = opponent_score // 10
    return 1 + max(digit1 , digit2)
    # END PROBLEM 2


# Write your prime functions here!
def is_prime(player_score):
    """Return if True if the opponent_score is prime number else return False
    
    >>> is_prime(6)
    False
    >>> is_prime(11)
    True
    >>> is_prime(56)
    False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(0)
    False
    
    """
    counter = 2
    is_prime = True
    if(player_score == 1 or player_score == 0):
        return not is_prime
    if(player_score == counter):
        return is_prime
    else:
        while counter < player_score:
            if(player_score % counter == 0):
                is_prime = False
            counter+=1
        if(is_prime):
            return True
        else:
            return False
            
def generate_primes():
    """Generates list of prime nubmers"""
    prime_list = []
    i = 1
    while i < GOAL_SCORE:
        if(is_prime(i)):
            prime_list.append(i)
        i+=1
    return prime_list  
    

def next_prime(player_score):
    """Return the next prime number
    
    >>> next_prime(11)
    13
    >>> next_prime(3)
    5
    >>> next_prime(17)
    19
    """
    a = generate_primes()
    if player_score in a:
        return a[a.index(player_score)+ 1]
        
def pigs_fly(turn_score, dice_rolled):
    """ 
    The score for a turn is limited to 25 points minus the number of dice rolled.
    
    >>> pigs_fly(25, 3)
    22
    >>> pigs_fly(15 , 6)
    15
    >>> pigs_fly(19, 7)
    18
    >>> pigs_fly(23 , 4)
    21
    
    """
    return min(turn_score , 25 - dice_rolled)
    
def hog_wild(score0, score1):
    """
    If the sum of both players' total scores is a multiple of seven (e.g., 0, 7, 14, 21, 35), 
    then the current player rolls special re-rolling dice. 
    When re-rolling dice are rolled and the outcome is odd, they are rolled again exactly once.
    
    returns True if using special re-rolling dice
    if True call the rerolling function
    
    >>> hog_wild(23, 54)
    True
    >>> hog_wild(15, 13)
    True
    >>> hog_wild(15, 15)
    False
    
    
    """
    return (score0 + score1) % 7 == 0

def swine_swap(score0, score1):
    """
    After the turn score is added, if one of the scores is double the other, then the two scores are swapped.
    
    >>> swine_swap(15, 30)
    (30, 15)
    >>> swine_swap(22, 44)
    (44, 22)
    >>> swine_swap(22, 45)
    (22, 45)
    
    
    """
    return (score1, score0) if ((score0 * 2 == score1) or (score1*2 == score0)) else (score0, score1)    

def pork_chop(dice_swapped):
    """
    A player may choose to roll -1 dice, which scores 1 point for the turn, 
    but swaps the normal six-sided dice with four-sided dice for all subsequent turns. 
    The special re-rolling dice are affected by this rule and will become four-sided as well. 
    The odd re-rolling rule will still apply to the four-sided dice. 
    The next time either player rolls -1 dice, the six-sided dice will be swapped back. 
    Subsequent rolls of -1 dice will continue swapping the dice back and forth.
    
    >>> pork_chop(True)
    False
    >>> pork_chop(False)
    True
    
    
    """
    return False if dice_swapped else True 

def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player. Also
    implements the Hogtimus Prime and When Pigs Fly rules.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    
    >>> test_dice = make_test_dice(4,1,3,2,5, 5, 2, 5,3 ,2,2)
    >>> take_turn(3, 12, test_dice)
    8
    >>> take_turn(0, 29)
    10
    
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    
    
    if(num_rolls == 0):
        score = free_bacon(opponent_score)
    else:
        score = roll_dice(num_rolls,dice)
    if( is_prime(score)):
        score = next_prime(score)
    return pigs_fly(score, num_rolls)
    
    # END PROBLEM 2


def reroll(dice):
    """Return dice that return even outcomes and re-roll odd outcomes of DICE."""
    def rerolled():
        # BEGIN PROBLEM 3
        odd = dice()
        if odd % 2 == 1:
            odd = dice()
        return odd  # Replace this statement
        # END PROBLEM 3
    return rerolled


def select_dice(score, opponent_score, dice_swapped = False):
    """Return the dice used for a turn, which may be re-rolled (Hog Wild) and/or
    swapped for four-sided dice (Pork Chop).

    DICE_SWAPPED is True if and only if four-sided dice are being used.
    
    """
    # BEGIN PROBLEM 4
    dice = six_sided
    if (dice_swapped):
        dice = four_sided
    # END PROBLEM 4
    #if (((score + opponent_score) % 7 == 0) and ((score + opponent_score) != 0 )):
    if(score + opponent_score) % 7 == 0:
        dice = reroll(dice)
    return dice


def other(player):
    """Return the other player, for a player PLAYER numbered 0 or 1.

    """Return the dice used for a turn, which may be re-rolled (Hog Wild) and/or
    1
    >>> other(1)
    0
    """
    return 1 - player


def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    
    Hog wild, pork_chop, swine_swap
    """
    player = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    dice_swapped = False  # Whether 4-sided dice have been swapped for 6-sided
    # BEGIN PROBLEM 5
    # counter = 0
    
    while score0 < goal and score1 < goal:
        #print("player: ", player)
        if player == 0:
            rolls = strategy0(score0, score1)
            if rolls == -1:
                dice_swapped = pork_chop(dice_swapped)
                score0 += 1
            else:
                die = select_dice(score0, score1, dice_swapped)
                score0 += take_turn(rolls, score1, die)
        else:
            rolls = strategy1(score1, score0)
            if rolls == -1:
                dice_swapped = pork_chop(dice_swapped)
                score1 += 1
            else:
                die = select_dice(score1, score0, dice_swapped)
                score1 += take_turn(rolls, score0, die)
        score0, score1 = swine_swap(score0, score1)
        player = other(player)
    # END PROBLEM 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


def check_strategy_roll(score, opponent_score, num_rolls):
    """Raises an error with a helpful message if NUM_ROLLS is an invalid
    strategy output. All strategy outputs must be integers from -1 to 10.

    >>> check_strategy_roll(10, 20, num_rolls=100)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(10, 20) returned 100 (invalid number of rolls)

    >>> check_strategy_roll(20, 10, num_rolls=0.1)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(20, 10) returned 0.1 (not an integer)

    >>> check_strategy_roll(0, 0, num_rolls=None)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(0, 0) returned None (not an integer)
    """
    msg = 'strategy({}, {}) returned {}'.format(
        score, opponent_score, num_rolls)
    assert type(num_rolls) == int, msg + ' (not an integer)'
    assert -1 <= num_rolls <= 10, msg + ' (invalid number of rolls)'


def check_strategy(strategy, goal=GOAL_SCORE):
    """Checks the strategy with all valid inputs and verifies that the
    strategy returns a valid input. Use `check_strategy_roll` to raise
    an error with a helpful message if the strategy returns an invalid
    output.

    >>> def fail_15_20(score, opponent_score):
    ...     if score != 15 or opponent_score != 20:
    ...         return 5
    ...
    >>> check_strategy(fail_15_20)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(15, 20) returned None (not an integer)
    >>> def fail_102_115(score, opponent_score):
    ...     if score == 102 and opponent_score == 115:
    ...         return 100
    ...     return 5
    ...
    >>> check_strategy(fail_102_115)
    >>> fail_102_115 == check_strategy(fail_102_115, 120)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(102, 115) returned 100 (invalid number of rolls)
    """
    # BEGIN PROBLEM 6
    for i in range(goal+ 25):
        for j in range(goal+ 25):
            num_rolls = strategy(i, j)
            check_strategy_roll(i, j, num_rolls)
    return None
    # END PROBLEM 6


# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    """
    # BEGIN PROBLEM 7
    def func(*args):
        avg = 0
        for _ in range(num_samples):
            avg += fn(*args) 
        return avg / num_samples
    
    return func
        
    # END PROBLEM 7


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    # BEGIN PROBLEM 8
    "*** REPLACE THIS LINE ***"
    # END PROBLEM 8


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(4)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        rerolled_max = max_scoring_num_rolls(reroll(six_sided))
        print('Max scoring num rolls for re-rolled dice:', rerolled_max)

    if False:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    "*** You may add additional experiments as you wish ***"


# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 9
    points = free_bacon(opponent_score)
    if is_prime(points):
        points = next_prime(points)
    return 0 if points >= margin else 4  # Replace this statement
    # END PROBLEM 9
check_strategy(bacon_strategy)


def swap_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice when it triggers a beneficial swap. It also
    rolls 0 dice if it gives at least MARGIN points. Otherwise, it rolls
    NUM_ROLLS.
    """
    # BEGIN PROBLEM 10
    
    return 4  # Replace this statement
    # END PROBLEM 10
check_strategy(swap_strategy)


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 11
    "*** REPLACE THIS LINE ***"
    return 4  # Replace this statement
    # END PROBLEM 11
check_strategy(final_strategy)


##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()