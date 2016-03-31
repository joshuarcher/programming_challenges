'''
Fix the Stack
Your friend's dish-washing robot stacked the plates incorrectly 
and the first two items were always placed in the wrong order. :-( 
To help your friend fix this egregious robot error, write a function 
that takes a stack as input and swaps the bottom two items only.
'''

def fix_stack_iter(stack=[]):
  if len(stack) <= 1:
    return stack
  temp_stack = []

  while len(stack) is not 0:
    temp_stack.append(stack.pop())

  temp_one, temp_two = temp_stack.pop(), temp_stack.pop()
  stack.append(temp_two)
  stack.append(temp_one)

  while len(temp_stack) is not 0:
    stack.append(temp_stack.pop())
  return stack

def test():
  stack = [4,5,3,2,1]
  print("hallo")
  print(fix_stack_iter(stack))

if __name__ == "__main__":
  test()