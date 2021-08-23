# -*- coding: utf-8 -*-
"""
1. balance - the outstanding balance on the credit card
2. annualInterestRate - annual interest rate as a decimal
3. monthlyPaymentRate - minimum monthly payment rate as a decimal

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid
balance)

"""
balance = 42; annualInterestRate = 0.2; monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate /12
previousBalance = balance
for i in range (12):
    minimumMonthlyPayment = monthlyPaymentRate * previousBalance
    monthlyUnpaidBalance = previousBalance - minimumMonthlyPayment
    previousBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    
print ("Remaining balance: ", "{:.2f}".format(previousBalance))
