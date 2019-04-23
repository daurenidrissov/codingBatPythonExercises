def count_evens(nums):
  count = 0
  for i in nums:
    if i%2 is 0:
      count += 1
  return count

def big_diff(nums):
  maximum = -999
  minimum = 999
  for i in range(len(nums)):
    maximum = max(nums[i], maximum)
    minimum = min(nums[i], minimum)
  return maximum - minimum

def centered_average(nums):
  maximum = -999
  minimum = 999
  avrg = 0
  for i in range(len(nums)):
    maximum = max(nums[i], maximum)
    minimum = min(nums[i], minimum)
    avrg += nums[i]
  avrg -= maximum + minimum
  avrg /= len(nums) - 2
  return avrg

def sum13(nums):
  summ = 0
  for i in range(len(nums)):
    if nums[i] is 13:
      nums[i] = 0
      if i < len(nums)-1:
        nums[i+1] = 0
    summ += nums[i]
  return summ

def sum67(nums):
  summ = 0
  tick = False
  for i in nums:
    if i is 6:
      tick = True
    if not tick:
      summ += i
    if i is 7 and tick:
      tick = False
  return summ

def has22(nums):
  for i in range(len(nums)-1):
    if nums[i] is 2 and nums[i+1] is 2:
      return True
  return False
