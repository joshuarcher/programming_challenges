'''
Make Change
You're tasked with writing a function for a cash register that shows 
a teller how to make change for a customer after a transaction. Given 
a list of coin denominations available and an amount of money, return 
a list of what coins to give as change.

Example: `change(coins=[1, 5, 10, 25], amount=42)` should return 
`[25, 10, 5, 1, 1]`

Can you implement this recursively? Does it make it easier to write, 
or shorter code?

Stretch goal: Find all possible combinations of coins to make 
change and return the one that requires giving the fewest number of coins.

use the next largest coin until you cant use it

can I use a quarter? sure, use it and call the recursive call
can I use a quarter? sure, use it and call the recursive call
can I use a quarter? no, recursive call without quarters
'''

def get_change(coins=[], amount=0):
  coins.sort()
  change = []
  if amount is 0:
    return change
  while amount - coins[-1] >= 0:
    amount = amount - coins[-1]
    change.append(coins[-1])

  change.extend(get_change(coins[:-1], amount))
  return change

def test():
  print("hallo")
  print(get_change([25,5,10,1], 42))
  print(get_change([25,5,10,1], 100))

if __name__ == "__main__":
  test()