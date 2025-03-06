
# ########################################################################### #
# #                                                                         # #
# #   42: computorv1                                                        # #
# #                                                                         # #
# #   by dFleury                                                            # #
# #                                                                         # #
# ########################################################################### #

import sys
import re
import math
import decimal

from utils_colors import *

# #############################################################################


def my_sqrt(number, precision=decimal.Decimal("0.00001")):

    ###  return math.sqrt(number)    # !!!!!!!!!!!!!!!!!!

    if number < 0:
        raise ValueError("Cannot compute the square root of a negative number.")

    guess = number / decimal.Decimal("2")

    while True:
        better_guess = (guess + number / guess) / decimal.Decimal("2")

        if (int(better_guess) * int(better_guess) == number):
            return int(better_guess)
        if abs(guess - better_guess) < precision:
            return better_guess

        guess = better_guess



def put_num(num):
    num = strip_trailing_zeros(num)
    return str(num)


def strip_trailing_zeros(s):
    try:
        num = float(s)
        if num.is_integer():
            return str(int(num))
        else:
            return str(num)
    except ValueError:
        return s  # si ce n'est pas un nombre


def format_console_str(title, strr, title_style="", str_style=""):
    title_width: int = 29
    return f"  {title_style}{title:>{title_width}}{RESET}  :  {str_style}{strr}{RESET}"

def print_f_line(title, strr, title_style="", str_style=""):
    print(format_console_str(title, strr, title_style, str_style))


def pgcd(a, b):
    ## algorithme d'Euclide:
    while b:
        a, b = b, a % b
    return a

def reduce_fraction(numerator, denominator):
    if denominator == 0:
          return None, None

    if numerator == 0:
        return 0, 1

    common_divisor = pgcd(abs(numerator), abs(denominator))

    reduced_numerator = numerator // common_divisor
    reduced_denominator = denominator // common_divisor

    if reduced_denominator < 0:
        reduced_numerator = -reduced_numerator
        reduced_denominator = -reduced_denominator

    return reduced_numerator, reduced_denominator




def get_str_reduce_fraction(numerator, denominator):



    if denominator == 0:
          return None

    if numerator == 0:
        return None


    if not float(numerator).is_integer():
        return None

    if not float(denominator).is_integer():
        return None

    reduced_numerator, reduced_denominator = reduce_fraction(numerator, denominator)

    if numerator == reduced_numerator:
        return None

    if reduced_denominator == 1:
        return None

    return f"{reduced_numerator} / {reduced_denominator}"


def is_approximate_float(value):
    string_repr = f"{value}"
    float_from_string = float(string_repr)
    return value != float_from_string


def str_equal_or_approx(value):
    if is_approximate_float(value):
        return f"{GREEN+ITALIC}~="
    else:
        return f" ="


