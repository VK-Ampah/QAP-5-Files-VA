#!C:\Users\vkamp\Desktop\QAP4\QAP-4-Files-VA\myenv\Scripts\python.exe
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
HST_RATE = .15
MONTHLY_PROCESSING_FEE = 39.99

current_date = datetime.now()
current_date = datetime.strftime(current_date.date(), "%Y-%m-%d")
    

print(f'ONE STOP INSURANCE COMPANY') 
print(f'MONTHLY PAYMENT LISTING AS OF {current_date}') 
print()
print(f'POLICY CUSTOMER             TOTAL                 TOTAL       MONTHLY') 
print(f'NUMBER NAME                PREMIUM      HST       COST        PAYMENT') 
print(f'======================================================================')

# Read records from policies file

with open('Policies.dat', 'r') as file:
    # setting intial values for totals
    total_policies = 0
    tot_premium = 0
    tot_hst = 0
    tot_extra_cost = 0
    tot_cost = 0
    tot_monthly = 0
    valid_payment_methods = ['Full', 'Monthly']
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
        payment_method =line[13].strip() 
        total_premium =float(line[14].strip())

            # Calculate extra costs
        extra_costs = 0
        if extra_liability == 'Y':
            extra_costs += COST_OF_EXTRA_LIABILITY_COVERAGE
        if optional_glass_coverage == 'Y':
            extra_costs += COST_OF_GLASS_COVERAGE
        if optional_loaner_car == 'Y':
            extra_costs += COST_FOR_LOANER_CAR_COVERAGE
            
        
        # calculations
        total_premium_cost = total_premium + extra_costs
        hst = total_premium_cost * HST_RATE
        total = total_premium_cost * hst
        monthly_payment = (total + MONTHLY_PROCESSING_FEE) / 12
        
        fname = first_name +''+ last_name
        
        # accumulating total values
        
        tot_premium += total_premium
        tot_hst += hst
        tot_extra_cost += extra_costs
        tot_cost += total
        tot_monthly += monthly_payment
        if payment_method == valid_payment_methods[1]:
            total_policies += 1
            print(f'{NEXT_POLICY_NUMBER:<5} {fname:<20s}${total_premium:<9.2f}   ${hst:<7.2f}  ${total:<9.2f}  ${monthly_payment:<9.2f}')  
print(f'======================================================================') 
print(f'Total policies: {total_policies}        ${tot_premium:<10.2f} ${tot_hst:<9.2f}  ${tot_extra_cost:<10.2f} ${tot_monthly:>.2f}')  
  