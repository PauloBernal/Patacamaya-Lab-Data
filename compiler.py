import os
import re

data1 = os.listdir()
data2 = []
for file in data1:
  a = file.split('.')
  if a[-1].lower() == 'txt' and len(a) == 2:
    data2.append(a[0])
data2.sort()

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
            data2.append(f'³     {day} {i}')
          elif day < 100:
            data2.append(f'³    {day} {i}')
          elif day < 1000:
            data2.append(f'³   {day} {i}')
      else:
        day += 1
        data2.append(data[7])
  data2.append(data[7])
  with open(f'./compile/cmp_{fname}.TXT', 'w') as file2:
    file2.writelines(data2)
  print(f'File "{fname}.txt" successfully compiled!')

for i in data2:
  compile(i)