def make_bricks(small, big, goal):
  if goal/5 <= big and (goal%5) <= small:
    return True
  elif goal - big*5 <= small and goal - big*5 >= 0:
    return True
  return False

def lone_sum(a, b, c):
  temp = 0
  if a == b:
    if a == c:
      c = 0
    a = 0
    b = 0
  elif a == c:
    a = 0
    c = 0
  elif b == c:
    b = 0
    c = 0
  return a + b + c

def lucky_sum(a, b, c):
  if a == 13:
    return 0
  elif b == 13:
    return a
  elif c == 13:
    return a + b
  return a + b + c

def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)
  
def fix_teen(n):
  if n == 13 or n == 14:
    return 0
  elif n >= 17 and n <= 19:
    return 0
  else:
    return n

def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
  
def round10(n):
  if (n%10) < 5:
    return n - (n%10)
  else:
    return n + 10 - (n%10)

def close_far(a, b, c):
  if abs(a-b) < 2 and abs(a-c) > 1 and abs(b-c) > 1:
    return True
  if abs(a-c) <2 and abs(a-b) > 1 and  abs(b-c) > 1:
    return True
  return False

def make_chocolate(small, big, goal):
  if goal/5 <= big and goal%5 <= small:
    return goal%5
  if goal - big*5 <= small and goal - big*5 >= 0:
    return goal - big*5
  return -1
