from tinydb import TinyDB, Query
from datetime import datetime
import uuid
db = TinyDB('db.json')
notes = Query()
now = datetime.now();
selected = ""

def newNote():
  print("introduce nueva nota: ")
  title = input("title: ")
  print(now)
  print(title)
  db.insert(
    {
      'title':  title,
      'date':   str(now),
      '_id':    str(uuid.uuid4())
    })
  return 1

def listing():
  # print(json.dumps(db.all(), separators=(',', ':')))
  print([r['title'] for r in db])
  return 1

def write():
  for r in db:
    f = open("./files/" + str(r['title']) +".md", "a")
    f.write(r['title'])
    f.close()

def menu():
  print("\nIntroduce un numero, 0 para salir")
  print("0. Salir \n1. nuevo\n2. list\n3. save")
  return input()

def main():
  while(True):
    selected = menu();
    if selected == "0":
      break
    if selected == "1":
      newNote()
    if selected == "2":
      listing()
    if selected == "3":
      write()

if __name__ == "__main__":
    main()



  


