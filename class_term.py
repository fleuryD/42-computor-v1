
# ########################################################################### #
# #                                                                         # #
# #   42: computorv1                                                        # #
# #                                                                         # #
# #   by dFleury                                                            # #
# #                                                                         # #
# ########################################################################### #

import decimal

from utils_colors import *
from utils_math import *

# #############################################################################


# #  Un terme

class Term:
    def __init__(self, strr, isRightSide=0):
        self.str = strr          ##   -4  *  5.0  *  X^2  *  X^3
        self.coefFactors = []   ##   [ -4  ,  5.0  ]
        self.xFactors = []      ##   [  2  ,  3  ]
        self.degree = decimal.Decimal("0")         ##   2 + 3     ===>   5
        self.coefTotal = decimal.Decimal("1")      ##   -4 * 5.0  ===>   -20.0
        self.isRightSide = isRightSide
        self.factors = []


        #### TODO if no *
        for factor in strr.split("*"):
            if "X" in factor:
                self.xFactors.append(factor)
            else:
                self.coefFactors.append(factor)
                self.coefTotal *= decimal.Decimal(factor)
                ## factor = strip_trailing_zeros(factor)
                ## if '.' in factor:
                ##     self.coefTotal *= float(factor)
                ## else:
                ##     self.coefTotal *= int(factor)
            self.factors.append(factor)



        if self.xFactors:

            self.degree = decimal.Decimal("0")

            for xFactor in self.xFactors:
                if "^" in xFactor:
                    degree_str = xFactor.split("^")[1]
                else:
                    degree_str = "1"
                # self.degree += int(degree_str)


            # TODO :            replace   42.0000   by   42
                if degree_str == None:
                    self.degree = decimal.Decimal("0")
                else:
                    degree_str = strip_trailing_zeros(degree_str)
                    if degree_str.isdigit():  # Vérifie si degree_str est un nombre entier
                        self.degree += int(degree_str)
                    else:
                        raise ValueError(format_console_str("INVALID EXPONENT ERROR", f"Invalid exponent : {YELLOW+degree_str}", BOLD+RED, RED))




    def __repr__(self):
            return f"Term(coef={self.coefTotal}, degree={self.degree})"



    def get_printable_colored_factors(self):
        strr = f"{BG_WHITE+BLACK}["
        strr += color_by_degree(self.degree)

        for factors in self.coefFactors:
            if len(self.coefFactors) > 1:
                strr += "("
            strr += f"{factors}"
            if len(self.coefFactors) > 1:
                strr += ")"
            elif len(self.xFactors) > 0:
                strr += BLACK
                strr += "*"
        strr += BLACK


        for factors in self.xFactors:
            strr += "("+factors+")"
        strr +=  f"{BLACK}]{RESET}"

        return strr


    def get_printable_colored_factors_simplified(self):
        strr = f"{BG_WHITE+BLACK}["
        strr += color_by_degree(self.degree)


        strr += str(self.coefTotal)

        strr +=BLACK

        if self.degree == 1:
            strr += "*X"
        elif self.degree > 0:
            strr += "*X^"+str(self.degree)


        strr +=  f"{BLACK}]{RESET}"

        return strr

   # def calculate_area(self):
   #     return self.width * self.height
