#Title: Sales Commission
#Developer: Jenna Wan
#Purpose: calculate salary earned

salary = 0.0
commission = 0.0
sales = int(input("Total sales this year: "))

if sales > 0 and sales <= 200000:
    commission += (sales * 0.1)

if sales > 200000 and sales <= 400000:
    commission += 20000
    commission += (sales - 200000)* 0.2

if sales > 400000:
    commission += 60000
    commission += (sales - 400000)* 0.25 

if sales > 1000000:
    commission += 50000

salary = 35000 + commission
print("Total salary earned: " + str(salary))
