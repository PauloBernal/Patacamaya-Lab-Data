import os
import re
import date as dt

data1 = os.listdir()
data2 = []
for file in data1:
  a = file.split('.')
  if a[-1].lower() == 'txt' and len(a) == 2:
    data2.append(a[0])
data2.sort()

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
  return f'{day}/{month}/{year}'

def compile(fname):
  with open(f'{fname}.TXT', 'r') as file:
    data = file.readlines()

  repeated = [data[0], data[2], data[3], data[4], data[5], data[6], data[7], data[40]]
  year = re.findall('\d\d\d\d', data[1])[0]
  day = 0
  data2 = [data[0], 'IIF LABORATORIO DE METEOROLOGIA\n', f'{data[2].rstrip()} ({year})', data[3], '\n', data[4], f'³  FECHA  {data[5]}', f'³       {data[6]}']
  for i in data:
    if i not in repeated:
      if 'IIF' not in i:
        if 'MED' not in i and 'VAR' not in i and 'V.MN' not in i and 'H.MN' not in i and 'V.MX' not in i and 'H.MX' not in i and 'AMP' not in i:
          if day < 10:
            data2.append(f'³   {date(day, year)} {i}')
          elif day < 100:
            data2.append(f'³ {date(day, year)} {i}')
          elif day < 1000:
            data2.append(f'³ {date(day, year)} {i}')
      else:
        day += 1
        data2.append(data[7])
  data2.append(data[7])
  with open(f'./compile/cmp_{fname}.TXT', 'w') as file2:
    file2.writelines(data2)
  print(f'File "{fname}.txt" successfully compiled!')
print(date(1, 2002))
for i in data2:
  compile(i)