simpsons = [ ('Lisa', 8), ('Bart', 10), ('Maggie', 2), ('Homer', 36), ('Marge', 34) ]

def sortage(x):
    return x[1]

print("The results of sorted(simpsons, key sortage):", sorted(simpsons, key=sortage))


