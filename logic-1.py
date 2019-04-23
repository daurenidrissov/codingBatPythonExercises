def cigar_party(cigars, is_weekend):
  return is_weekend and cigars >= 40 or cigars >= 40 and cigars <=60

def date_fashion(you, date):
  if you < 3 or date < 3:
    return 0
  if you > 7 or date > 7:
    return 2
  return 1

def squirrel_play(temp, is_summer):
  return temp >= 60 and (not is_summer and temp <= 90 or is_summer and temp <= 100)

def caught_speeding(speed, is_birthday):
  if speed <= 60 and not is_birthday or speed <= 65 and is_birthday:
    return 0
  elif speed <= 80 and not is_birthday or speed <= 85 and is_birthday:
    return 1
  else:
    return 2

def sorta_sum(a, b):
  answer = a + b
  if answer >= 10 and answer < 20:
    answer = 20
  return answer

def alarm_clock(day, vacation):
  if vacation:
    if day == 0 or day == 6:
      return "off"
    else:
      return "10:00"
  else:
    if day == 0 or day == 6:
      return "10:00"
    else:
      return "7:00"
    
def love6(a, b):
  return a == 6 or b == 6 or a+b == 6 or abs(a-b) == 6

def in1to10(n, outside_mode):
  if outside_mode:
    if n <= 1 or n >= 10:
      return True
  else:
    if n >= 1 and n <= 10:
      return True
  return False

def near_ten(num):
  return (num % 10) <= 2 or (num % 10) >= 8
  