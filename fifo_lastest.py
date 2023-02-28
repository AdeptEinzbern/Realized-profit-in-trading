# This script calculates the realized profit from a list of transactions in a CSV file.
import csv
import pandas as pd

#Read in the CSV file using pandas.
df = pd.read_csv('fifo_test - Copy.csv')

# Extract the relevant data from the DataFrame.
side = df['Side'] # The side of each transaction (buy or sell).
price = df['Price'] # The price of each transaction.
size = df['Size'] # The size of each position.
fee = df['Fee'] # The fee paid for each transaction.
currency = df['Fee Currency'] # The currency of the fee (may not be the same as the transaction currency).
tempi = len(side) - 1 # The number of transactions in the CSV file.

# Initialize variables.
profit = 0  # The total realized profit.
fee_main = 0.1  # The percentage fee charged for each transaction (assumes maker and taker fees are the same).
fee_second = 0.1  # The percentage fee charged for each transaction (assumes maker and taker fees are the same).
i = 0  # The index of the current sell transaction.
j = 0  # The index of the current buy transaction.
fix_step = 0.250  # The minimum price difference between two transactions (close positive).

# Loop through all sell transactions.

while i <= tempi:
    # Loop through all transactions
    j = 0
    t = 0    ## t is checker if t = 1 we shift i value
    while j < i: 
        print("i start = ", i)
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
                    print("side = buy and size[j] != 9999")
                    
                    if temp_price == 0:
                        print("set temp_price = 0")
                        temp_price = price[j]
                        temp_price = price[j]
                        temp_stock = size[j]
                        temp_j = j
                    #if temp_price < price[j] and size[j] != 9999 and (price[i] + fix_step) > price[j]:
                    if price[j] < price[i] and  size[j] != 9999:
                        if temp_price < price[j] and size[j] != 9999 and (price[i] + fix_step) > price[j]:
                            print("temp price < price set temp price = price[j]")
                            print("temp price", temp_price)
                            print("price j = " ,price[j])
                            temp_price = price[j]
                            temp_stock = size[j]
                            temp_j = j
                    print("j in side sell side[i] = ", j)
                j = j + 1
                
                print("finaly temp price = ", temp_price)
                print("fnaly temp stock = ", temp_stock)
                print("price [j] = ", price[temp_j])
                print("size [j] = ", size[temp_j])
                if size[i] < size[temp_j] and size[i] != 9999 and price[i]+fix_step > price[temp_j] and size[temp_j] != 9999 and j == i:
                    print("size < stock amount")
                    print("size = ", size[i])
                    print("at price", price[i])
                    print("stock price = ", price[temp_j])
                    print("stock amount = ", size[temp_j])
                    fee_price_i = (price[i]*size[i])*(fee_main/100)
                    fee_price_j = (price[temp_j]*size[i])*(fee_main/100)
                    total_fee = fee_price_i + fee_price_j
                    print("fee price[i] = ", fee_price_i)
                    print("fee price[temp_j] = ", fee_price_j)
                    print("total fee = ", total_fee)
                    real = (price[i]*size[i]) - (size[i] * price[temp_j])
                    profit = real + profit - total_fee
                    print("real = ", real)
                    print("realzed - fee = ", real - total_fee)
                   
                    size[temp_j] = size[temp_j] - size[i]  ### reduce stock[j] because sold out for size[i]
                    print("stock_amount after sell = ", size[temp_j])
                    size[i] = 9999
                    print("size[i] = ", size[i])
                    print("\n")
                    
                    ks = 1

                if size[i] == size[temp_j] and size[temp_j] != 9999 and size[i] != 9999 and price[i]+fix_step > price[temp_j] and j == i:
                    print("size == stock amount")
                    print("size = ", size[i])
                    print("at price", price[i])
                    print("stock price = ", price[temp_j])
                    print("stock amount = ", size[temp_j])
                    fee_price_i = (price[i]*size[i])*(fee_main/100)
                    fee_price_j = (price[temp_j]*size[i])*(fee_main/100)
                    total_fee = fee_price_i + fee_price_j
                    print("fee price[i] = ", fee_price_i)
                    print("fee price[temp_j] = ", fee_price_j)
                    print("total fee = ", total_fee)
                    real = (price[i]*size[i]) - (size[i] * price[temp_j])
                    profit = real + profit - total_fee
                    print("real = ", real)
                    print("realzed - fee = ", real - total_fee)
                    size[temp_j] = 9999
                    size[i] = 9999
                    #print("realised profit = ", profit)
                    print("i = ",i)
                    print("size[i] = ", size[i])
                    print("stock_amount after sell = ", size[temp_j])
                    ks = 1
                        

                if size[i] > size[temp_j] and size[temp_j] != 9999 and size[i] != 9999 and price[i]+fix_step > price[temp_j] and j == i:
                    print("size > stock amount")
                    print("size = ", size[i])
                    print("at price", price[i])
                    print("stock price = ", price[temp_j])
                    print("stock amount = ", size[temp_j])
                    fee_price_i = (price[i]*size[i])*(fee_main/100)
                    fee_price_j = (price[temp_j]*size[temp_j])*(fee_main/100)
                    total_fee = fee_price_i + fee_price_j
                    print("fee price[i] = ", fee_price_i)
                    print("fee price[temp_j] = ", fee_price_j)
                    print("total fee = ", total_fee)
                    real = (price[i]*size[temp_j]) - (size[temp_j] * price[temp_j])
                    profit = real + profit - total_fee
                    print("real01 = ", real)
                    print("realzed - fee = ", real - total_fee)
                    print("size before sell", size[i])
                    temp = size[i] - size[temp_j]
                    temp2 = size[i]
                    #size[i] = temp2 - temp #reduce size in size[i]
                    size[i] = temp #reduce size in size[i]
                    print("over size = ", temp)
                    print("size[i] after sell = ", size[i])
                    print("stock_amount before sell = ", size[temp_j])
                    size[temp_j] = 9999 ## we don't need to use this array anymore
                    print("stock_amount after sell = ", size[temp_j])
                    print("i before i -", i)
                    t = 1
                    print("\n")
                    ks = 1

            if ks == 0:
                print("\n")
                print("find all [j] (buy side still cannot match order sell)")
                #print("check all stock still cannot sell so we force sell negative(at best price)")
                j = 0
                temp_price = 0
                while j < i:
                    if side[j] == "Buy" and size[j] != 9999:
                        if temp_price == 0:
                            print("set temp prce == 0 k = 0")
                            temp_price = price[j]
                            temp_stock = size[j]
                            temp_j = j
                            
                        if temp_price >= price[j] and price[j] != 9999:
                            print("temp price < price k = 0")
                            temp_price = price[j]
                            temp_stock = size[j]
                            temp_j = j
                            print("temp price = ", temp_price)
                            print("temp stock = ", temp_stock)
                    j = j + 1
                print("finaly temp price = k=0", temp_price)
                print("fnaly temp stock = k=0", temp_stock)
                print("price [j] = k=0", price[temp_j])
                print("size [j] = k=0", size[temp_j])
                print("j = k=0", j)
                print("temp j = k=0", temp_j)
                if size[i] < size[temp_j] and size[i] != 9999 and j == i:
                    print("size < stock amount")
                    print("size = ", size[i])
                    print("at price", price[i])
                    print("stock price = ", price[temp_j])
                    print("stock amount = ", size[temp_j])
                    fee_price_i = (price[i]*size[i])*(fee_main/100)
                    fee_price_j = (price[temp_j]*size[i])*(fee_main/100)
                    total_fee = fee_price_i + fee_price_j
                    print("fee price[i] = ", fee_price_i)
                    print("fee price[temp_j] = ", fee_price_j)
                    print("total fee = ", total_fee)
                    real = (price[i]*size[i]) - (size[i] * price[temp_j])
                    profit = real + profit - total_fee
                    print("real = ", real)
                    print("realzed - fee = ", real - total_fee)
                    size[temp_j] = size[temp_j] - size[i]  ### reduce stock[j] because sold out for size[i]
                    print("stock_amount after sell = ", size[temp_j])
                    print("\n")
                    size[i] = 9999
                    print("size[i] = ", size[i])

                if size[i] == size[temp_j] and size[temp_j] != 9999 and size[i] != 9999 and j == i:
                    print("size == stock amount")
                    print("size = ", size[i])
                    print("at price", price[i])
                    print("stock price = ", price[temp_j])
                    print("stock amount = ", size[temp_j])
                    fee_price_i = (price[i]*size[i])*(fee_main/100)
                    fee_price_j = (price[temp_j]*size[i])*(fee_main/100)
                    total_fee = fee_price_i + fee_price_j
                    print("fee price[i] = ", fee_price_i)
                    print("fee price[temp_j] = ", fee_price_j)
                    print("total fee = ", total_fee)
                    real = (price[i]*size[i]) - (size[i] * price[temp_j])
                    profit = real + profit - total_fee
                    print("real = ", real)
                    print("realzed - fee = ", real - total_fee)
                    size[temp_j] = 9999
                    size[i] = 9999
                    print("i = ",i)
                    print("size[i] = ", size[i])
                    print("stock_amount after sell = ", size[temp_j])
                    price[j] = 9999
                    price[i] = 9999
                    print("make price j and i = 9999", price[j])
                    print("price i = 9999", price[i])
                    
                        

                if size[i] > size[temp_j] and size[temp_j] != 9999 and size[i] != 9999 and j == i:
                    print("size > stock amount")
                    print("size = ", size[i])
                    print("at price", price[i])
                    print("stock price = ", price[temp_j])
                    print("stock amount = ", size[temp_j])
                    fee_price_i = (price[i]*size[i])*(fee_main/100)
                    fee_price_j = (price[temp_j]*size[temp_j])*(fee_main/100)
                    total_fee = fee_price_i + fee_price_j
                    print("fee price[i] = ", fee_price_i)
                    print("fee price[temp_j] = ", fee_price_j)
                    print("total fee = ", total_fee)
                    real = (price[i]*size[temp_j]) - (size[temp_j] * price[temp_j])
                    profit = real + profit - total_fee
                    print("real01 = ", real)
                    print("size before sell")
                    print("size before sell", size[i])
                
                    temp = size[i] - size[temp_j]
                    temp2 = size[i]
                    #size[i] = temp2 - temp #reduce size in size[i]
                    size[i] = temp #reduce size in size[i]
                    print("over size = ", temp)
                    print("size[i] = ", size[i])
                    print("stock_amount before sell = ", size[temp_j])
                    size[temp_j] = 9999 ## we don't need to use this array anymore
                    print("stock_amount after sell = ", size[temp_j])
                    print("i before i -", i)
                    t = 1
                    print("\n")
                
                    
            

            
        if side[i] == "Buy":
            print("side[i] = Buy")
            #print("find to side =[i] = sell so skip this (j = i)")
            j = i

        if size[i] == 9999:
            print("skip check sold out")
            #size alerady sold out we skip
            j = i


        if i == j + 1 and size[i] != 9999 and k != 0:
            print("check all stock still cannot sell so we force sell negative(at best price)")
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
                        print("temp price < price force sell negative method")
                        print("temp price", temp_price)
                        temp_price = price[j]
                        temp_stock = size[j]
                        temp_j = j
                j = j + 1
            print("finaly temp price = ", temp_price)
            print("fnaly temp stock = ", temp_stock)
            print("price [j] = ", price[temp_j])
            print("size [j] = ", size[temp_j])
            print("ik = ", i)
            print("jk = ", j)
            
            if size[i] < size[temp_j] and size[i] != 9999 and j == i:
                print("size < stock amount")
                print("size = ", size[i])
                print("at price", price[i])
                print("stock price = ", price[j])
                print("stock amount = ", size[temp_j])
                fee_price_i = (price[i]*size[i])*(fee_main/100)
                fee_price_j = (price[temp_j]*size[i])*(fee_main/100)
                total_fee = fee_price_i + fee_price_j
                print("fee price[i] = ", fee_price_i)
                print("fee price[temp_j] = ", fee_price_j)
                print("total fee = ", total_fee)
                real = (price[i]*size[i]) - (size[i] * price[temp_j])
                profit = real + profit - total_fee
                print("real = ", real)
                print("realzed - fee = ", real - total_fee)
                size[temp_j] = size[temp_j] - size[i]  ### reduce stock[j] because sold out for size[i]
                print("stock_amount after sell = ", size[temp_j])
                print("\n")
                size[i] = 9999
                print("size[i] = ", size[i])

            if size[i] == size[temp_j] and size[temp_j] != 9999 and size[i] != 9999 and j == i:
                print("size == stock amount")
                print("size = ", size[i])
                print("at price", price[i])
                print("stock price = ", price[temp_j])
                print("stock amount = ", size[temp_j])
                fee_price_i = (price[i]*size[i])*(fee_main/100)
                fee_price_j = (price[temp_j]*size[i])*(fee_main/100)
                total_fee = fee_price_i + fee_price_j
                print("fee price[i] = ", fee_price_i)
                print("fee price[temp_j] = ", fee_price_j)
                print("total fee = ", total_fee)
                real = (price[i]*size[i]) - (size[i] * price[temp_j])
                profit = real + profit - total_fee
                print("real = ", real)
                print("realzed - fee = ", real - total_fee)
                size[temp_j] = 9999
                size[i] = 9999
                print("realised profit = ", profit)
                print("i = ",i)
                print("size[i] = ", size[i])
                print("stock_amount after sell = ", size[temp_j])
                    

            if size[i] > size[temp_j] and size[temp_j] != 9999 and size[i] != 9999 and j == i:
                print("size > stock amount")
                print("size = ", size[i])
                print("at price", price[i])
                print("stock price = ", price[j])
                print("stock amount = ", size[temp_j])
                real = (price[i]*size[temp_j]) - (size[temp_j] * price[temp_j])
                profit = real + profit
                print("real01 = ", real)
                print("size before sell", size[i])
                
                temp = size[i] - size[temp_j]
                temp2 = size[i]
                #size[i] = temp2 - temp #reduce size in size[i]
                size[i] = temp #reduce size in size[i]
                print("over size = ", temp)
                print("size[i] = ", size[i])
                print("stock_amount before sell = ", size[temp_j])
                size[temp_j] = 9999 ## we don't need to use this array anymore
                print("stock_amount after sell = ", size[temp_j])
                print("i before i -", i)
                t = 1
                print("\n")

        if t == 1:
            print("t = 1 check i value", t)
            print("check i value = ", i)
            i  = i - 1
            print("i = i -  1", i)
        print("i  = ", i)
        print("j  = ", j)
        j = j + 1
    print("profit = ", profit)
    print("\n")
    i = i + 1

for i in range(tempi):
    print("side = ",side[i])
    print("price = ",price[i])
    print("size = ", size[i])
    print("\n")

