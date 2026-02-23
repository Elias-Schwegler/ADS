
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung02/al/aufgabe02
# Version: Sat Feb 21 16:12:32 CET 2026

from uebung02.al.aufgabe02.node import Node
from uebung02.al.aufgabe02.dequeue_empty_exception import DequeEmptyException


class DequeImplementation:
  '''
  Double linked list and DE-Queue (double ended queue: Deque)
  '''
  def __init__(self):
    self._header = Node()
    self._trailer = Node()
    self._header.set_next(self._trailer)
    self._trailer.set_prev(self._header)
    self._size = 0

  def insert_first(self, element):
    second = self._header.get_next()
    first = Node(element, self._header, second)
    second.set_prev(first)
    self._header.set_next(first)
    self._size += 1
    
  def remove_last(self): 
    if self.is_empty(): 
      raise DequeEmptyException("Deque is empty!")
    last = self._trailer.get_prev()
    e = last.get_element()
    secondtolast = last.get_prev()
    self._trailer.set_prev(secondtolast)
    secondtolast.set_next(self._trailer)
    self._size -= 1
    return e
    
  def remove_first(self): 
  
    # TODO: Implement here...
    pass
  
    
  def insert_last(self, element):
  
    # TODO: Implement here...
    pass
  
    
  def first(self): 
  
    # TODO: Implement here...
    pass
  
    
  def last(self): 
  
    # TODO: Implement here...
    pass
  
    
  def size(self):
  
    # TODO: Implement here...
    pass
  
    
  def is_empty(self):
  
    # TODO: Implement here...
    pass
  
  
  def __str__(self):
    node = self._header.get_next()
    elements = []
    while node != self._trailer:
      elements.append(str(node.get_element()))
      node = node.get_next()
    separator=", "
    return "[" + separator.join(elements) + "]"


if __name__ == '__main__':
  deque = DequeImplementation()
  deque.insert_first(3)
  deque.insert_first(2)
  deque.insert_first(1)   
  print(deque)
  deque.insert_last(4)
  deque.insert_last(5)
  deque.insert_last(6)
  print(deque)
  print("size  : " + str(deque.size()))
  print("empty : " + str(deque.is_empty()))
  print("first : " + str(deque.first()))
  print("last  : " + str(deque.last()))
  for i in range(3):
    print(str(deque.remove_first()), end = " ")
  print()
  for i in range(3):
    print(str(deque.remove_last()), end = " ")
  print()
  deque.remove_first()


""" Session-Log:

[1, 2, 3]
[1, 2, 3, 4, 5, 6]
size  : 6
empty : False
first : 1
last  : 6
1 2 3 
6 5 4 
Traceback (most recent call last):
  File "/home/tletsch/HSLU/FS26/ADS_Uebungen_Python/Uebungen/uebung02/al/aufgabe02/dequeue_implementation.py", line 102, in <module>
    deque.remove_first()
  File "/home/tletsch/HSLU/FS26/ADS_Uebungen_Python/Uebungen/uebung02/al/aufgabe02/dequeue_implementation.py", line 41, in remove_first
    raise DequeEmptyException("Deque is empty!")
uebung02.al.aufgabe02.dequeue_empty_exception.DequeEmptyException: Deque is empty!

"""   
