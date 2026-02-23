
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung01/ml/aufgabe04
# Version: Fri Feb 13 18:34:31 CET 2026

import random
import sys
from time import time


def insertion_sort(data):
  """Sorts a list with the Insertion-Sort algorithm.
  
  p   List of comparable elements which will be sorted.
  """
  for k in range(1, len(data)):  
    cur = data[k]  
    j = k  
    while j > 0 and data[j - 1] > cur:  
      data[j] = data[j - 1]
      j -= 1
    data[j] = cur  
    
    
def verify(orginalData, sortedData):
  correctSorted = orginalData.copy()
  correctSorted.sort()
  for i in range(len(orginalData)):
    if correctSorted[i] != sortedData[i]:
      print("ERROR: wrong sorted!")
      print("Orginal : ", orginalData)
      print("Sorted  : ", sortedData)
      print(f"index[{i}]: should be: {correctSorted[i]}, but is: {sortedData[i]}")
      sys.exit(1)
  

if __name__ == '__main__':
  
  data = [5, 4, 2, 3, 1]
  orginalData = data.copy()
  print(data)
  
  insertion_sort(data)
  
  print(data)
  verify(orginalData, data)
  
  # Makeing some test to measure the time needed of insertion_sort().
  # Creating int-lists, beginning with length of 2^minExponent
  # until the last array with length of 2^maxExponent.
  minExponent =  9
  maxExponent = 13
  lastTime = sys.float_info.max
  for exp in range(minExponent, maxExponent + 1):
    length = pow(2, exp)
    MEASUREMENTS = 10
    minTime = sys.float_info.max
    for i in range(MEASUREMENTS):
      data = list(range(length))
      random.shuffle(data)
      start = time()
      insertion_sort(data)
      end = time()
      timeSpent = end - start
      if timeSpent < minTime:
        minTime = timeSpent
    print(f"List-Size: {length:6,d}         Time: {minTime*1e3:7.1f} ms          Ratio to last: {minTime / lastTime:.1f}")
    lastTime = minTime
    
    
  """ Session-Log:
  
  [5, 4, 2, 3, 1]
  [1, 2, 3, 4, 5]
  List-Size:    512         Time:     3.7 ms          Ratio to last: 0.0
  List-Size:  1,024         Time:    16.3 ms          Ratio to last: 4.4
  List-Size:  2,048         Time:    70.4 ms          Ratio to last: 4.3
  List-Size:  4,096         Time:   280.9 ms          Ratio to last: 4.0
  List-Size:  8,192         Time:  1133.7 ms          Ratio to last: 4.0
  
  """  
  
  
