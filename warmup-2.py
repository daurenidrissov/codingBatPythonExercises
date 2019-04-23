def string_times(str, n):
  new = ""
  for i in range(n):
    new += str
  return new

def front_times(str, n):
  front = ""
  new = ""
  if len(str) < 3:
    front = str
  else:
    front = str[:3]
  
  for i in range(n):
    new += front
  return new

def string_bits(str):
  new = ""
  for i in range(len(str)):
    if i%2 == 0:
      new += str[i]
  return new

def string_splosion(str):
  new = ""
  for i in range(len(str)):
    new += str[:i+1]
  return new  

def last2(str):
  count = 0
  end = str[-2:]
  for i in range(len(str)-2):
    if str[i] is end[0] and str[i+1] is end[1]:
      count += 1
  return count

def array_count9(nums):
  count = 0
  for i in nums:
    if i == 9:
      count += 1
  return count

def array_front9(nums):
  for num in nums[:4]:
    if num == 9:
      return True
  return False 

def array123(nums):
  for i in range(len(nums)-2):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
      return True
  return False

def string_match(a, b):
  count = 0
  for i in range(min(len(a), len(b))-1):
    if a[i:i+2] == b[i:i+2]:
      count += 1
  return count
  