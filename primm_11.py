"""
PRIMM: 1+1 = 11
Description of program here
Name - Date
"""

def main():
      #prompt users for numbers
    num1: float = float(input("Enter a number: "))
    num2: float = float(input("Enter another number: "))
      #add numbers together
    total: float = num1+num2

      #output
    print(f"{num1} + {num2} = {total}")
    print(f"{num1} - {num2} = {num1-num2}")
    print(f"{num1} * {num2} = {num1*num2}")
    print(f"{num1} ** {num2} = {num1**num2}")
    print(f"{num1} / {num2} = {num1/num2}")
    print(f"{num1} // {num2} = {num1//num2}")
    print(f"{num1} % {num2} = {num1%num2}")
if __name__ == "__main__":
  main()
