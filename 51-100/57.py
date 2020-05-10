from fractions import Fraction

count = 0

root = Fraction(3,2)
for i in range(1,1000):
    next_denominator = root.numerator+root.denominator
    root = Fraction(next_denominator+root.denominator,next_denominator)

    if len(str(root.numerator)) > len(str(root.denominator)):
        count += 1
print(count)





