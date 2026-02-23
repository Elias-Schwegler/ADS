
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung02/ml/aufgabe03
# Version: Sat Feb 21 16:14:44 CET 2026

from uebung02.ml.aufgabe03.empty_stack_exception import EmptyStackException
import sys


class StackImplementation:
  '''
  Stack: a collection of objects that are inserted and removed according 
  to the last-in first-out principle.
  '''
  # --- nested _Node class: -----------------
  class _Node:
    
    def __init__(self, elem):
      self._element = elem
      self._next = None
    
    def append_node(self, nextNode):
      self._next = nextNode
    
    def get_next(self):
      return self._next
    
    def get_element(self):
      return self._element


  # --- stack methods: -----------------

  def __init__(self):
    self._top = None
    self._size = 0
  
  def __len__(self):
    return self._size
  
  def size(self):
    return self.__len__()

  def is_empty(self):
    return self._size == 0
  
  def top(self):
    if self._size == 0:
      raise EmptyStackException("Could not get top of stack because stack is empty.")
    return self._top.get_element()
  
  def push(self, element):
    new_node = self._Node(element)
    new_node.append_node(self._top)
    self._top = new_node
    self._size += 1
    
  def pop(self):
    if self._size == 0:
      raise EmptyStackException("Could not remove top of stack because stack is empty.")
    top_node = self._top
    self._top = top_node.get_next()
    self._size -= 1
    return top_node.get_element()
  
  def printout(self):
    print("Stack: (", self._to_string(self._top, ""), ")")
    
  def _to_string(self, node, content):
    if node == None:
      return content
    if not content == "":
      content += ", "
    content += str(node.get_element())
    return self._to_string(node.get_next(), content)

    
if __name__ == '__main__':
  stack = StackImplementation()
  stack.printout()
  TEST_SIZE = 4
  for i in range(TEST_SIZE):
    stack.push(i)
    stack.printout()
    if stack.size() != i+1: 
      print("ERROR: Stack.size() != ", i+1)
      sys.exit()
    if stack.top() != i: 
      print("ERROR: Stack.top() != ", i)
      sys.exit()
  for i in range(TEST_SIZE-1, 0, -1):
    if stack.pop() != i: 
      print("ERROR: Stack.pop() != ", i)
      sys.exit()
    stack.printout()
    if stack.size() != i: 
      print("ERROR: Stack.size() != ", i)
      sys.exit()
    if stack.top() != i-1: 
      print("ERROR: Stack.top() != ", i-1)
      sys.exit()
  if stack.pop() != 0: 
    print("ERROR: Stack.pop() != ", 0)
    sys.exit()
  stack.printout()
  if not stack.is_empty(): 
    print("ERROR: Stack.empty() != true")
    sys.exit()
  if stack.size() != 0: 
    print("ERROR: Stack.size() != 0")
    sys.exit()
  try:
    stack.top()
    print("ERROR: no EmptyStackException for stack.top()!")
    sys.exit()
  except EmptyStackException:
    pass
  try:
    stack.pop()
    print("ERROR: no EmptyStackException for stack.pop()!")
    sys.exit()
  except EmptyStackException:
    pass
    

""" Session-Log:

Stack: (  )
Stack: ( 0 )
Stack: ( 1, 0 )
Stack: ( 2, 1, 0 )
Stack: ( 3, 2, 1, 0 )
Stack: ( 2, 1, 0 )
Stack: ( 1, 0 )
Stack: ( 0 )
Stack: (  )

""" 

