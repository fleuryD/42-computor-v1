
# ########################################################################### #
# #                                                                         # #
# #   42: computorv1                                                        # #
# #                                                                         # #
# #   by dFleury                                                            # #
# #                                                                         # #
# ########################################################################### #

import sys
#import re
#import math
from collections import defaultdict

from class_equation import Equation
#from class_term import Term
from class_solver import Solver

from utils_colors import *
from utils_math import *
from auto_tests import *

# #############################################################################



def handle_entry(txt: str):


    try:

        ## Creer l'objet Equation à partir de l'entrée
        equa = Equation(txt)
        equa.print_entry()
        equa.format_entry_and_check_syntax_errors()


        ## Splitter Gauche et droite du "="
        equa.set_left_and_right_str()
        # equa.print_left_and_right_str()  #

        ## Splitter les termes (à gauche et à droite)
        equa.set_left_and_right_terms()
        # equa.print_left_and_right_terms_strs() #

        ## Splitter les termes en facteurs
        equa.print_terms_factors()
        equa.print_terms_factors_simplified()

        ## Passer les termes de droite à gauche
        equa.pass_right_terms_to_left()
        equa.print_right_to_left()

        ## Trier par exposant
        equa.left_terms.sort(key=lambda term: term.degree)
        equa.print_sorted_by_exponents()

        ## Create  'dico_degree_coef'  and print "Reduced form"
        equa.create_dico_degree_coef()
        equa.print_exponenent_regrouped_from_dico_degree_coef()
        equa.print_reduced_form_from_dico_degree_coef()





        ## Create  Solver object from 'dico_degree_coef'
        solver = Solver(equa.dico_degree_coef)
        solver.print_poly_degree()


        ## if  DEGREE > 2
        if solver.degree > 2:
            print_f_line("WARNING", f"The polynomial degree is greater than 2. Sorry, I can't solve it" , BRIGHT_CYAN, BRIGHT_CYAN)
            return

        ## if  DEGREE == 0
        if solver.degree == 0:
            if (solver.c != 0):
                print_f_line("SOLUTION", f"The equation has no solution.", BRIGHT_GREEN, BRIGHT_GREEN)
            else:
                print_f_line("SOLUTION", f"The equation is always true (every X in R is a solution)", BRIGHT_GREEN, BRIGHT_GREEN)
            return

        ## if  DEGREE == 1
        if solver.degree == 1:
            solver.solve_degree_1()
            return


        ## DEGREE = 2


        solver.init_delta()
        print_f_line("Discriminant (Δ = b² -4ac)", f"Δ  =  {solver.b}²  -  4 * {solver.a} *  {solver.c}")
        print_f_line("",  f"Δ  =  {solver.delta}" )


        if solver.delta > 0:
            solver.solve_degree_2_delta_positiv()
        elif solver.delta < 0:
            solver.solve_degree_2_delta_negativ()
        else:
            solver.solve_degree_2_delta_null()


    except ValueError as e:
        print(e)







def main():
    try:
        if len(sys.argv) == 2 and sys.argv[1] == "auto":
            auto_tests()
            sys.exit(0)
        elif len(sys.argv) != 2:
            print(f"{RED}ERROR: One and only one argument expected{RESET}")
        else:
            try:
                handle_entry(sys.argv[1])

            except ValueError as e:
                print(f"Erreur xxxxxxxxxxxxxxxxxxxxxxxx: {e}")
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
