"""""def divide(x,y):
    try:
        return x/y
    except ZeroDivisionError as error:
        print(error)
        raise
"""""
def divide(x,y):
    if y ==0:
        raise ValueError("y não pode ser zero")
    return x/y

try:
    print(divide(2,0))
except ValueError as error:
    print("você está tentado dividor por 0.")
    print("log:", error)