def teste(X):
    if X%2 == 0:
        return print("fizz")
    elif X%5 == 0:
        if X%3 ==0:
            return print("Fizzbuzz")
        else:
            return print("buzz")
    else:
        return print(X)
X = int(input())
teste(X)