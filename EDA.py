import sys
from colorama import Fore, Style, Back

equations_list = []
remainders_list = []
quotients_list = []
divisors_list = []
dividends_list = []
numbers = []
remainders_want_list = []
hcfs_found = []
num1 = 0
num2 = 0

add_symbol = Fore.RED + ' + ' + Style.RESET_ALL
equal_symbol = Fore.RED + ' = ' + Style.RESET_ALL
multiply_symbol = Fore.RED + 'x' + Style.RESET_ALL
subtract_symbol = Fore.RED + '-' + Style.RESET_ALL
bracket_open = Fore.RED + '(' + Style.RESET_ALL
bracket_close = Fore.RED + ')' + Style.RESET_ALL

print(Style.RESET_ALL)

def ask(numbers):
    print('\n')
    xyz = input(Fore.CYAN + 'Choose one of the following options. Type A, B or C. \na)Find HCF of 2 numbers and represent the HCF as a linear expression. \nb)Find HCF of 2 or more numbers. \nc)Find the largest number which divides 2 or more numbers and leaves a specific remainder' + Style.RESET_ALL + '\n').lower()
    
    if xyz == 'a':
        how_many = 2
        want_remainder = 'n'
        numbers_input(how_many, want_remainder)
        poi = HCF_find(xyz)
        if len(equations_list) > 2:
            equation_forming()


        else:
            if numbers[0] < numbers[1]:
                a = int(poi/numbers[0])
                b = 0
            elif numbers[1] < numbers[0]:
                a = 0
                b = int(poi/numbers[1])
            else:
                a = 1
                b = 0

            print('\n' + Back.WHITE + Fore.BLACK + 'If the HCF of ' + str(numbers[0]) + ' and ' +  str(numbers[1]) + ' is represented in the form of ' + str(numbers[0]) + 'a' + ' + ' + str(numbers[1]) + 'b, then:' + '   ' + Style.RESET_ALL)
            print(Back.WHITE + Fore.BLACK + 'a = ' + str(a) + '   ' + Style.RESET_ALL)
            print(Back.WHITE + Fore.BLACK + 'b = ' + str(b) + '   ' + Style.RESET_ALL)


    elif xyz == 'b':
        want_remainder = 'n'
        how_many = input('\n' + Fore.CYAN + 'How many numbers?' + Style.RESET_ALL + '\n')
        check(how_many, 2,)
        how_many = int(how_many)
        numbers_input(how_many, want_remainder)
        print('\n' + Fore.BLACK + Back.WHITE + 'HCF' + str(numbers) + ' = ' + str(HCF_find(xyz)) + '   ' + Style.RESET_ALL)
        

    elif xyz == 'c':
        want_remainder = 'y'
        how_many = input('\n' + Fore.CYAN + 'How many numbers?' + Style.RESET_ALL + '\n')
        check(how_many, 2,)
        how_many = int(how_many)
        numbers_input(how_many, want_remainder)
        numbers = remainder_formality(numbers, remainders_want_list)
        print('\n' + Fore.BLACK + Back.WHITE + 'The number is ' + str(HCF_find(xyz)) + '   ' + Style.RESET_ALL)
    

    elif xyz != 'a' and xyz != 'b' and xyz != 'c':
        print(Fore.MAGENTA + '\nInvalid Command. Try again' + Style.RESET_ALL)
        ask(numbers)


def check(a, vbn):
    try:
        a = int(a)
    except:
        print(Fore.MAGENTA + '\nInput is not a positive integer. \n THANK YOU!' + Style.RESET_ALL)
        sys.exit
    
    if a < vbn:
        print(Fore.MAGENTA + '\nInvalid input \n THANK YOU!' + Style.RESET_ALL)
        sys.exit
        

def numbers_input(how_many, want_remainder):
    for zxc in range(0, how_many):
        number_idk = input('\n' + Fore.CYAN + 'Enter a number' + Style.RESET_ALL + '\n')
        check(number_idk, 1)
        numbers.append(int(number_idk))

        if want_remainder == 'y':
            dfg = input('\n' + Fore.CYAN + 'What remainder should be left for the number ' + str(numbers[-1]) + '?' + Style.RESET_ALL + '\n')
            check(dfg, 0)
            dfg = int(dfg)
            
            if dfg >= numbers[-1]:
                print(Fore.MAGENTA + '\n The remainder must be smaller than the number. \n THANK YOU!' + Style.RESET_ALL)
                sys.exit()
            
            remainders_want_list.append(dfg)


def HCF_find(xyz):
    print('')
    asd = 0

    while asd+1 != len(numbers):
        asd = asd + 1

        if len(hcfs_found) == 0:
            num1 = numbers[0]
            num2 = numbers[1]

        else:
            num1 = numbers[asd]
            num2 = hcfs_found[-1]

        if xyz != 'a':
            print('\n' + Fore.YELLOW + 'Finding HCF of ' + str(num1) + ' and ' + str(num2) + Style.RESET_ALL)

        divisor = max([num1, num2])
        remainder = min([num1, num2])
        x = 0

        while remainder != 0:
            x = x + 1
            dividend = divisor
            divisor = remainder
            quotient = dividend//divisor
            remainder = dividend - divisor*quotient
            quotient = dividend//divisor
            remainder = dividend - divisor*quotient
            print('\n' + Fore.GREEN + 'Dividend: ' + Style.RESET_ALL +str(dividend))
            print(Fore.GREEN +'Divisor: ' + Style.RESET_ALL +str(divisor))
            print(Fore.GREEN +'Quotient: ' + Style.RESET_ALL +str(quotient))
            print(Fore.GREEN +'Remainder: ' + Style.RESET_ALL +str(remainder))
            
            if xyz == 'a':
                quotients_list.append(quotient)
                remainders_list.append(remainder)
                divisors_list.append(divisor)
                dividends_list.append(dividend)
                equation = (str(dividend) + equal_symbol + str(divisor) + multiply_symbol + str(quotient) + add_symbol + str(remainder))
                equations_list.append(equation)
                print(Fore.YELLOW + 'Equation' + str(x) + ': ' +Style.RESET_ALL + str(equation) + '\n')

        HCF = divisor
        hcfs_found.append(HCF)
        print('\n' + Back.WHITE + Fore.BLACK + 'The HCF of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(divisor) + '   ' + Style.RESET_ALL )
    return HCF


def equation_forming():
    original_equation = equations_list[-2]
    base_equation_number = len(equations_list) - 1
    print('\n' + Fore.YELLOW + 'Equation' + str(base_equation_number) + ': ' + Style.RESET_ALL + original_equation)
    LHS = remainders_list[-2]
    base_equation_term1_1 = dividends_list[-2]
    base_equation_term1_2 = 1
    base_equation_term2_1 = quotients_list[-2]*-1
    base_equation_term2_2 = divisors_list[-2]
    print(str(LHS) + equal_symbol + str(base_equation_term1_1) + multiply_symbol + str(base_equation_term1_2) + add_symbol + str(base_equation_term2_1) + multiply_symbol + str(base_equation_term2_2))

    idk = -2
    while idk > len(equations_list)*-1:
        idk = idk - 1
        number_equation = len(equations_list) + idk + 1
        bracket_term1 = dividends_list[idk]
        bracket_term2_1 = quotients_list[idk]*-1
        bracket_term2_2 = divisors_list[idk]

        print('\n' + Fore.YELLOW + 'Equation' + str(number_equation) + ': ' + Style.RESET_ALL + equations_list[idk])
        print(str(remainders_list[idk]) + equal_symbol + str(bracket_term1) + add_symbol +  str(bracket_term2_1)  + multiply_symbol + str(bracket_term2_2))
        print('\n' + Fore.GREEN + 'Replacing value of ' + str(base_equation_term2_2) + ' from Equation' + str(number_equation) + ' in Equation' + str(base_equation_number))
        print(Style.RESET_ALL + str(LHS) + equal_symbol + str(base_equation_term1_1) + multiply_symbol + str(base_equation_term1_2) + add_symbol + str(base_equation_term2_1) + bracket_open + str(bracket_term1) + add_symbol +  str(bracket_term2_1)  + multiply_symbol + str(bracket_term2_2) + bracket_close)
        
        base_equation_term2_1 = base_equation_term2_1
        base_equation_term2_2 = bracket_term1
        base_equation_term3_1 = base_equation_term2_1*bracket_term2_1
        base_equation_term3_2 = bracket_term2_2
        
        print(str(LHS) + equal_symbol + str(base_equation_term1_1) + multiply_symbol + str(base_equation_term1_2) + add_symbol + str(base_equation_term2_1) + multiply_symbol + str(base_equation_term2_2) + add_symbol + str(base_equation_term3_1) + multiply_symbol + str(base_equation_term3_2))
        print(str(LHS) + equal_symbol + str(base_equation_term2_1) + multiply_symbol + str(base_equation_term2_2) + add_symbol + str(base_equation_term3_1) + multiply_symbol + str(base_equation_term3_2) + add_symbol + str(base_equation_term1_1) + multiply_symbol + str(base_equation_term1_2))
        print(str(LHS) + equal_symbol + str(base_equation_term2_1) + multiply_symbol + str(base_equation_term2_2) +  add_symbol +  str(base_equation_term3_2) + bracket_open + str(base_equation_term1_2) + add_symbol + str(base_equation_term3_1) + bracket_close)
        
        base_equation_term1_1_new = base_equation_term2_2
        base_equation_term1_2_new = base_equation_term2_1
        base_equation_term2_1_new = base_equation_term1_2 + base_equation_term3_1
        base_equation_term2_2_new = base_equation_term1_1

        base_equation_term1_1 = base_equation_term1_1_new
        base_equation_term1_2 = base_equation_term1_2_new
        base_equation_term2_1 = base_equation_term2_1_new
        base_equation_term2_2 = base_equation_term2_2_new
        #2.1 has become 2.2, 2.2 has become 2.1
        print(Fore.YELLOW + 'Equation' + str(base_equation_number) + ': ' + Style.RESET_ALL + str(LHS) + equal_symbol + str(base_equation_term1_1) + multiply_symbol + str(base_equation_term1_2) + add_symbol + str(base_equation_term2_2) + multiply_symbol + str(base_equation_term2_1))
        
    print('\n' + Back.WHITE + Fore.BLACK + 'If the HCF of ' + str(numbers[0]) + ' and ' +  str(numbers[1]) + ' is represented in the form of ' + str(base_equation_term1_1) + 'a' + ' + ' + str(base_equation_term2_2) + 'b, then:' + '   ' + Style.RESET_ALL)
    print(Back.WHITE + Fore.BLACK + 'a = ' + str(base_equation_term1_2_new) + '   ' + Style.RESET_ALL)
    print(Back.WHITE + Fore.BLACK + 'b = ' + str(base_equation_term2_1) + '   ' + Style.RESET_ALL)

    base_equation_term3_1 = base_equation_term1_1
    base_equation_term3_2 = base_equation_term2_2
    base_equation_term4_1 = base_equation_term1_1 * -1
    base_equation_term4_2 = base_equation_term2_2
    new_equation(base_equation_term1_1, base_equation_term1_2, base_equation_term4_1, base_equation_term4_2, base_equation_term2_1, base_equation_term2_2, base_equation_term3_1, base_equation_term3_2, base_equation_number, LHS)

    base_equation_term1_1 = base_equation_term1_1_new
    base_equation_term1_2 = base_equation_term1_2_new
    base_equation_term2_1 = base_equation_term2_1_new
    base_equation_term2_2 = base_equation_term2_2_new

    base_equation_term3_1 = base_equation_term1_1
    base_equation_term3_2 = base_equation_term2_2 * -1
    base_equation_term4_1 = base_equation_term1_1
    base_equation_term4_2 = base_equation_term2_2
    new_equation(base_equation_term1_1, base_equation_term1_2, base_equation_term4_1, base_equation_term4_2, base_equation_term2_1, base_equation_term2_2, base_equation_term3_1, base_equation_term3_2, base_equation_number, LHS)

def new_equation(base_equation_term1_1, base_equation_term1_2, base_equation_term4_1, base_equation_term4_2, base_equation_term2_1, base_equation_term2_2, base_equation_term3_1, base_equation_term3_2, base_equation_number, LHS):
    print('\n \n')
    print(Fore.YELLOW + 'Equation' + str(base_equation_number) + ': ' + Style.RESET_ALL + str(LHS) + equal_symbol + str(base_equation_term1_1) + multiply_symbol + str(base_equation_term1_2) + add_symbol + str(base_equation_term2_2) + multiply_symbol + str(base_equation_term2_1))
    print(Style.RESET_ALL + str(LHS) + equal_symbol + str(base_equation_term1_1) + multiply_symbol + str(base_equation_term1_2) + add_symbol + str(base_equation_term2_2) + multiply_symbol + str(base_equation_term2_1) + add_symbol + Fore.GREEN + str(base_equation_term3_1) + multiply_symbol + Fore.GREEN+ str(base_equation_term3_2) + add_symbol +Fore.GREEN + str(base_equation_term4_1) + multiply_symbol+ Fore.GREEN + str(base_equation_term4_2) + Style.RESET_ALL)
    print(Style.RESET_ALL + str(LHS) + equal_symbol + str(base_equation_term1_1) + multiply_symbol + str(base_equation_term1_2) + add_symbol + str(base_equation_term3_1) + multiply_symbol + str(base_equation_term3_2) + add_symbol + str(base_equation_term2_2) + multiply_symbol + str(base_equation_term2_1) + add_symbol + str(base_equation_term4_1) + multiply_symbol + str(base_equation_term4_2))
    print(Style.RESET_ALL + str(LHS) + equal_symbol + str(base_equation_term1_1) + bracket_open + str(base_equation_term1_2) + add_symbol + str(base_equation_term3_2) + bracket_close + add_symbol + str(base_equation_term2_2) + bracket_open + str(base_equation_term2_1) + add_symbol + str(base_equation_term4_1) + bracket_close)

    base_equation_term1_2 = base_equation_term1_2 + base_equation_term3_2
    base_equation_term2_1 = base_equation_term2_1 + base_equation_term4_1
    print(str(LHS) + equal_symbol + str(base_equation_term1_1) + multiply_symbol + str(base_equation_term1_2) + add_symbol + str(base_equation_term2_2) + multiply_symbol + str(base_equation_term2_1))

    print('\n' + Back.WHITE + Fore.BLACK + 'If the HCF of ' + str(numbers[0]) + ' and ' +  str(numbers[1]) + ' is represented in the form of ' + str(base_equation_term1_1) + 'a' + ' + ' + str(base_equation_term2_2) + 'b, then:' + '   ' + Style.RESET_ALL)
    print(Back.WHITE + Fore.BLACK + 'a = ' + str(base_equation_term1_2) + '   ' + Style.RESET_ALL)
    print(Back.WHITE + Fore.BLACK + 'b = ' + str(base_equation_term2_1) + '   ' + Style.RESET_ALL)


def remainder_formality(numbers, remainders_want_list):
    old_numbers = numbers.copy()
    numbers.clear()
    print('\n' + Fore.YELLOW + 'We will subtract the remainders from the numbers' + Style.RESET_ALL + '\n')

    for rty in range(0, len(remainders_want_list)):
        okm = old_numbers[rty] - remainders_want_list[rty]
        print(str(old_numbers[rty]) + subtract_symbol + str(remainders_want_list[rty]) + equal_symbol + str(okm))
        numbers.append(okm)

    print('\n' + Fore.YELLOW + 'Now, we will find the HCF of the new numbers obtained' + Style.RESET_ALL)
    print(numbers)
    return numbers

ask(numbers)