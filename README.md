# trading_fifo
ArtyEth_trades.csv name of file we need to read,
fifo_test.csv show how accurate hand vs automate.

One of most wierdest thing for trader who especially spot trading in crypto,
I hope this help you find out how much realised profit you had.

The logic is simple 
We have 3 scenario, the first one is our sell position size lesser than stock we have buy,
realised profit = (current price * position size) - (old price * position size).

the secondary scenario is when our sell position size is bigger than stock we have buy,
realised profit 01 = (current price * position size) - (old price * position size)
realised profit 02 = ((current price * position size(left) - (old price(+1 array) * position size(left)))
realised profit = realised 01 + 02.

the last scenario is our sell position size is equal to stock we have buy,
realised profit = realised profit = (current price * position size) - (old price * position size).
