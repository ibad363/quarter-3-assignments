def main():
    first_num = int(input("enter the first number."))
    second_num = input("enter the second number.")
    second_num: int = int(second_num)
    sum = first_num + second_num
    print(f"The Sum of {first_num} & {second_num} is {sum}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()