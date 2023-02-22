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
## fee as percent 0.01 mean 0.01%
fee_main = 0.01
fee_second = 0.01
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
while i <= tempi:
    j = 0
    t = 0
    while j < i:
        print("i start = ", i)
        if side[i] == "Sell":
            #print("side i = Sell")
            #print("Check all side[j] buy side")
            #print("current price = ", price[i])
            #print("current size = ", size[i])
            
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
                        #print("temp price < price")
                        #print("temp price", temp_price)
                        temp_price = price[j]
                        temp_stock = size[j]
                        temp_j = j
                    #print("j in side sell side[i] = ", j)
                j = j + 1
                
                #print("finaly temp price = ", temp_price)
                #print("fnaly temp stock = ", temp_stock)
                #print("price [j] = ", price[temp_j])
                #print("size [j] = ", size[temp_j])
                if size[i] < size[temp_j] and size[i] != 9999 and price[i] > price[temp_j]:
                    #print("size < stock amount")
                    #print("size = ", size[i])
                    #print("at price", price[i])
                    #print("stock price = ", price[temp_j])
                    #print("stock amount = ", size[temp_j])
                    fee_price_i = (price[i]*size[i])*(fee_main/10)
                    fee_price_j = (price[temp_j]*size[i])*(fee_main/10)
                    total_fee = fee_price_i + fee_price_j
                    #print("fee price[i] = ", fee_price_i)
                    #print("fee price[temp_j] = ", fee_price_j)
                    #print("total fee = ", total_fee)
                    real = (price[i]*size[i]) - (size[i] * price[temp_j])
                    profit = real + profit - total_fee
                    #print("real = ", real)
                    #print("realzed - fee = ", real - total_fee)
                   
                    size[temp_j] = size[temp_j] - size[i]  ### reduce stock[j] because sold out for size[i]
                    #print("stock_amount after sell = ", size[temp_j])
                    #print("\n")
                    size[i] = 9999
                    #print("size[i] = ", size[i])
                    
                    ks = 1

                if size[i] == size[temp_j] and size[temp_j] != 9999 and size[i] != 9999 and price[i] > price[temp_j]:
                    #print("size == stock amount")
                    #print("size = ", size[i])
                    #print("at price", price[i])
                    #print("stock price = ", price[temp_j])
                    #print("stock amount = ", size[temp_j])
                    fee_price_i = (price[i]*size[i])*(fee_main/10)
                    fee_price_j = (price[temp_j]*size[i])*(fee_main/10)
                    total_fee = fee_price_i + fee_price_j
                    #print("fee price[i] = ", fee_price_i)
                    #print("fee price[temp_j] = ", fee_price_j)
                    #print("total fee = ", total_fee)
                    real = (price[i]*size[i]) - (size[i] * price[temp_j])
                    profit = real + profit - total_fee
                    #print("real = ", real)
                    #print("realzed - fee = ", real - total_fee)
                    size[temp_j] = 9999
                    size[i] = 9999
                    #print("realised profit = ", profit)
                    #print("i = ",i)
                    #print("size[i] = ", size[i])
                    #print("stock_amount after sell = ", size[temp_j])
                    ks = 1
                        

                if size[i] > size[temp_j] and size[temp_j] != 9999 and size[i] != 9999 and price[i] > price[temp_j]:
                    #print("size > stock amount")
                    #print("size = ", size[i])
                    #print("at price", price[i])
                    #print("stock price = ", price[temp_j])
                    #print("stock amount = ", size[temp_j])
                    fee_price_i = (price[i]*size[i])*(fee_main/10)
                    fee_price_j = (price[temp_j]*size[temp_j])*(fee_main/10)
                    total_fee = fee_price_i + fee_price_j
                    #print("fee price[i] = ", fee_price_i)
                    #print("fee price[temp_j] = ", fee_price_j)
                    #print("total fee = ", total_fee)
                    real = (price[i]*size[temp_j]) - (size[temp_j] * price[temp_j])
                    profit = real + profit - total_fee
                    #print("real01 = ", real)
                    #print("size before sell")
                    #print("size before sell", size[i])
                    
                    temp = size[i] - size[temp_j]
                    temp2 = size[i]
                    #size[i] = temp2 - temp #reduce size in size[i]
                    size[i] = temp #reduce size in size[i]
                    #print("over size = ", temp)
                    #print("size[i] = ", size[i])
                    #print("stock_amount before sell = ", size[temp_j])
                    size[temp_j] = 9999 ## we don't need to use this array anymore
                    #print("stock_amount after sell = ", size[temp_j])
                    #print("i before i -", i)
                    t = 1
                    #print("\n")
                    ks = 1

            if ks == 0:
                #print("cannot find price > price[j]")
                #print("check all stock still cannot sell so we force sell negative(at best price)")
                j = 0
                temp_price = 0
                while j < i:
                    if side[j] == "Buy" and size[j] != 9999:
                        if temp_price == 0:

                            temp_price = price[j]
                            temp_stock = size[j]
                            temp_j = j
                            
                        if temp_price >= price[j] and price[j] != 9999:
                            #print("temp price < price")
                            temp_price = price[j]
                            temp_stock = size[j]
                            temp_j = j
                            #print("temp price = ", temp_price)
                            #print("temp stock = ", temp_stock)
                    j = j + 1
                #print("finaly temp price = ", temp_price)
                #print("fnaly temp stock = ", temp_stock)
                #print("price [j] = ", price[temp_j])
                #print("size [j] = ", size[temp_j])
                #print("j = ", j)
                #print("temp j = ", temp_j)
                if size[i] < size[temp_j] and size[i] != 9999:
                    #print("size < stock amount")
                    #print("size = ", size[i])
                    #print("at price", price[i])
                    #print("stock price = ", price[temp_j])
                    #print("stock amount = ", size[temp_j])
                    fee_price_i = (price[i]*size[i])*(fee_main/10)
                    fee_price_j = (price[temp_j]*size[i])*(fee_main/10)
                    total_fee = fee_price_i + fee_price_j
                    #print("fee price[i] = ", fee_price_i)
                    #print("fee price[temp_j] = ", fee_price_j)
                    #print("total fee = ", total_fee)
                    real = (price[i]*size[i]) - (size[i] * price[temp_j])
                    profit = real + profit - total_fee
                    #print("real = ", real)
                    #print("realzed - fee = ", real - total_fee)
                    size[temp_j] = size[temp_j] - size[i]  ### reduce stock[j] because sold out for size[i]
                    #print("stock_amount after sell = ", size[temp_j])
                    #print("\n")
                    size[i] = 9999
                    #print("size[i] = ", size[i])

                if size[i] == size[temp_j] and size[temp_j] != 9999 and size[i] != 9999:
                    #print("size == stock amount")
                    #print("size = ", size[i])
                    #print("at price", price[i])
                    #print("stock price = ", price[temp_j])
                    #print("stock amount = ", size[temp_j])
                    fee_price_i = (price[i]*size[i])*(fee_main/10)
                    fee_price_j = (price[temp_j]*size[i])*(fee_main/10)
                    total_fee = fee_price_i + fee_price_j
                    #print("fee price[i] = ", fee_price_i)
                    #print("fee price[temp_j] = ", fee_price_j)
                    #print("total fee = ", total_fee)
                    real = (price[i]*size[i]) - (size[i] * price[temp_j])
                    profit = real + profit - total_fee
                    #print("real = ", real)
                    #print("realzed - fee = ", real - total_fee)
                    size[temp_j] = 9999
                    size[i] = 9999
                    #print("i = ",i)
                    #print("size[i] = ", size[i])
                    #print("stock_amount after sell = ", size[temp_j])
                    price[j] = 9999
                    price[i] = 9999
                    #print("make price j and i = 9999", price[j])
                    #print("price i = 9999", price[i])
                    
                        

                if size[i] > size[temp_j] and size[temp_j] != 9999 and size[i] != 9999:
                    #print("size > stock amount")
                    #print("size = ", size[i])
                    #print("at price", price[i])
                    #print("stock price = ", price[temp_j])
                    #print("stock amount = ", size[temp_j])
                    fee_price_i = (price[i]*size[i])*(fee_main/10)
                    fee_price_j = (price[temp_j]*size[temp_j])*(fee_main/10)
                    total_fee = fee_price_i + fee_price_j
                    #print("fee price[i] = ", fee_price_i)
                    #print("fee price[temp_j] = ", fee_price_j)
                    #print("total fee = ", total_fee)
                    real = (price[i]*size[temp_j]) - (size[temp_j] * price[temp_j])
                    profit = real + profit - total_fee
                    #print("real01 = ", real)
                    #print("size before sell")
                    #print("size before sell", size[i])
                
                    temp = size[i] - size[temp_j]
                    temp2 = size[i]
                    #size[i] = temp2 - temp #reduce size in size[i]
                    size[i] = temp #reduce size in size[i]
                    #print("over size = ", temp)
                    #print("size[i] = ", size[i])
                    #print("stock_amount before sell = ", size[temp_j])
                    size[temp_j] = 9999 ## we don't need to use this array anymore
                    #print("stock_amount after sell = ", size[temp_j])
                    #print("i before i -", i)
                    t = 1
                    #print("\n")
                
                    
            

            
        if side[i] == "Buy":
            #print("side[i] = Buy")
            #print("find to side =[i] = sell so skip this (j = i)")
            j = i

        if size[i] == 9999:
            #print("skip check sold out")
            #size alerady sold out we skip
            j = i


        if i == j + 1 and size[i] != 9999 and k != 0:
            #print("check all stock still cannot sell so we force sell negative(at best price)")
            j = 0
            temp_price = 0
            while j < i:
                if side[j] == "Buy" and size[j] != 9999:
                    if temp_price == 0:
                        temp_price = price[j]
                        temp_price = price[j]
                        temp_stock = size[j]
                        temp_j = j
                        
                    if temp_price >= price[j]:
                        #print("temp price < price")
                        #print("temp price", temp_price)
                        temp_price = price[j]
                        temp_stock = size[j]
                        temp_j = j
                j = j + 1
            #print("finaly temp price = ", temp_price)
            #print("fnaly temp stock = ", temp_stock)
            #print("price [j] = ", price[temp_j])
            #print("size [j] = ", size[temp_j])
            
            if size[i] < size[temp_j] and size[i] != 9999:
                #print("size < stock amount")
                #print("size = ", size[i])
                #print("at price", price[i])
                #print("stock price = ", price[j])
                #print("stock amount = ", size[temp_j])
                fee_price_i = (price[i]*size[i])*(fee_main/10)
                fee_price_j = (price[temp_j]*size[i])*(fee_main/10)
                total_fee = fee_price_i + fee_price_j
                #print("fee price[i] = ", fee_price_i)
                #print("fee price[temp_j] = ", fee_price_j)
                #print("total fee = ", total_fee)
                real = (price[i]*size[i]) - (size[i] * price[temp_j])
                profit = real + profit - total_fee
                #print("real = ", real)
                #print("realzed - fee = ", real - total_fee)
                size[temp_j] = size[temp_j] - size[i]  ### reduce stock[j] because sold out for size[i]
                #print("stock_amount after sell = ", size[temp_j])
                #print("\n")
                size[i] = 9999
                #print("size[i] = ", size[i])

            if size[i] == size[temp_j] and size[temp_j] != 9999 and size[i] != 9999:
                #print("size == stock amount")
                #print("size = ", size[i])
                #print("at price", price[i])
                #print("stock price = ", price[temp_j])
                #print("stock amount = ", size[temp_j])
                fee_price_i = (price[i]*size[i])*(fee_main/10)
                fee_price_j = (price[temp_j]*size[i])*(fee_main/10)
                total_fee = fee_price_i + fee_price_j
                #print("fee price[i] = ", fee_price_i)
                #print("fee price[temp_j] = ", fee_price_j)
                #print("total fee = ", total_fee)
                real = (price[i]*size[i]) - (size[i] * price[temp_j])
                profit = real + profit - total_fee
                #print("real = ", real)
                #print("realzed - fee = ", real - total_fee)
                size[temp_j] = 9999
                size[i] = 9999
                #print("realised profit = ", profit)
                #print("i = ",i)
                #print("size[i] = ", size[i])
                #print("stock_amount after sell = ", size[temp_j])
                    

            if size[i] > size[temp_j] and size[temp_j] != 9999 and size[i] != 9999:
                #print("size > stock amount")
                #print("size = ", size[i])
                #print("at price", price[i])
                #print("stock price = ", price[j])
                #print("stock amount = ", size[temp_j])
                real = (price[i]*size[temp_j]) - (size[temp_j] * price[temp_j])
                profit = real + profit
                #print("real01 = ", real)
                #print("size before sell", size[i])
                
                temp = size[i] - size[temp_j]
                temp2 = size[i]
                #size[i] = temp2 - temp #reduce size in size[i]
                size[i] = temp #reduce size in size[i]
                #print("over size = ", temp)
                #print("size[i] = ", size[i])
                #print("stock_amount before sell = ", size[temp_j])
                size[temp_j] = 9999 ## we don't need to use this array anymore
                #print("stock_amount after sell = ", size[temp_j])
                #print("i before i -", i)
                t = 1
                print("\n")

        if t == 1:
            #print("t = 1 check i value", t)
            #print("check i value = ", i)
            i  = i - 1
            #print("i = i -  1", i)
        #print("i  = ", i)
        #print("j  = ", j)
        j = j + 1
    print("profit = ", profit)
    print("\n")
    i = i + 1

#for i in range(tempi):
    #print("side = ",side[i])
    #print("price = ",price[i])
    #print("size = ", size[i])
    #print("\n")

