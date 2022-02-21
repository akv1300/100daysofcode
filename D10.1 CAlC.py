def calculator():
    n1 = float(input("Enter 1st number\n"))
    sigma = True
    while sigma:
        def add(n1,n2):
            return n1 + n2
        def substract(n1,n2):
            return n1 - n2
        def divide(n1,n2):
            return n1 / n2
        def multiply(n1,n2):
            return n1 * n2
        operators = {"+" :  add, "-" : substract, "/" : divide, "*" :multiply}
        for i in operators:
            print(i)
        operator = input("Select one of the operators from above \n")
        n2 = float(input("Enter next   number\n"))
        for i in operators:
            if i == operator:
                ans = operators[i](n1,n2)
        print(f"{n1} {operator} {n2} = {ans}")
        sigma = int(input(f"Do you want to continue with {ans} or start a new one, press 0 or 1 \n"))
        n1 = ans
        if sigma == 0:
            calculator()
calculator()