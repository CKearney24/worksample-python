def run_loop():
  dict = {}
  while True:
    command = input("> ")
    execute = command.split()[0]
    if command.split().__len__() > 1:
      key = command.split()[1]
    else:
      key = ''
    if command.split().__len__() > 2:
      value = command.split()[2]
    else:
      value = ''
    if execute.upper() == "KEYS":
      print_keys(dict)
    elif execute.upper() == "MEMBERS":
      print_members(dict, key)
    elif execute.upper() == "ADD":
      add_key(dict, key, value)
    elif execute.upper() == "REMOVE":
      remove_value(dict, key, value)
    elif execute.upper() == "REMOVEALL":
      if key in dict.keys():
        dict.pop(key)
        print("Removed")
      else:
        print("ERROR, key does not exist")
    elif execute.upper() == "CLEAR":
      dict = {}
    elif execute.upper() == "KEYEXISTS":
      if dict != {} and key in dict.keys():
        print("true")
      else:
        print("false")
    elif execute.upper() == "MEMBEREXISTS":
      check_member(dict, key, value)
    elif execute.upper() =="ALLMEMBERS":
      if dict.keys():
        show_values(dict)
      else:
        print({})
    elif execute.upper() == "ITEMS":
      i = 0
      for key in dict.keys():
        for item in dict[key]:
          print(str(i) + ") " +key + ": "+item)
          i += 1


def show_values(dict):
  i = 0
  for key in dict.keys():
    for value in dict[key]:
      print(str(i) + ") " +value)
      i+=1

def print_members(dict, key):
  if key in dict.keys() and key:
    for item in dict[key]:
      print(item)
  else:
    print("key does not exist")
def add_key(dict, key, value):

  if key in dict.keys():
    dict[key].append(value)
  else:
    dict[key] = [value]
  print("added")

def print_keys(dict):
  for value in dict.keys():
    print(value)

def remove_value(dict, key, value):
  if key in dict.keys():
    dict[key].remove(value)
    if dict[key].__len__() == 0:
      dict.pop(key)
      print('Removed')
  else:
    print("ERROR, key does not exist")

def check_member(dict, key, value):
  if key in dict.keys() and value in dict[key]:
    print("true")
  else:
    print("false")
if __name__ == '__main__':
    run_loop()