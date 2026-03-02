
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung03/al/aufgabe02
# Version: Sun Mar  1 18:06:44 CET 2026

import enum
from uebung03.al.aufgabe02.no_such_node_exception import NoSuchNodeException


ROOT_INDEX = 1

class VectorTree:
  
  class _child_side(enum.Enum):
    LEFT = enum.auto()
    RIGHT = enum.auto()

  def __init__(self):
    self._binary_tree = []
    self._binary_tree.append(None)
    self._binary_tree.append(None)
    self._size = 0
    
  def root(self):
    # TODO: Implement here...
    pass
  
  def set_root(self, root):
    # TODO: Implement here...
    pass
    
  def parent(self, child):
    # TODO: Implement here...
    pass
    
  def left_child(self, parent):
    # TODO: Implement here...
    pass

  def right_child(self, parent):
    # TODO: Implement here...
    pass

  def is_internal(self, node):
    # TODO: Implement here...
    pass

  def is_external(self, node):
    # TODO: Implement here...
    pass
  
  def is_root(self, node):
    # TODO: Implement here...
    pass

  def set_right_child(self, parent, child):
    # TODO: Implement here...
    pass
  
  def set_left_child(self, parent, child):
    # TODO: Implement here...
    pass
      
  def remove_right_child(self, parent):
    # TODO: Implement here...
    pass

  def remove_left_child(self, parent):
    # TODO: Implement here...
    pass
       
  def size(self):
    # TODO: Implement here...
    pass

  def print_vector(self, message):
    print("\n" + message)
    print(self._binary_tree)
