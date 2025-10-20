from calculator import Calculator

def main():
    calc = Calculator()
    print("Calculator Demo:")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    
if __name__ == "__main__":
    main()
