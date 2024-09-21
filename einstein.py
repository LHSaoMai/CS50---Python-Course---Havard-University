def main():
    mass=int(input("Please, provide a number for the mass: "))
    einstein(mass)

def einstein(m):
    E = m*(300000000**2)
    print(E)

main()
