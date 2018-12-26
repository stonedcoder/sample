##Finding the right amount to save 

annual_salary = int(input ("Enter yout annual salary:"))
semi_annual_raise = 0.07
r = 0.04
total_cost = 1000000
down_payment = 0.25*total_cost 
months = 36
monthly_salary = annual_salary / 12
low = 0
high = 10000
epsilon = 100
portion_saved = int((high+low)/2)
steps = 0 
total_salary = 0
for i in range (0, 36): 
    if i != 0 and i % 6 == 0:
        monthly_salary += (annual_salary / 12.0)*semi_annual_raise 
        
    monthly_salary += monthly_salary*(r/12)
    total_salary += monthly_salary 
if total_salary < down_payment - 100: 
    print('it is not possible')
    
else: 
    savings = total_salary*portion_saved
        
        
    while abs(savings - down_payment) >= epsilon:
        steps += 1
        if savings < down_payment:
            low = portion_saved
        else:
            high = portion_saved
        portion_saved = (high+low)/2
        savings = total_salary*portion_saved
        
    print ('best savings rate:', "%.4f" %portion_saved)
    print ('steps in bisection search:', steps)
