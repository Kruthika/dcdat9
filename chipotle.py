# -*- coding: utf-8 -*-
"""
Created on Thu Oct 01 19:41:58 2015

@author: Kruthika
"""
from collections import defaultdict
import csv
# read tab-delimited file
with open('chipotle.tsv','rb') as fin:
    cr = csv.reader(fin, delimiter='\t')
    file_nested_list = [row for row in cr]
    
# separate the header and data
header = file_nested_list[0]
data = file_nested_list[1:]

#Calculating average price of an order
# Calculating the number of unique orders by removing the duplicates
orders = len(set([row[0] for row in data]))
# Stripping '$' and converting the prices to float values
price= [float(row[4].lstrip('$')) for row in data]
#Calculating average price of an order and rounding it to 2 places
average_price = round(sum(price)/orders, 2) 

#Creating a unique list of  sodas and soft drinks
unique_drinks = []
for row in data:
    if "Canned" in row[2]:
        unique_drinks.append(row[3][1:-1])
unique_sodas = set(unique_drinks)

#Average number of toppings per a burrito
burrito = []
toppings = []
for row in data:
    if 'Burrito' in row[2]:
        burrito.append(row[2])
#Counting the commas and adding 1 to include the last topping in the row
        toppings.append(row[3].count(',') +1)
average_toppings = round(float(sum(toppings))/len(burrito), 2)

# Creating a dictionary with chips order and quantity ordered
d = defaultdict(int)
for row in data:
    if 'Chips' in row[2]:
        d[row[2]] += int(row[1])
        
#Number of soda drinkers that ordered for burritos
soda =[]
for row in data:
    if 'Soda' in row[2]:
        soda.append(row[0])# Appending the order id to the list
burritos = []
for row in data:
    if 'Burrito' in row[2]:
        burritos.append(row[0])# Appending the order id to the list
#Removing the duplicates in the lists and listing the common order id to both
soda_burrito = set(soda) & set(burritos)
       
        
        
        

        
        
     


