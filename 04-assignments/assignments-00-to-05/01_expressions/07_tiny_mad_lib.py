SENTENCE_START = "Panaversity is fun. I learned to program and used Python to make my"

def main():
    adjective = input("Please type an adjective and press enter. ")
    noun = input("Please type a noun and press enter. ")
    verb = input("Please type a verb and press enter. ")
    
    print(f"{SENTENCE_START} {adjective} {noun} {verb}!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()