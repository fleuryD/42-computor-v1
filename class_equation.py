
# ########################################################################### #
# #                                                                         # #
# #   42: computorv1                                                        # #
# #                                                                         # #
# #   by dFleury                                                            # #
# #                                                                         # #
# ########################################################################### #

import re # module pour les expressions régulières

from class_term import Term

from utils_colors import *
from utils_math import *

# #############################################################################


def _split_terms(str):
    # Ajouter un espace devant chaque + ou - qui n'est pas précédé par un ^ ou un *
    modified_equation = re.sub(r'(?<![\^\*])([+-])', r' \1', str)
    # Diviser la chaîne modifiée par les espaces
    termsStr = modified_equation.split(" ")

    terms = []
    for termStr in termsStr:
        if termStr == "":
            continue
        term = Term(termStr)
        terms.append(term)

    return terms


# #############################################################################


class Equation:

    #########   CONSTRUCTOR    ##################

    def __init__(self, input_str):

        self.input_str = input_str
        self.str = input_str # !!! unused
        self.degree = None

        self.terms = []

        self.left_str = "VIDE"
        self.right_str = "VIDE"

        self.left_terms = []
        self.right_terms = []

        self.dico_degree_coef = {}







    #########   METHODS    ##################

    def format_entry_and_check_syntax_errors(self):

        if self.input_str is None or self.input_str == "":
            raise ValueError(format_console_str("SYNTAX ERROR", f"Empty input", BOLD+RED, RED))

        ##  trouver les parties où des nombres sont séparés par des espaces
        regex = r'\d+\s+\d+'
        matches = re.findall(regex,  self.input_str )
        if matches:
            for match in matches:
                raise ValueError(format_console_str("SYNTAX ERROR", f"Syntax Error found near {YELLOW}\"{match}\"", BOLD+RED, RED))

        ##  SYNTAX ERROR : Forbidden char (autre que "0123456789.xX+-*∗^= ")
        regex = r'[^0123456789.xX+\-*∗^= ²]'
        match = re.findall(regex,  self.input_str )
        if match:
            raise ValueError(format_console_str("SYNTAX ERROR", f"Forbidden Char  {YELLOW}'{match[0]}'", BOLD+RED, RED))

        ##  format   self.input_str  (space and case)
        self.input_str =  self.input_str.replace(" ", "").replace("x", "X").replace("∗", "*").replace("²", "^2")

        ##  trouver les '*', '+' et '-' qui ne sont pas suivies d'un chiffre ou d'un 'X'
        regex = r'[*+-](?![\dX])'
        matches = re.finditer(regex, self.input_str)
        incorrect_parts = [match.group() for match in matches]
        if incorrect_parts:
            raise ValueError(format_console_str("SYNTAX ERROR", f"Syntax Error found after {YELLOW}\"{incorrect_parts[0]}\"", BOLD+RED, RED))

        ##  trouver les '*' qui ne sont pas précédés d'un chiffre ou d'un 'X'
        regex = r'(?<![0-9X])\*'
        matches = re.finditer(regex, self.input_str)
        incorrect_parts = [match.group() for match in matches]
        if incorrect_parts:
            raise ValueError(format_console_str("SYNTAX ERROR", f"Syntax Error found before {YELLOW}\"{incorrect_parts[0]}\"", BOLD+RED, RED))

        ##  trouver les '^' qui ne sont pas précédés d'un 'X'
        regex = r'(?<!X)\^'
        matches = re.finditer(regex, self.input_str)
        incorrect_parts = [match.group() for match in matches]
        if incorrect_parts:
            raise ValueError(format_console_str("SYNTAX ERROR", f"Syntax Error found before {YELLOW}\"{incorrect_parts[0]}\"", BOLD+RED, RED))

        ## Repace aX by a*X
        regex = r'(\d)(X)'
        self.input_str  = re.sub(regex, r'\1*\2',  self.input_str )

        ## SYNTAX ERROR :
        if "XX" in self.input_str:
            raise ValueError(format_console_str("SYNTAX ERROR", f"Syntax Error found near  {YELLOW}\"XX\"", BOLD+RED, RED))
        if "++" in self.input_str:
            raise ValueError(format_console_str("SYNTAX ERROR", f"Syntax Error found near  {YELLOW}\"++\"", BOLD+RED, RED))
        if "^+" in self.input_str:
            raise ValueError(format_console_str("SYNTAX ERROR", f"Syntax Error found near  {YELLOW}\"^+\"", BOLD+RED, RED))








    # #     set  self.right_str  and  self.left_str
    # #     throw an error if there is not 1 and only one '='
    # #     throw an error if self.right_str  or  self.left_str are empty
    def set_left_and_right_str(self):
        # print("--set_left_and_right_str--")
        if '=' not in self.input_str:
            raise ValueError(format_console_str("SYNTAX ERROR", f"There is no '='", BOLD+RED, RED))

        if self.input_str.count('=') > 1:
            raise ValueError(format_console_str("SYNTAX ERROR", f"There are {YELLOW+repr(self.input_str.count('='))+RED} '='", BOLD+RED, RED))



        self.left_str, self.right_str = self.input_str.split('=')

        if self.right_str is None or self.right_str == "":
            raise ValueError(format_console_str("SYNTAX ERROR", f"There's nothing on the right side of '='", BOLD+RED, RED))
        if self.left_str is None or self.left_str == "":
            raise ValueError(format_console_str("SYNTAX ERROR", f"There's nothing on the left side of '='", BOLD+RED, RED))


    def set_left_and_right_terms(self):
        # print("--set_left_and_right_terms--")
        self.left_terms = _split_terms(self.left_str)
        self.right_terms = _split_terms(self.right_str)

        if self.left_terms is None or self.right_terms is None:
            # !!!! n'arrive j'amais ??? on a raise une erreur avant ??????????
            print(RED + "ERROR:    Invalid exponent"  + RESET)
            return


    def pass_right_terms_to_left(self):
        for term in self.right_terms:
            term.coefTotal *= -1
            self.left_terms.append(term)
        self.right_terms = []


    def create_dico_degree_coef(self):
        self.dico_degree_coef = {}

        # Parcourir la liste des termes et accumuler les sommes des coefficients
        for term in  self.left_terms:
            if term.degree in self.dico_degree_coef:
                self.dico_degree_coef[term.degree] += term.coefTotal
            else:
                self.dico_degree_coef[term.degree] = term.coefTotal





    #########   PRINT METHODS    ##################


    def print_entry(self):
        print("\n")
        if self.input_str is None or self.input_str == "":
            print_f_line("Entry", "(EMPTY)", "", BG_BRIGHT_WHITE+BLACK)
            return
        print_f_line("Entry", self.input_str, "", BG_BRIGHT_WHITE+BLACK)




    def print_left_and_right_str(self):
        print_f_line("Trim and split L/R", f"{BG_WHITE+BLACK}{self.left_str}{RESET+YELLOW}  =  {BG_WHITE+BLACK}{self.right_str}")



    def print_left_and_right_terms_strs(self):

        left_str = ""
        for term in self.left_terms:
            if left_str != "":
                left_str += " + "
            left_str += f"{BG_WHITE+BLACK}[ {term.str} ]{RESET}"

        right_str = ""
        for term in self.right_terms:
            if right_str != "":
                right_str += " + "
            right_str += f"{BG_WHITE+BLACK}[ {term.str} ]{RESET}"

        print_f_line("Terms (strs)", f"{left_str}   =   {right_str}")


    def print_terms_factors(self):

        left_term_factors_str = ""
        for term in self.left_terms:
            if left_term_factors_str != "":
                left_term_factors_str += " + "
            left_term_factors_str += term.get_printable_colored_factors()

        right_term_factors_str = ""
        for term in self.right_terms:
            if right_term_factors_str != "":
                right_term_factors_str += " + "
            right_term_factors_str += term.get_printable_colored_factors()


        print_f_line("Terms.factors", f"{left_term_factors_str}{RESET}  =  {BG_WHITE+BLACK}{right_term_factors_str}")


    def print_terms_factors_simplified(self):

        left_term_factors_str = ""
        for term in self.left_terms:
            if left_term_factors_str != "":
                left_term_factors_str += " + "
            left_term_factors_str += term.get_printable_colored_factors_simplified()

        right_term_factors_str = ""
        for term in self.right_terms:
            if right_term_factors_str != "":
                right_term_factors_str += " + "
            right_term_factors_str += term.get_printable_colored_factors_simplified()


        print_f_line("Simplified factors", f"{left_term_factors_str}{RESET}  =  {BG_WHITE+BLACK}{right_term_factors_str}")


    def print_right_to_left(self):

        left_term_factors_str = ""
        for term in self.left_terms:
            if left_term_factors_str != "":
                left_term_factors_str += " + "
            left_term_factors_str += term.get_printable_colored_factors_simplified()

        print_f_line("Right to Left", f"{left_term_factors_str}{RESET}  =  0")



    def print_sorted_by_exponents(self):

        left_term_factors_str = ""
        for term in self.left_terms:
            if left_term_factors_str != "":
                left_term_factors_str += " + "
            left_term_factors_str += term.get_printable_colored_factors_simplified()

        print_f_line("Sort by exponents", f"{left_term_factors_str}{RESET}  =  0")



    #def print_poly_degree(self):
    #    print(f"  Polynomial degree : {CYAN}{self.degree}{RESET}")


    def print_exponenent_regrouped_from_dico_degree_coef(self):
        strr = ""
        for degree, coef in self.dico_degree_coef.items():
            if strr != "":
                strr += " + "



            strr += f"{BG_WHITE+BLACK}[ {color_by_degree(degree)}{coef}{BLACK}"

            strr +=BLACK

            if degree == 1:
                strr += "*X"
            elif degree > 0:
                strr += "*X^"+str(degree)



            #strr += f" * X^{degree}"
            strr += f"{BLACK} ]{RESET}"
        print_f_line("Group by exponents", f"{strr}  =  0")


    def print_reduced_form_from_dico_degree_coef(self):
        strr = ""
        for degree, coef in self.dico_degree_coef.items():

            if coef != 0:
                temp_coef = coef
                if strr != "":
                    if temp_coef < 0 :
                        strr += "   "
                        #strr += " - "
                        #temp_coef *= -1
                    else:
                        strr += " + "

                ####  strr += f"{BG_WHITE+BLACK} {strip_trailing_zeros(temp_coef)}"
                strr += f"{BLACK} {strip_trailing_zeros(temp_coef)}"
                strr += f"{color_by_degree(degree)}"
                if degree > 1:
                    strr += f"*X^{degree}"
                elif degree == 1:
                    strr += f"*X"
                ####  strr += f" {BLACK}{RESET}"
                strr += f" {BLACK}"
        if strr == "":
            strr = "0"
        print_f_line("Reduced form", f"{strr}    =    0",    YELLOW,   BG_BRIGHT_WHITE + BLACK)

