import os

def add(a,b):
  return a + b
def substract(a,b):
  return a - b
def multiply(a,b):
  return a * b
def devide(a,b):
  return a / b

operations = {"+" : add , "-" : substract , "*" : multiply , "/" : devide}

def calc():
  first_num = float(input("What's the first number?: "))
  for op in operations:
    print(op)
  operation = input("Pick an operation: ")
  second_num = float(input("What's the next number?: "))
  calc_helper(first_num,second_num,operation)
  
def calc_helper(a,b,op):
  res = operations[op](a,b)
  print(f"{a} {op} {b} = {res}")
  cont = input(f"Type 'y' to continue calculating with {res}, type 'n' to start a new calculation, type 'x' to exit: ")
  if cont == "y":
    new_op = input("+\n-\n*\n/\nPick an operation: ")
    next_num = float(input("What's the next munber?: "))
    calc_helper(res,next_num,new_op)
  elif cont == "n":
    os.system("clear")
    calc()
  elif cont == "x":
    return
  

calc()
