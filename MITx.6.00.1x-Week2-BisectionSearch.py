# This program searches for the smallest monthly payment such
# that we can pay off the entire balance within a year using bisection search.
# Month: 1
# Minimum monthly payment: 96.0
# Remaining balance: 4784.0

# balance = 999999; annualInterestRate = 0.18
MonthPayment = 0.0
balanceloop = balance

low = 0
high = balance
epsilon = 0.02
while abs(balanceloop) >= epsilon:
    MonthPayment = (high + low) / 2.0
    totalpaid = 0
    balancenew = 0
    balanceloop = balance #setting up a balance value to run the loop
    for month in range(0,12):
        balancenew = balanceloop - MonthPayment #new balance after taking out montly payment
        balancenewandinterest = balancenew + annualInterestRate/12 * balancenew #adding interest to balance
        balanceloop = balancenewandinterest #setting up the balance for next month run
        totalpaid += MonthPayment #counting the total amount paid
    if balanceloop < 0:
        high = MonthPayment
    else:
        low = MonthPayment

print("Lowest Payment: "+str(round(MonthPayment,2)))
