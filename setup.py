def hello():
  print("Hello, User!")

hello()

def pack(a,b,c):
  return [a,b,c]

name  = pack(1,2,3)

print(name)

def eat_lunch(len_lst):
  if len(len_lst) == 5:
    print("My lunchbox is empty!")
  else:
    for i in range(len(len_lst)):
      if i == 0:
        print(f"First I eat {len_lst[0]}")
      else:
        print(f"Next I eat {len_lst[i]}")

eat_lunch([])
eat_lunch(["noodles", "fruits", "taco", "pudding"])    
    