time = 16*60 + 42

hour = time // 3600
rest = (time - 3600*hour)
min = rest // 60
rest = time - (3600*hour + 60*min)
seg = rest
print(f"{hour}:{min}:{seg}")