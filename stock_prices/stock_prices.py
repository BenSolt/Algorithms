#!/usr/bin/python

import argparse

def find_max_profit(prices):
# MY CODE
  profit = [] #add prices too
#for loop
  for b in range(len(prices)):
   #for loop
    for s in range(b+1, len(prices)):
     #buy prices
     buy = prices[b]
     #sell prices
     sell = prices[s]
     #subtract sell from buy
     subtract = sell - buy
     #add subtract answer to profit array
     profit.append(subtract)
     #result = total of profit added.
     result = max(profit)
  return result
 
numberList = [5,245,53,36,125,759]
print('answer:', find_max_profit(numberList))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))