'''
Find a Pair
Given a list of numbers and a target sum, find a pair of numbers in 
the list that add to the target sum. What is the time complexity of 
your solution? How can you improve it?

Example: `find_pair(numbers=[1, 5, 4, 1, 7, -2], target=3)` 
should return `(5, -2)`

Stretch goal: Find all pairs of numbers that add to the target sum. 
Return a list of pairs.
Example: `find_all_pairs(numbers=[3, 5, 7, 2, 4, 0], target=7)` 
should return `[(3, 4), (5, 2), (7, 0)]`
'''

def find_all_pairs(numbers=[], target=0):
  return [(i,j) for ind,i in enumerate(numbers) for j in numbers[ind+1:] if i+j == target]

def test():
  print("hallo")
  print(find_all_pairs([1,5,4,1,7,-2],3))
  print(find_all_pairs([],2))
  print(find_all_pairs([5,6,7,8,9],15))
  print(find_all_pairs([9,8,7,6,5],16))

if __name__ == "__main__":
  test()