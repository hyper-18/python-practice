p = int(input("enter p:"))
r = int(input("enter r:"))
t = int(input("enter t:"))


def simple_interest(p, r, t):
    si = (p*r*t)/100
    print("simple interest=", si)


simple_interest(p, r, t)
