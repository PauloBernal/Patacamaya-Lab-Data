
def date(day, year):
  month = 0
  d = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
  if day in range(d[0], d[1]):
    month = 1
  elif day in range(d[1], d[2]):
    month = 2
  elif day in range(d[2], d[3]):
    month = 3
  elif day in range(d[3], d[4]):
    month = 4
  elif day in range(d[4], d[5]):
    month = 5
  elif day in range(d[5], d[6]):
    month = 6
  elif day in range(d[6], d[7]):
    month = 7
  elif day in range(d[7], d[8]):
    month = 8
  elif day in range(d[8], d[9]):
    month = 9
  elif day in range(d[9], d[10]):
    month = 10
  elif day in range(d[10], d[11]):
    month = 11
  elif day in range(d[11], d[12]):
    month = 12
  
  index = month - 1
  if index == 0:
    day = day
  else:
    day = day - d[index] + 1
  return day, month, year

