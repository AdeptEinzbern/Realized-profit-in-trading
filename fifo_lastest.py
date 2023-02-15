import csv
import pandas as pd
df = pd.read_csv('fifo_test - Copy.csv')


side = df['Side'] ##get side buy or sell
price = df['Price'] ## get price 
size = df['Size'] ## get size position
fee = df['Fee'] ##get fee
currency = df['Fee Currency']

tempi = len(side) - 1 ## want to find how many data we have


i = tempi

stock_amount = [0]*9999 ##stock amount is stock size when buying seperate by time when you buy
stock_price = [0]*9999


##### get stock_amount and stock_price buy information
j = 0 
for i in range(tempi):
    if side[i] == 'Buy':
        stock_amount[j] = size[i]
        stock_price[j] = price[i]
        j = j + 1
    print("j = ", j)

print("stock amount = ", stock_amount[0])

i = 0
for i in range(tempi):
    print(stock_amount[i])
    


##### start with oldest date
i = tempi 
j = tempi
ks = tempi
profit = 0 #profit = total realised profit

##################### close this it ok if don't care about small fee
fee_main = 0
fee_second = 0
##get fee
while (ks >= 0):
    if currency[ks] == 'USDT': ## change USD to your main currency
        fee_main = fee_main + fee[ks]
        
    if currency[ks] == 'LTC': #$ change ETH to your secondary currency
        fee_second = fee_second + fee[ks]
    ks = ks - 1
    
print("fee USDT = ",fee_main)
print("fee LTC = ", fee_second)
print("i = ", i)
print("j = ", j)
k = tempi
#######################
i = 0
j = 0


