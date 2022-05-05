from art import logo
print(logo)
def add(a,b):
  return a+b 

def sub(a,b):
  return a-b 

def multiply(a,b):
  return a*b

def division(a,b):
  return a/b 

def polynomial(a):
  for numbers in range(1,a):
    multiply(numbers)

signs = {
       "+": add,
       "-": sub,
       "*": multiply,
       "/": division,
  "!": polynomial
}

def t_calculator():
  a = float(input("What's the number?\n:"))
  for key in signs:
    print(key)
  more_calculation = True
  
  while more_calculation:
    user_input = input("What operational sign?\n:")
    operational_sign = signs[user_input]
    b = float(input("What's your next number?\n:"))
    answer = (operational_sign(a,b))
    print (f"The answer is {answer}")

    more = input(f"Do you want to continue calculation with {answer}, or type 'n' to start a new calculation (Y/N)").lower()
    if more == "y":
      a = answer
    elif more == "n":
      more_calculation = False
      t_calculator()
    else:
      print("error")

t_calculator()