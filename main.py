import os
import json

data = {}

if os.path.isfile('./init') == False:
  with open('init', 'w') as m:
    print('Generating database file')
    print('')
    os.mkdir('./data')
    pass
  with open('./data/mth.json', 'w') as file:
    data['0'] = 0
    json.dump(data, file)
  with open('./data/phy.json', 'w') as file:
    data['0'] = 0
    json.dump(data, file)
  with open('./data/chm.json', 'w') as file:
    data['0'] = 0
    json.dump(data, file)
  with open('./data/bio.json', 'w') as file:
    data['0'] = 0
    json.dump(data, file)
  with open('./data/tha.json', 'w') as file:
    data['0'] = 0
    json.dump(data, file)
  with open('./data/eng.json', 'w') as file:
    data['0'] = 0
    json.dump(data, file)
else:
  print('Database found, skipping initialization')
  print('')


def insert(subj):
  while True:
    try:
      key = input('Key : ')
      ans = input('Answer : ')
      print('')
      with open(f'./data/{subj}.json', 'r') as file:
        data = json.load(file)
      data[f'{key}'] = ans
      with open(f'./data/{subj}.json', 'w') as file:
        json.dump(data, file)
    except:
      print('')
      print('Quit')
      break

def read(subj):
  while True:
    try:
      key = input('Key : ')
      with open(f'./data/{subj}.json', 'r') as file:
        data = json.load(file)
        try:
          res = data[f'{key}']
          print(res)
        except:
          print('Not founded')
          print('')
    except:
      print('')
      print('Quit')
      break

mode = input('Select mode (1 Write, 2 Read) : ')
print('')

if mode == '1':

  subj = input('Select subject (1 Math, 2 Physic, 3 Chemistery, 4 Biology, 5 Thai, 6 English) : ')
  print('')
  if subj == '1':
    insert('mth')
  elif subj == '2':
    insert('phy')
  elif subj == '3':
    insert('chm')
  elif subj == '4':
    insert('bio')
  elif subj == '5':
    insert('tha')
  elif subj == '6':
    insert('eng')
  else:
    print('Subject not found')

elif mode == '2':

  subj = input('Select subject (1 Math, 2 Physic, 3 Chemistery, 4 Biology, 5 Thai, 6 English) : ')
  if subj == '1':
    read('mth')
  elif subj == '2':
    read('phy')
  elif subj == '3':
    read('chm')
  elif subj == '4':
    read('bio')
  elif subj == '5':
    read('tha')
  elif subj == '6':
    read('eng')
  else:
    print('Subject not found')

else:
  print('Selected mode not found')