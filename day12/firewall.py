firewall = [ 22, 80, 443, 25565, 5060, 5061, 123, 143 ]

def modTen(x):
    return x%10

print("Our list firewall looks like this:", firewall)

print("Our list when we apply sorted(firewall, key=modTen):", sorted(firewall, key=modTen))
