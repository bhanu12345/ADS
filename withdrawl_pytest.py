import time

def atm():
    import datetime
    today = datetime.date.today()
    print('Welcome to Sacred Heart ATM')
    restart='y'
    chances = 3
    balance = 100
    while chances >= 0:
        swipe=input('\nswipe your card ')
        pin = int(input('Please Enter You 4 Digit Pin: '))
        if pin == (1234):
            while restart not in ('n','NO','no','N'):
                print('Please Press 1 For Your Balance\n')
                print('Please Press 2 To Make a Withdrawl\n')
                print('Please Press 3 To Deposit Amount\n')
                option = int(input('Enter your option '))
                if option > 3 or option < 1:
                    print('enter correct option')
                    break
                elif option == 1:
                    print ('\n', today)
                    print('\nYour Balance is $',balance,'\n')
                    restart = input('Would You you like to go back(y/n)? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break
                elif option == 2:
                    withdrawl = float(input('\nHow Much Would you like to withdraw? \n \n$10,$20,$40,$60,$80,$100 for other enter 1: '))
                    if withdrawl in [10, 20, 40, 60, 80, 100]:
                        balance = balance - withdrawl
                        print ('\n', today)
                        print('\nwithdraw amount : $',withdrawl)
                        print ('\nYour Current Balance is $',balance)
                        restart = input('\nWould You you like to go back(y/n)? ')
                        if restart in ('n','NO','no','N'):
                            print('Thank You')
                            break
                    elif withdrawl != [10, 20, 40, 60, 80, 100]:
                        print('\nInvalid Amount, Please Re-try\n')
                        restart = ('y')
                    elif withdrawl == 1:
                            withdrawl = float(input('Please Enter Desired amount:'))    
                            
                elif option == 3:
                    Pay_in = float(input('How Much Would You like to Deposit '))
                    balance = balance + Pay_in
                    print ('\n',today)
                    print ('\nDeposit: ', Pay_in)
                    print ('\nYour current Balance is now $',balance,)
                    restart = input('\nWould You you like to go back( y/n)? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break
                else:
                    print('Please Enter a correct number. \n')
                    restart = ('y')
        elif pin != ('1234'):
            print('Incorrect Password')
            chances = chances - 1
            if chances == 0:
                print('\nNo more tries')
                break
atm()

import unittest

class MyTest():
    def test_atm():
        main_menu='y'
        number_of_pin_attemps=3
        balance_availabe= 67.14
        while number_of_pin_attemps >= 3:
            swipe_card=input('\nswipe your card')
            pin_request=int(input('please enter your 4 digit pin: '))
            pin_request == 0
            if pin_request == (1234):
                while main_menu not in ('n', 'NO', 'no', 'N'):
                    print('Press 1 For Your Current Balance\n')
                    print('press 2 To Make a Withdrawl\n')
                    print('press 3 To Deposit Amount\n')
                    user_option=int(input('Enter your Option? '))
                    if user_option > 3 or user_option < 1:
                        print('enter correct option')
                        break
                    elif user_option == 1:
                        print('\nYour Current Balance is $',balance)
                        main_menu= input('would you like to go back to menu(y/n)? ')
                        if main_menu in ('n','NO', 'no', 'N'):
                            print('Thank You')
                            break
                    
                    elif option == 2:
                        withdrawl = float(input('\nHow Much Would you like to withdraw? \n$10,$20,$40,$60,$80,$100 for other enter 1: '))
                        if withdrawl in [10, 20, 40, 60, 80, 100]:
                            balance = balance - withdrawl
                            print('\n withdraw amount : $',withdrawl)
                            print ('\nYour Current Balance is $',balance)
                            main_menu = input('\nWould You you like to go back(y/n)? ')
                            if main_menu in ('n','NO','no','N'):
                                print('Thank You')
                                break
                        
                            elif withdrawl != [10, 20, 40, 60, 80, 100]:
                                print('\nInvalid Amount, Please Re-try\n')
                                main_menu = ('y')
                            
                            elif withdrawl == 1:
                                withdrawl = float(input('Please Enter Desired amount:'))    

                    elif option == 3:
                        Pay_in = float(input('How Much Would You like to Deposit '))
                        balance = balance + Pay_in
                        print ('\nDeposit: ', Pay_in)
                        print ('\nYour current Balance is now $',balance,)
                        main_menu = input('\nWould You you like to go back(y/n)? ')
                        if main_menu in ('n','NO','no','N'):
                            print('Thank You')
                            break
                        
                    else:
                        print('Please Enter a correct number. \n')
                        main_menu = ('y')
                    
            elif pin != ('1234'):
                print('Incorrect Password')
                number_of_pin_attempts = number_of_pin_attempts - 1
                if number_of_pin_attempts == 0:
                    print('\nNo more tries')
                    break



unittest.main()
