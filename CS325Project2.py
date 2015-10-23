def get_coins():
    
    coins = []
    with open('coin1.txt') as f:
        while True:
            line1 = f.readline().strip().strip(']').strip('[')
            line2 = f.readline().strip()
            line1arr = [int(x) for x in line1.split(', ')]
            if not line2:
                break
            coins.append([int(line2), line1arr])
            
            
    return coins
    
coins = get_coins()

coins = coinarr[1]
value = coinarr[0]

def changeslow(coinarr, value, coins, amt, i):
    
    if value == coinarr[i]:
        return coins[i] + 1, amt + 1
    else:
        
        

    
    for x in xrange(len(coins)):
        