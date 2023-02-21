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

sell_amount = [0]*9999 ##stock amount is stock size when buying seperate by time when you buy
sell_price = [0]*9999


##### get stock_amount and stock_price buy information



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

##i for sell
##j for buy
##we running check all j (buy side untill we reach current i (sell side))
for i in range(tempi):
    j = 0
    while j < i:
        if side[i] == "Sell":
            print("side i = Sell")
            print("Check all side[j] buy side")
            print("current price = ", price[i])
            print("current size = ", size[i])
            
            j = 0
            temp_price = 0
            ks = 0
            while j < i:
                if side[j] == "Buy" and size[j] != 9999:
                    
                    if temp_price == 0:
                        temp_price = price[j]
                        temp_price = price[j]
                        temp_stock = size[j]
                        temp_j = j
                        
                    if temp_price < price[j] and size[j] != 9999:
                        print("temp price < price")
                        print("temp price", temp_price)
                        temp_price = price[j]
                        temp_stock = size[j]
                        temp_j = j
                    print("j in side sell side[i] = ", j)
                j = j + 1
                
                print("finaly temp price = ", temp_price)
                print("fnaly temp stock = ", temp_stock)
                print("price [j] = ", price[temp_j])
                print("size [j] = ", size[temp_j])
                if size[i] < size[temp_j] and size[i] != 9999 and price[i] > price[temp_j]:
                    print("size < stock amount")
                    print("size =")
