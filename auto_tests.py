
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
from collections import defaultdict

from computor import handle_entry
from utils_colors import *
from utils_math import *

# #############################################################################


def print_auto_test_header(title, style=BG_WHITE+BLUE):
    title_width: int = 68
    print("\n\n\n")
    print(f"{style}###############################################################################################{RESET}")
    print(f"{style}##                                                                                           ##{RESET}")
    print(f"{style}##                  {title:<{title_width}}     ##{RESET}")
    print(f"{style}##                                                                                           ##{RESET}")
    print(f"{style}###############################################################################################{RESET}")


def print_auto_test_comment(title, style=BRIGHT_CYAN+BOLD+ITALIC):
    print(f"\n\n   {style}{title}{RESET}")




def auto_tests_errors():
    print_auto_test_header("ERRORS (syntax...)", BG_WHITE+RED)
    print_auto_test_comment("## TEST ERRORS: Empty input, no '=', or nothing on the left/right side of '=':")
    handle_entry("")
    handle_entry("5*X^0 + 4*x^1 - 9.3*X^2")
    handle_entry("5*X^0   =      4*x^1   =  9.3*X^2")
    handle_entry("=")
    handle_entry("5*X^0 + 4*x^1 - 9.3*X^2=")
    handle_entry("=5*X^0 + 4*x^1 - 9.3*X^2")
    print_auto_test_comment("## TEST ERRORS: Invalid Exponent:")
    handle_entry("42 ∗ X^-1 = 42 * x^1")
    handle_entry("42 ∗ X^0 = 42 * x^-3")
    handle_entry("42 ∗ X^2.2 = 42 * x^1")
    handle_entry("5*X^X  +  9.3*X^2=0")
    handle_entry("2^^X^1  =  0")
    handle_entry("X = X^")
    print_auto_test_comment("## TEST ERRORS: Syntax error:")
    handle_entry("5*X^0 + 4*x^1 - 9.3*X^2=xxxxxxxxxxxxx")
    handle_entry("5*X^0 + 4*x^1 - 9.3*X^2=abcdfefgsmldfkmslkdf")
    handle_entry("2*X^1  =  2   2")
    print_auto_test_comment("## TEST ERRORS: Syntax error before [*-^]:")
    handle_entry("*2*X^1  =  0")
    handle_entry("2*X^1  =  * 2")
    handle_entry("2*X^1  =  *0")
    handle_entry("X = ^2")
    handle_entry("X = 5^2")
    print_auto_test_comment("## TEST ERRORS: Syntax error after [*-^]:")
    handle_entry("2*X^1 * =  0")
    handle_entry("2+X^1 + =  0")
    handle_entry("2-X^1 - =  0")
    print_auto_test_comment("## TEST ERRORS: Syntax error near [*-^]:")
    handle_entry("2**X^1  =  0")
    handle_entry("2++X^1  =  0")
    handle_entry("2--X^1  =  0")
    handle_entry("2*X^1  =  2  + +  2")
    handle_entry("2*X^1  =  2  + *  2")
    handle_entry("2*X^1  =  2  + -  2")
    handle_entry("    X  =  2  - +  2")
    handle_entry("    X  =  2  * +  2")
    handle_entry("    X  =  2  + *  2")
    handle_entry("2*X^1  =  *")
    handle_entry("2*X^1  =  -")
    handle_entry("2*X^1  =  +")
    handle_entry("2*X^1*-3  =  0")
    handle_entry("2*X^1  =  0*")
    handle_entry("X = X^+2")







def auto_tests_degree_greater_than_2():
    print_auto_test_header("polynomial degree > 2", BG_WHITE+RED)
    handle_entry("42 ∗ X^11 = 42")
    handle_entry("-9.3*X^2  +  5*X^0         +  4*x^1*2      +     4*X^2*5*X^3      =      1*X^0")
    handle_entry("8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0")




def auto_tests_degree_0():
    print_auto_test_header("polynomial degree = 0", BG_WHITE+GREEN)
    handle_entry("2 * X^0 = 3 ∗ X^0")
    handle_entry("3=0")
    handle_entry("42 ∗ X^0 = 42 ∗ X^0 ")



def auto_tests_degree_1():
    print_auto_test_header("polynomial degree = 1", BG_WHITE+BLUE)
    handle_entry("5 * X^0 + 4 * X^1 = 4 * X^0")
    handle_entry("5  + 2*X^0          -     3*X^1*3       +     0 * X^2     =   22")
    handle_entry("      3*X^1      =   0")
    handle_entry(" 2+   3*X^1      =   0")
    handle_entry("2 ∗ X^1 = 3 ∗ X^1")



def auto_tests_degree_2_delta_positiv():
    print_auto_test_header("polynomial degree = 2,   Discriminant > 0", BG_WHITE+MAGENTA)
    handle_entry("X^2 = 9")
    handle_entry("5*X^0         +  4*x^1           - 9.3*X^2      =      1*X^0")
    handle_entry("3         +  4*x^1          -  9.3*X^2      =   1*X^0     +     12*x^2")
    handle_entry("5*X^0         +  2*X^1*3       +     9.3*X^2      =   22")
    handle_entry("5  + 2*X^0          -     3*X^1*3       +     X^2*42.2     -10 * X^2     =   22")
    handle_entry("-9.3*X^2  +  5*X^0         +  4*x^1*2      +     3*X^2*2      =      1*X^0   +    2*X^1*3*2   + 5*0*X^4")
    handle_entry("-9.3*X^2  +  5*X^0         +  4*x^1*2      +     4*X^2*5*X^3      =      1*X^0   +    20*X^5" )


def auto_tests_degree_2_delta_0():
    print_auto_test_header("polynomial degree = 2,   Discriminant = 0", BG_WHITE+MAGENTA)
    handle_entry("  x^2   -    4*x   +  4    =   0 ")
    handle_entry("  9*x^2   -    6*x   +   1   =   0 ")
    handle_entry(   "X^2   = 0")
    handle_entry("   3*X^2    =  0")



def auto_tests_degree_2_delta_negativ():
    print_auto_test_header("polynomial degree = 2,   Discriminant < 0", BG_WHITE+MAGENTA)
    handle_entry("X^2 = -9")
    handle_entry(" X^2           +  4*x^1     =      -5")
    handle_entry("42.24*X^0         +          9.3*X^2       =   22")
    handle_entry(" 9.3*X^2  +  5*X^0         +  4*x^1*2      +     3*X^2      =      1*X^0")



def auto_tests_bonus_free_form():
    print_auto_test_header("BONUS: Free Form Entry / Format CheLou", BG_WHITE+BLACK+RAPID_BLINK)
    print_auto_test_comment("## BONUS (Free form):   Sans 'x^0' ni '^1'     (  x^0 = 1    et   x^1 = x  ) :")
    handle_entry("5 + 5*X  =  5*X^1")
    print_auto_test_comment("## BONUS (Free form):   Sans '*'   entre le coef et le 'X'   :")
    handle_entry("3x^2 - 4x + 4x^0 = 8")
    print_auto_test_comment("## BONUS (Free form):   Avec un exposant chelou (mais valide)   :")
    handle_entry("42 ∗ X^4.00000 = 42 * x^1")
    handle_entry("3.0000 * X = 42.00042 * X")
    print_auto_test_comment("## BONUS (Free form):   Avec un '²' au lieu de '^2':")
    handle_entry("9*x² - 6*x + 1 = 0")
    print_auto_test_comment("## BONUS (Free form):   exposants dans le desordre':")
    handle_entry("  2   +      2*X^0    +     2*X²*3    -  2   +   4*X^1*2    +     3*2*X^2.00*2*1       =   -4   -    3*2*X^5     +  x^1  -  3*0*X^42")




def auto_tests_bonus_irreducible_fraction():
    print_auto_test_header("BONUS: Irreducible fraction", BG_WHITE+BLACK+RAPID_BLINK)
    handle_entry("9*x² - 6*x + 1 = 0")
    handle_entry("3x^2 - 4x + 4x^0 = 8")
    handle_entry("  9*x^2   -    6*x   +   1   =   0 ")
    handle_entry("5  + 2*X^0          -     3*X^1*3       +     0 * X^2     =   22")






def auto_tests():
    print_auto_test_header("***** ComputerV1 by dFleury - AUTO TESTS *****", BG_YELLOW+BLACK)
    auto_tests_errors()
    auto_tests_degree_greater_than_2()
    auto_tests_degree_0()
    auto_tests_degree_1()
    auto_tests_degree_2_delta_0()
    auto_tests_degree_2_delta_positiv()
    auto_tests_degree_2_delta_negativ()
    auto_tests_bonus_free_form()
    auto_tests_bonus_irreducible_fraction()
    print_auto_test_header("*************** THE END ***************", BG_YELLOW+BLACK)

    ## add custom tests here:
    # handle_entry("3*X^0 + 3*X^1 + 3*X^2  = 3*X^0 + 3*X^1 + 3*X^2")
    # handle_entry("3.0000 * X^2.0000 = 42 * X")







