# -*- coding: utf-8 -*-
"""
same as p2_2 but with bisection serach.
balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
"""

balance = 3926; annualInterestRate = 0.2 #remove this line before submit


monthlyInterestRate = annualInterestRate /12
lowMonthlyPayment = round (balance /12, 2)
highMonthlyPayment = round (balance*(1+monthlyInterestRate)**12, 2)

updatedBalance = balance

while (abs(updatedBalance) >1):
    givenPayment = round ((lowMonthlyPayment + highMonthlyPayment)/2, 2)
    for i in range (12):
        monthlyUnpaidBalance = updatedBalance - givenPayment
        updatedBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
       
    if updatedBalance >1:
        updatedBalance = balance
        lowMonthlyPayment = givenPayment
        
    elif updatedBalance <-1:
        updatedBalance = balance
        highMonthlyPayment = givenPayment
        
    else:
        break

print ("givenPayment: ", givenPayment)