import csv
import pandas as pd
df = pd.read_csv('ArtyEth_trades.csv')


side = df['Side'] ##get side buy or sell
price = df['Price'] ## get price 
size = df['Size'] ## get size position
fee = df['Fee'] ##get fee
currency = df['Fee Currency']

temp = len(side) - 1 ## want to find how many data we have


i = temp

stock_amount = [0]*999 ##stock amount is stock size when buying seperate by time when you buy
stock_price = [0]*999

j = temp

##### get stock_amount and stock_price buy information 
while(i >= 0):
    if side[i] == 'buy':
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
    if currency[ks] == 'USD': ## change USD to your main currency
        fee_main = fee_main + fee[ks]
        
    if currency[ks] == 'ETH': #$ change ETH to your secondary currency
        fee_second = fee_second + fee[ks]
    ks = ks - 1
    
print("fee USD = ",fee_main)
print("fee ETH = ", fee_second)

#######################
while(i >= 0):
    if side[i] == 'sell': ### 3 scenerio 01 is size[i] < stock_amount[j] 02 size[i] = stock_amount[j] 03 size[i] > stock_amount[j]
        #print("J = ",j)
        if size[i] < stock_amount[j] and stock_amount[j] != 9999: #stock_amount 9999 is no more stock left at this array
            #print("size < stock amount")
            #print("size = ", size[i])
            #print("at price", price[i])
            #print("stock price = ", stock_price[j])
            #print("stock amount = ", stock_amount[j])
            real = (price[i]*size[i]) - (size[i] * stock_price[j])
            profit = real + profit
            #print("real = ", real)
            stock_amount[j] = stock_amount[j] - size[i]  ### reduce stock[j] because sold out for size[i]
            #print("stock_amount after sell = ", stock_amount[j])
        if size[i] > stock_amount[j] and stock_amount[j] != 9999:
            #print("size > stock amount")
            #print("size = ", size[i])
            #print("at price", price[i])
            #print("stock price = ", stock_price[j])
            #print("stock amount = ", stock_amount[j])
            real = (price[i]*size[i]) - (size[i] * stock_price[j])
            profit = real + profit
            #print("real01 = ", real)
            temp = size[i] - stock_amount[j]
            #print("over size = ", temp)
            stock_amount[j] = 9999 ## we don't need to use this array anymore
            #print("stock amount 02 = ",stock_amount[j-1])
            if temp < stock_amount[j-1]:
                real = (price[i]*temp) - (temp * stock_price[j-1])
                profit = real + profit
                #print("real02 = ", real)
                stock_amount[j-1] = stock_amount[j-1] - temp
                j = j - 1
            #print("stock_amount after sell = ", stock_amount[j])
            #print("stock_amount02 after sell = ", stock_amount[j-1])
        if size[i] == stock_amount[j]:
            #print("size == stock amount")
            #print("size = ", size[i])
            #print("at price", price[i])
            #print("stock price = ", stock_price[j])
            #print("stock amount = ", stock_amount[j])
            real = (price[i]*size[i]) - (size[i] * stock_price[j])
            profit = real + profit
            stock_amount[j] = 9999
            j = j - 1
    #print("realised profit = ", profit)
    #print("i = ",i)
    
    i = i - 1
total = 0
i = temp
while (i >= 0):
    if stock_amount[i] != 0 and stock_amount[i] != 9999:
        total = stock_amount[i] + total
    i = i - 1
print("total exposure",total)
print("total exposure - fee (secondary) = ",total - fee_second)
print("profit = ", profit)
print("net profit = ", profit - fee_main)
