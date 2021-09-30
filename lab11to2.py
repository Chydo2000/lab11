def celToFah(degree):
    return round(degree * 1.8 + 32,1)

def fahToCel(degree):
    return round((degree - 32) / 1.8,1)
print(celToFah(10.0))
print(fahToCel(50.0))