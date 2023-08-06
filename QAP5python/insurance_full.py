# Program Description: This program calculates new insurance policies for One Stop Insurance Company and prints reports for all policies
# Author: Valentine Ampah
# Date: 2023-08-05
from datetime import datetime
from dateutil.relativedelta import relativedelta
import time
from tqdm import tqdm

# constants
COST_OF_EXTRA_LIABILITY_COVERAGE = 130
COST_OF_GLASS_COVERAGE = 86
COST_FOR_LOANER_CAR_COVERAGE = 58
    
current_date = datetime.now()
current_date = datetime.strftime(current_date.date(), "%Y-%m-%d")


print('ONE STOP INSURANCE COMPANY POLICY') 
print(f'LISTING AS OF {current_date}') 
print()
print('POLICY CUSTOMER                POLICY          INSURANCE     EXTRA      TOTAL') 
print('NUMBER NAME                     DATE            PREMIUM      COSTS     PREMIUM')
print('===============================================================================')  

# Read records from policies file

with open('Policies.dat', 'r') as file:
    total_policies =0
    tot_premium = 0
    tot_extra_cost = 0
    tot_cost = 0
    for record in file:
        record.strip()
        #print(record)
        line = record.split(',')
        NEXT_POLICY_NUMBER = line[0]
        current_date =line[1]
        first_name =line[2]
        last_name =line[3]
        address =line[4]
        city =line[5]
        province =line[6]
        postal_code =line[7]
        phone_number =line[8]
        num_cars_insured=line[9] 
        extra_liability =line[10].strip()
        optional_glass_coverage =line[11].strip()
        optional_loaner_car =line[12].strip()
        payment_method =line[13] 
        total_premium =float(line[14].strip())

            # Calculate extra costs
        extra_costs = 0
        if extra_liability == 'Y':
            extra_costs += COST_OF_EXTRA_LIABILITY_COVERAGE
        if optional_glass_coverage == 'Y':
            extra_costs += COST_OF_GLASS_COVERAGE
        if optional_loaner_car == 'Y':
            extra_costs += COST_FOR_LOANER_CAR_COVERAGE

        total_cost = total_premium + extra_costs
        
        fname = first_name +''+ last_name
        
        total_policies +=1
        tot_premium += total_premium
        tot_extra_cost += extra_costs
        tot_cost += total_cost       


        print(f'{NEXT_POLICY_NUMBER:<5}  {fname:<20s}   {current_date:<10}     ${total_premium:<9.2f}    ${extra_costs:<9.2f} ${total_cost:<9.2f}') 
print('===============================================================================') 
print(f'Total policies: {total_policies}                            ${tot_premium:<10.2f}   ${tot_extra_cost:<10.2f}${tot_cost:<10.2f}') 