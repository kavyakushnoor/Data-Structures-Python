# Kavyashree Kushnoor (850426572)
# Homework 2 - Process Accounts -CSC 231

from BankAccount import *

file = open("accounts.txt", "r")    #Opens file
accounts = []                       #Creates list

for line in file:                   #Creates Comma separated values for account
    tokens = line.split()           
    lastName = tokens[1]
    firstName = tokens[0]
    balance = tokens[2]
    bal = float(balance)
    acct = BankAccount(firstName, lastName, bal)
    accounts.append(acct)    

min = accounts[0]                   #Finds account with minimum balance value
for a in accounts:
    if a.balance < min.balance:
        min = a

max = accounts[0]                   #Finds account with maximum balance value
for a in accounts:
    if a.balance > max.balance:
        max = a

def counter():                      #Finds length of list to calculate average
    
    n = float(len(accounts))

    return n

def avg():                          #Determines average of balance
    n = counter()
    
    total = 0
    for a in accounts:
        total = total + (float(a.balance))
    avg = total/n
    return avg

def median():                       #Determines median of balance
    accounts.sort(key = lambda x:x.balance)

    length = len(accounts)
    
    if length%2 == 0:               #Finds median using formula
        index1 = int((length /2)-1)
        index2 = int(length/2)

        median = (accounts[index1].balance + accounts[index2].balance)/2
        
    else:
        index = int(length/2)
        median = accounts[index].balance
        
    return median

def addInterest():                  #Updates list balance with interest
    for acct in accounts:
        acct.balance += acct.calculateInterest()
    
    avgInterest = avg()             #Returns new average balance with interest
    return avgInterest

print ("The average balance of all the accounts is ", avg())
print ("The account with the largest balance is ", max)
print ("The account with the smallest balance is ", min)
print ("The median balance is ", median())
print ("The average balance of all the accounts after adding interest is ", addInterest())
lowestFN = accounts[0].firstName    #Sets first name to lowest, compares with other names
for x in accounts:
    if x.firstName < lowestFN:
        lowestFN = x.firstName
        #print (lowestFN)
for z in accounts:                  #Determines account with lowest first name on list
    if z.firstName == lowestFN:
        print ("The account with the lowest first name is ", z)

lowestLN = accounts[0].lastName     #Sets last name to lowest, compares with other names         
for x in accounts:
    if x.lastName < lowestLN:
        lowestLN = x.lastName
        #print (lowestLN)
for z in accounts:                  #Determines account with lowest last name on list
    if z.lastName == lowestLN:
        print ("The account with the lowest last name is ", z)

file.close()
