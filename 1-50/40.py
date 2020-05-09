dn = ''
d=1
while len(dn) < 1000001:
    dn += str(d)
    d += 1
print(int(dn[0])*int(dn[9])*int(dn[99])*int(dn[999])*int(dn[9999])*int(dn[99999])*int(dn[999999]))
