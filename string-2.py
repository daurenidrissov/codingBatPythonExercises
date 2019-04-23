def double_char(str):
  new = ""
  for i in str:
    new += i + i
  return new

def count_hi(str):
  count = 0
  for i in range(len(str)-1):
    if str[i] is 'h' and str[i+1] is 'i':
      count += 1
  return count

def cat_dog(str):
  cat, dog = 0, 0
  for i in range(len(str)-2):
    if str[i] is 'c' and str[i+1] is 'a' and str[i+2] is 't':
      cat += 1
    if str[i] is 'd' and str[i+1] is 'o' and str[i+2] is 'g':
      dog += 1
  return cat == dog

def count_code(str):
  count = 0
  for i in range(len(str)-3):
    if str[i] is 'c' and str[i+1] is 'o' and str[i+3] is 'e':
      count += 1
  return count

def end_other(a, b):
# return a[-len(b):].lower() == b.lower() or b[-len(a):].lower() == a.lower()
  return a.lower().endswith(b.lower()) or b.lower().endswith(a.lower())  

def xyz_there(str):
  for i in range(len(str)-2):
    if i is 0:
      if str[i] is 'x' and str[i+1] is 'y' and str[i+2] is 'z':
        return True
    if i is not 0:
      if str[i] is 'x' and str[i+1] is 'y' and str[i+2] is 'z' and str[i-1] is not '.':
        return True
  return False  