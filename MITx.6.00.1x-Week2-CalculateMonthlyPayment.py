# This program calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
for MonthPayment in range(0,balance,10):
    totalpaid = 0
    balancenew = 0
    balanceloop = balance #setting up a balance value to run the loop
    for month in range(0,12):
        #print("Month: "+str(month+1))
        #MonthPayment = monthlyPaymentRate*balance
        #print("Minimum monthly payment: "+str(round(MonthPayment,2)))
        balancenew = balanceloop - MonthPayment #new balance after taking out montly payment
        balancenewandinterest = balancenew + annualInterestRate/12 * balancenew #adding interest to balance
        #print("Remaining balance: "+str(round(balancenewandinterest,2)))
        balanceloop = balancenewandinterest #setting up the balance for next month run
        totalpaid += MonthPayment #counting the total amount paid
    if balanceloop <= 0:
        break

print("Lowest Payment: "+str(round(MonthPayment,2)))
