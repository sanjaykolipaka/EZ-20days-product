'''ss having 100000 in his bank account. rate of interst is 12% per annum.
in th 5th month ss is withdrawing 25000 rs in order to buy a git for his loved one.
in 9th month 10000rs is deposited by his 2nd loved one.End of financial year how much ss is having in account
simple intrest'''

def calculate(PA,roi,month):
    z=0
    while (month<=12):
        interest = 0.01*PA
        z=z+interest
        if (month == 4):
            PA = PA - 25000
        elif month == 8:
            PA = PA + 10000
        month+=1
        pa = PA
    return z,pa

    
PA= 100000
roi = 1
month=1
a,pa = calculate(PA,roi,month)
print(pa+ a)


    
    










'''n = 100000
roi = 12
roi_per_month = roi/12
month = 1
while(month<=12):
    n = n + ((roi_per_month/100)*n)
    month+=1
print(n)
    


























# Principal amount
principal = 100000  # Initial amount in the bank account

# Annual interest rate
annual_interest_rate = 0.12  # 12% per annum

# Time in months
total_months = 12  # 1 year

# Calculate simple interest for 5 months
withdrawal_amount = 25000
withdrawal_month = 5
remaining_months_1 = total_months - withdrawal_month
simple_interest_1 = (principal - withdrawal_amount) * annual_interest_rate * withdrawal_month / 12

# Calculate simple interest for another 4 months after the deposit
deposit_amount = 10000
deposit_month = 9
remaining_months_2 = remaining_months_1 - (total_months - deposit_month)
simple_interest_2 = (principal - withdrawal_amount + deposit_amount) * annual_interest_rate * remaining_months_2 / 12

# Calculate the final amount in the account
final_amount = principal + simple_interest_1 + simple_interest_2

print("Final amount in SS's bank account at the end of the financial year:", final_amount)'''

