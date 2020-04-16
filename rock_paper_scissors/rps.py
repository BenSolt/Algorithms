#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    #MY CODE
  if n <= 1:
    return 0
  elif n == 1:
    return 1
  elif n == 2:
    return 2
  

  # else:
  #   return rock_paper_scissors(n-1) + rock_paper_scissors(n-2) + rock_paper_scissors(n-3)
 
for i in range(3):
   print(rock_paper_scissors(i))

print(rock_paper_scissors(3))
  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')