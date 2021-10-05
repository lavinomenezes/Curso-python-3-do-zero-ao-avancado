def conv(v):
    try:
        v = int(v)
        return v
    except ValueError:
        try:
            v = float(v)
            return v
        except:
            pass


n = conv(input())
if n is not None:
    print(n * 5)
else:
    print("Isso não é numero")