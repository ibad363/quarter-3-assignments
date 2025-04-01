C = 299792458 # speed of light in m/s

def main():
    mass_in_kg = float(input("Enter kilos of mass: "))

    # Calculate energy
    # equivalently energy = mass * (C ** 2)
    # using the ** operator to raise C to the power of 2
    energy_in_joules:float = mass_in_kg * (C ** 2)

    print("e = m * C^2...")
    print("m = " + str(mass_in_kg)+ "kg")
    print("C = " + str(C)+ " m/s")

    print(str(energy_in_joules) + " joules of energy!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()