
# ########################################################################### #
# #                                                                         # #
# #   42: computorv1                                                        # #
# #                                                                         # #
# #   by dFleury                                                            # #
# #                                                                         # #
# ########################################################################### #

from class_term import Term

from utils_colors import *
from utils_math import *

# #############################################################################


class Solver:

    #########   CONSTRUCTOR    ##################

    def __init__(self, _dico_degree_coef):

        self.dico_degree_coef = _dico_degree_coef
        self.degree = decimal.Decimal("0")
        self.a = decimal.Decimal("0")   # * x^2
        self.b = decimal.Decimal("0")   # * x^1
        self.c = decimal.Decimal("0")   # * x^0
        self.delta = None


        for degree, coef in self.dico_degree_coef.items():
            if coef != 0:
                if degree > self.degree:
                    self.degree = degree
                if degree == 0:
                    self.c = coef
                elif degree == 1:
                    self.b = coef
                elif degree == 2:
                    self.a = coef


    #########   METHODS    ##################



    def print_poly_degree(self):
        print_f_line("Polynomial degree", f"{self.degree}", YELLOW, YELLOW+BOLD)


    def init_delta(self):
        self.delta = self.b*self.b - 4*self.a*self.c





    def solve_degree_1(self):
        print_f_line("INFO", f"The equation is of the form \"{BOLD}c + bx = 0{RESET+CYAN}\",  with b not equal to 0.", CYAN+BOLD, CYAN)
        print_f_line("INFO", f"The unique solution is \"{BOLD}x = -c/b{RESET+CYAN}\"", CYAN+BOLD, CYAN)
        print_f_line("SOLUTION", f"X = {-self.c} / {self.b}", BRIGHT_GREEN, BRIGHT_GREEN)

        reduce_frac_str = get_str_reduce_fraction(-self.c, self.b)
        if reduce_frac_str:
            print_f_line("Reduced fraction", f"  = {reduce_frac_str}", BRIGHT_GREEN, BRIGHT_GREEN)

        result = -self.c / self.b

        if result == 0:
            result = 0  ## pour eviter -0E+5

        print_f_line("", f" {str_equal_or_approx(result)} {result}", BRIGHT_GREEN, BRIGHT_GREEN)





    def solve_degree_2_delta_null(self):
        a = self.a
        b = self.b
        c = self.c
        delta = self.delta

        print_f_line("Polarity of the discriminant",  f"Δ  = 0,  therefore this equation has a unique solution:", YELLOW, YELLOW)

        print_f_line("SOLUTION",  f"x = -b / 2a",                           BRIGHT_GREEN, BRIGHT_GREEN)
        print_f_line("",          f"  = {-b} / (2 * {a})",                  BRIGHT_GREEN, BRIGHT_GREEN)
        print_f_line("",          f"  = {-b} / {2*a}",                      BRIGHT_GREEN, BRIGHT_GREEN)

        reduce_frac_str = get_str_reduce_fraction(-b, 2*a)
        if reduce_frac_str:
            print_f_line("Reduced fraction", f"  = {reduce_frac_str}", BRIGHT_GREEN, BRIGHT_GREEN)

        result = -b /(2*a)
        print_f_line("",          f" {str_equal_or_approx(result)} {result}", BRIGHT_GREEN, BRIGHT_GREEN)




    def solve_degree_2_delta_positiv(self):
        a = self.a
        b = self.b
        c = self.c
        delta = self.delta
        sqrt_delta = my_sqrt(self.delta)
        str_equal_for_sqrt_delta = str_equal_or_approx(sqrt_delta)

        print_f_line("Polarity of the discriminant",  f"Δ  > 0,  therefore this equation has two distinct solutions:",  YELLOW, YELLOW)

        print_f_line("SOLUTION 1",  f"x1 = (-b + √Δ) / 2a",                         BRIGHT_GREEN, BRIGHT_GREEN)
        print_f_line("",            f"   = ({-b} + √{delta}) / (2 * {a})",          BRIGHT_GREEN, BRIGHT_GREEN)
        print_f_line("",            f"   = ({-b} + i√{delta}) / {2 *a}",            BRIGHT_GREEN, BRIGHT_GREEN)
        print_f_line("",            f"  {str_equal_for_sqrt_delta} ({-b} + {sqrt_delta}) / (2 * {a})",      BRIGHT_GREEN, BRIGHT_GREEN)
        print_f_line("",            f"  {str_equal_for_sqrt_delta} {-b + sqrt_delta} / {2*a}",              BRIGHT_GREEN, BRIGHT_GREEN)

        reduce_frac_str = get_str_reduce_fraction(-b + sqrt_delta, 2*a)
        if reduce_frac_str:
            print_f_line("Reduced fraction", f"   = {reduce_frac_str}",      BRIGHT_GREEN, BRIGHT_GREEN)

        result = (-b + sqrt_delta) / (2*a)
        print_f_line("",            f"  {str_equal_or_approx(result)} {result}",        BRIGHT_GREEN, BRIGHT_GREEN)



        print_f_line("SOLUTION 2",  f"x2 = (-b - √Δ) / 2a",                         BRIGHT_GREEN, BRIGHT_GREEN)
        print_f_line("",            f"   = ({-b} - √{delta}) / (2 * {a})",          BRIGHT_GREEN, BRIGHT_GREEN)
        print_f_line("",            f"   = ({-b} - √{delta}) / {2 *a}",              BRIGHT_GREEN, BRIGHT_GREEN)
        print_f_line("",            f"  {str_equal_for_sqrt_delta} ({-b} - {sqrt_delta}) / (2 * {a})",  BRIGHT_GREEN, BRIGHT_GREEN)
        print_f_line("",            f"  {str_equal_for_sqrt_delta} {-b - sqrt_delta} / {2*a}",          BRIGHT_GREEN, BRIGHT_GREEN)

        reduce_frac_str = get_str_reduce_fraction(-b - sqrt_delta, 2*a)
        if reduce_frac_str:
            print_f_line("Reduced fraction", f"   = {reduce_frac_str}",      BRIGHT_GREEN, BRIGHT_GREEN)

        result = (-b - sqrt_delta) / (2*a)
        print_f_line("",            f"  {str_equal_or_approx(result)} {result}",        BRIGHT_GREEN, BRIGHT_GREEN)




    def solve_degree_2_delta_negativ(self):
        a = self.a
        b = self.b
        c = self.c
        delta = self.delta
        sqrt_minus_delta = my_sqrt(-self.delta)

        print_f_line("Polarity of the discriminant",  f"Δ  < 0,  therefore this equation has {RED}no real solutions{YELLOW}, but two complex conjugate solutions:", YELLOW, YELLOW)

        real_part = -b / decimal.Decimal('2') / a
        if real_part == 0:
            real_part = ""

        imaginary_part = sqrt_minus_delta/decimal.Decimal('2')/a

        print_f_line("COMPLEX SOLUTION 1",  f"x1 = (-b + i√-Δ) / 2a",                   BRIGHT_GREEN, BRIGHT_GREEN)
        print_f_line("",                    f"   = ({-b} + i√{-delta}) / (2 * {a})",    BRIGHT_GREEN, BRIGHT_GREEN)
        print_f_line("",                    f"   = ({-b} + i√{-delta}) / {2 *a}",       BRIGHT_GREEN, BRIGHT_GREEN)
        print_f_line("",                    f"  {str_equal_or_approx(sqrt_minus_delta)} ({-b} + {sqrt_minus_delta} i) / {2 *a}",  BRIGHT_GREEN, BRIGHT_GREEN)
        print_f_line("",                    f"  {str_equal_or_approx(imaginary_part)} {real_part} + {imaginary_part} i",        BRIGHT_GREEN, BRIGHT_GREEN)


        print_f_line("COMPLEX SOLUTION 2",  f"x2 = (-b - i√-Δ) / 2a",                   BRIGHT_GREEN, BRIGHT_GREEN)
        print_f_line("",                    f"   = ({-b} - i√{-delta}) / (2 * {a})",    BRIGHT_GREEN, BRIGHT_GREEN)
        print_f_line("",                    f"   = ({-b} - i√{-delta}) / {2*a}",        BRIGHT_GREEN, BRIGHT_GREEN)
        print_f_line("",                    f"  {str_equal_or_approx(sqrt_minus_delta)} ({-b} - {sqrt_minus_delta} i) / {2 *a}",  BRIGHT_GREEN, BRIGHT_GREEN)
        print_f_line("",                    f"  {str_equal_or_approx(imaginary_part)} {real_part} - {imaginary_part} i",        BRIGHT_GREEN, BRIGHT_GREEN)

