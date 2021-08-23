# -*- coding: utf-8 -*-
"""
balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

"""
balance = 3926; annualInterestRate = 0.2 #remove this line before submit


previousBalance = balance
monthlyInterestRate = annualInterestRate /12
monthlyPayment = balance // 120 * 10


while (previousBalance >0):
    previousBalance = balance
    for i in range (12):
        monthlyUnpaidBalance = previousBalance - monthlyPayment
        previousBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        
    if previousBalance <=0:
        break
    
    monthlyPayment+=10


print ("Lowest Payment: ", monthlyPayment)