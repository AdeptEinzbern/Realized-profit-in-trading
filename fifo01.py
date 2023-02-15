import csv
import pandas as pd
df = pd.read_csv('fifo_test - Copy.csv')


side = df['Side'] ##get side buy or sell
price = df['Price'] ## get price 
size = df['Size'] ## get size position
fee = df['Fee'] ##get fee
currency = df['Fee Currency']

temp = len(side) - 1 ## want to find how many data we have


i = temp

stock_amount = [0]*9999 ##stock amount is stock size when buying seperate by time when you buy
stock_price = [0]*9999

j = temp

##### get stock_amount and stock_price buy information 
while(i >= 0):
    if side[i] == 'Buy':
        stock_amount[j] = size[i]
        stock_price[j] = price[i]
        j = j - 1
    i = i - 1
##### start with oldest date
i = temp 
j = temp
ks = temp
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

#######################
while(i >= 0):
    if side[i] == 'Sell': ### 3 scenerio 01 is size[i] < stock_amount[j] 02 size[i] = stock_amount[j] 03 size[i] > stock_amount[j]
        #print("J = ",j)
        if size[i] < stock_amount[j] and stock_amount[j] != 9999 and price[i] > stock_price[j]: #stock_amount 9999 is no more stock left at this array
            print("size < stock amount")
            print("size = ", size[i])
            print("at price", price[i])
            print("stock price = ", stock_price[j])
            print("stock amount = ", stock_amount[j])
            real = (price[i]*size[i]) - (size[i] * stock_price[j])
            profit = real + profit
            print("real = ", real)
            stock_amount[j] = stock_amount[j] - size[i]  ### reduce stock[j] because sold out for size[i]
            print("stock_amount after sell = ", stock_amount[j])
            print("\n")
            i = i - 1
            

            
        if size[i] > stock_amount[j] and stock_amount[j] != 9999 and price[i] > stock_price[j]:
            print("size > stock amount")
            print("size = ", size[i])
            print("at price", price[i])
            print("stock price = ", stock_price[j])
            print("stock amount = ", stock_amount[j])
            real = (price[i]*size[i]) - (size[i] * stock_price[j])
            profit = real + profit
            print("real01 = ", real)
            print("size before sell")
            print("size after sell", size[i])
            print("over size = ", temp)
            stock_amount[j] = 9999 ## we don't need to use this array anymore
            temp = size[i] - stock_amount[j]
            temp2 = size[i]
            size[i] = temp2 - temp #reduce size in size[i]
        
        if size[i] == stock_amount[j] and price[i] > stock_price[j] and stock_amount[j] != 9999:
            print("size == stock amount")
            print("size = ", size[i])
            print("at price", price[i])
            print("stock price = ", stock_price[j])
            print("stock amount = ", stock_amount[j])
            real = (price[i]*size[i]) - (size[i] * stock_price[j])
            print("real = ", real)
            profit = real + profit
            stock_amount[j] = 9999
            temp2 = size[i]
            size[i] = temp2
            j = j - 1
            print("realised profit = ", profit)
            print("i = ",i)
            print("\n")
            i = i - 1
    
        #loop find prrice i > stock_price not farther array than price[i]
        if price[i] < stock_price[j]:
            print("fiding price < stock price")
            j = j - 1
                
    if side[i] == 'Buy':
        print("side = buy")
        i = i - 1
    print("i = ", i)
    print("j = ", j)
    
total = 0
temp = len(side) - 1
i = temp

while (i >= 0):
    if stock_amount[i] != 0 and stock_amount[i] != 9999:
        total = stock_amount[i] + total
    i = i - 1
print("total exposure",total)
print("total exposure - fee (secondary) = ",total - fee_second)
print("profit = ", profit)
print("net profit = ", profit - fee_main)
print("\n")
##show order left

i = temp
while(i >= 0):
    
    if side[i] == 'Buy':
        print("stock buy amount",stock_amount[i])
        print("stock price ", stock_price[i])
        print("i = ", i)
    i = i - 1
