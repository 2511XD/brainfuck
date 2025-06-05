#
#made by 2511XD
#!usage in terminal :: python converter.py ,then it will ask for text to convert it
#
def text_to_brainfuck(text):
    bf_code = ""
    current = 0

    for char in text:
        target = ord(char)
        diff = target - current

        # Adjust memory cell to match target ASCII value
        if diff > 0:
            bf_code += '+' * diff
        elif diff < 0:
            bf_code += '-' * (-diff)

        bf_code += '.'  # Print character
        current = target

    return bf_code

# Example usage:
# !another example
# #
if __name__ == "__main__":
    input_text = input("Enter your text: ")
    bf_output = text_to_brainfuck(input_text)
    print("\nGenerated Brainfuck code:\n")
    print(bf_output)