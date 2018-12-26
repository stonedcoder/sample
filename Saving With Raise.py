## Saving with a raise 

annual_salary = int(input ("Enter yout annual salary:"))
portion_saved = float(input ("Enter the percent of your salary to save:"))
total_cost = int(input ("Enter cost of your dream home:"))
portion_down_payment = 0.25*(total_cost) 
monthly_saved = (annual_salary/12.0)*portion_saved
semi_annual_raise = float(input("enter semi-annual raise"))

   
current_savings = 0 
r = 0.04
months = 0
while current_savings <= portion_down_payment:
    months += 1
    monthly_saving = current_savings*(r/12)
    current_savings += monthly_saving + monthly_saved
    
    if months % 6 == 0:
        annual_salary += semi_annual_raise*annual_salary
        monthly_saved = (annual_salary / 12.0)*portion_saved
       
        
    
    print("Number of months:",months)
