dict  = {1:1, 2:2}

for key, value in dict.items():
    print(value, end='-')
    value += 3
    print(value)