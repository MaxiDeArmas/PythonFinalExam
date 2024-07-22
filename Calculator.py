# CALCULATOR #

import math
import sys

'''Areas used:
1- Variables
2- Import
3- Classes and methods
4- Functions
5- Math
6- If
7- Loop
8- File
9- Try
10- List
'''

#--------------------CLASS--------------------#

#Define class with functions (operations) the calculator has
class Calculations:
    #Divide
    def div(self, num1, num2):
        return num1/num2

    #Remainder
    def remainder(self, num1, num2):
        return num1%num2

    #Square
    def square(self,num1):
        return num1**2

    #Cube
    def cube(self,num1):
        return num1**3

    #Square root
    def sqrt(self, num1):
        return math.sqrt(num1)

    #Cube root
    def cbrt(self, num1):
        return num1**(1/3)

#--------------------END CLASS--------------------#

#--------------------FUNCTIONS--------------------#
#Function in where all the program is made
def Calculator():

    #Create file to save all the operations user did
    f = open('MaxDeArmasFinal/operations.txt','w')
    
    #Title the file will have for the operations made by the user
    f.write('\nOPERATIONS MADE\n\n')
    
    #Close file
    f.close()

    #Keep running calculator until user wants to stop it
    while True:

        #Operations available
        print('===========================')
        print('∥    CALCULATOR           ∥')
        print('∥    ----------           ∥')
        print("∥ 1: Add                  ∥")
        print("∥ 2: Substract            ∥")
        print("∥ 3: Multiply             ∥")
        print("∥ 4: Divide               ∥")
        print("∥ 5: Remainder            ∥")
        print("∥ 6: Square of            ∥")
        print("∥ 7: Cube of              ∥")
        print("∥ 8: Square root of       ∥")
        print("∥ 9: Cube root of         ∥")
        print('∥ 10: Operations made     ∥')
        print("∥ 11: Exit                ∥")
        print('===========================')
        
        #Ask for option and validate if it is a number
        try:
            opt = int(input("Select operation desired (1 to 10): "))
        except ValueError: #If not a number
            print('\nOnly integers are allowed.\n')
        else:

            #Validating option selected by the user is between the options of the calculator
            if (opt >= 1) and (opt <=11):
                
                #Confirm the action
                if(opt == 11):

                    #Checking if the user wants to exit the program
                    ans = str(input('Are you sure you want to exit the program? (Y/N): ')).upper()

                    #If user wants to exit
                    if (ans == 'Y'):
                        print('\nThank you for using our calculator.\n')
                        break #Finish while
                    elif (ans == 'N'):
                        continue #Keep running calculator
                    else:
                        print('\nInput needs to be Y or N.\n')                        

                #Operations made by user
                if (opt == 10):

                    #Open file with operations made by the user
                    f = open('MaxDeArmasFinal/operations.txt','r')
                    print(f.read())
                    continue
                
                #Addition, Substract or Multiply
                if (opt >= 1) and (opt <= 3):
                    
                    #List where input numbers will be saved
                    numbers = []
                    
                    #Ask for option and validate if it is a number
                    try:
                        #How many numbers user wants to use
                        n = int(input("Enter amount of numbers for the operation: "))
                    except ValueError:
                        print('\nOnly numbers are allowed.\n')
                    else:

                        #Ask for numbers to use
                        for i in range(0, n):
                            ele = int(input("Enter number: "))

                            #Saving number on the list
                            numbers.append(ele) 

                        #Adition
                        if (opt == 1):

                            #Make calculation
                            res = sum(numbers)

                            #Show result
                            print('\nResult of the sum: ',numbers," = ",res,'.\n')

                            #Open file to save operation made
                            f = open('MaxDeArmasFinal/operations.txt','a')

                            #Save result on file
                            print('Result of the sum: ',numbers," = ",res,'.',file=f)
                            
                            #Close file
                            f.close()

                        elif (opt==2): #Substraction

                            #Start on first number of the list
                            res = numbers[0]

                            #Make calculation
                            for i in range(1,n):
                                res = res - numbers[i]
                                i+=1
                            
                            #Show result
                            print('\nResult of the substraction: ',numbers," = ",res,'.\n')

                            #Open file to save operation made
                            f = open('MaxDeArmasFinal/operations.txt','a')

                            #Save result on file
                            print('Result of the substraction: ',numbers," = ",res,'.',file=f)

                            #Close file
                            f.close()

                        else: #Multiplication

                            #Start on first number of the list
                            res = numbers[0]

                            #Make calculation
                            for i in range(1,n):
                                res = res * numbers[i]
                                i+=1
                            
                            #Show result
                            print('\nResult of the multiplication: ',numbers," = ",res,'.\n')

                            #Open file to save operation made
                            f = open('MaxDeArmasFinal/operations.txt','a')

                            #Save result on file
                            print('Result of the multiplication: ',numbers," = ",res,'.',file=f)
                            
                            #Close file
                            f.close()

                elif (opt >= 6 and opt <= 9):
                    
                    #Ask for number user wants to use
                    try: #Validating option selected by the user
                        a = float(input("Enter number: "))
                    except ValueError:
                        print('\nOnly numbers are allowed.\n')

                    #Square of
                    if(opt == 6):

                        #Show result
                        print('\nResult of the square of: ',a, "^ 2", " = ", myCalculator.square(a),'.\n')
                        
                        #Open file to save operation made
                        f = open('MaxDeArmasFinal/operations.txt','a')

                        #Save result on file
                        print('Result of the square of: ',a, "^ 2", " = ", myCalculator.square(a),'.',file=f)
                        
                        #Close file
                        f.close()
                    
                    #Cube of
                    elif(opt == 7):

                        #Show result
                        print('\nResult of the cube of: ',a, "^ 3", " = ", myCalculator.cube(a),'.\n')
                        
                        #Open file to save operation made
                        f = open('MaxDeArmasFinal/operations.txt','a')

                        #Save result on file
                        print('Result of the cube of: ',a, "^ 3", " = ", myCalculator.cube(a),'.',file=f)
                        
                        #Close file
                        f.close()

                    #Square root of
                    elif(opt == 8):

                        #Show result
                        print('\nResult of the square root of ',"√", a, " = ", myCalculator.sqrt(a),'.\n')

                        #Open file to save operation made
                        f = open('MaxDeArmasFinal/operations.txt','a')

                        #Save result on file
                        print('Result of the square root of: ',"square root of ", a, " = ", myCalculator.sqrt(a),'.',file=f)
                        
                        #Close file
                        f.close()

                    #Cube root of
                    elif(opt == 9):

                        #Show result
                        print('\nResult of the cube root of: ',"3√", a, " = ", myCalculator.cbrt(a),'.\n')

                        #Open file to save operation made
                        f = open('MaxDeArmasFinal/operations.txt','a')

                        #Save result on file
                        print('Result of the cube root of: ',"cube root of ", a, " = ", myCalculator.cbrt(a),'.',file=f)
                        
                        #Close file
                        f.close()

                elif (opt == 4) or (opt == 5):
                    #Ask for numbers user wants to use
                    try: #Validating option selected by the user
                        a = float(input("Enter first number: "))
                    except ValueError:
                        print('\nOnly numbers are allowed.\n')
                    else:
                        try: #Validating option selected by the user     
                            b = float(input("Enter second number: "))
                        except ValueError:
                            print('\nOnly numbers are allowed.\n')
                        else:

                            #Division
                            if(opt == 4):

                                #Show result
                                print('\nResult of the division ',a, "/", b, " = ", myCalculator.div(a, b),'.\n')

                                #Open file to save operation made
                                f = open('MaxDeArmasFinal/operations.txt','a')

                                #Save result on file
                                print('Result of the division: ',a, "/", b, " = ", myCalculator.div(a, b),'.', file=f)
                                
                                #Close file
                                f.close()

                            #Remainder
                            elif(opt == 5):

                                #Show result
                                print('\nResult of the remainder: ',a, "%", b, " = ", myCalculator.remainder(a, b),'.\n')

                                #Open file to save operation made
                                f = open('MaxDeArmasFinal/operations.txt','a')
                                
                                #Save result on file
                                print('Result of the remainder: ',a, "%", b, " = ", myCalculator.remainder(a, b),'.',file=f)
                                
                                #Close file
                                f.close()
            else:
                print("\nSelect a number 1 to 10\n")

#Creating the calculator object
myCalculator = Calculations()
#--------------------END FUNCTIONS--------------------#

#Call function
Calculator()
