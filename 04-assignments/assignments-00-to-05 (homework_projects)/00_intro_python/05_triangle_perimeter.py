def main():
    # Get 3 side length of triangle
    side1 = float(input("What is the length of side 1?: "))
    side2 = float(input("What is the length of side 2?: "))
    side3 = float(input("What is the length of side 3?: "))

    # print the result
    print("The perimeter of the triangle is " + str((side1 + side2 + side3)))

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()