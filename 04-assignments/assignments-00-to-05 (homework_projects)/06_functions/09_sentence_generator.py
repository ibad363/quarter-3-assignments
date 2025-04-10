def make_sentence(word:str, part_of_speech: int):
    if part_of_speech == 0:
        # noun
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        # verb
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        # adjective
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")

def main():
    word : str = input("Please type a noun, verb, or adjective: ")
    print("Is this a noun, verb, or adjective?")
    part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
    make_sentence(word,part_of_speech)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()