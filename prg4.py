"""
Question:
Write a Python program that takes a string value as input, converts all uppercase 
letters to lowercase and all lowercase letters to uppercase, and then prints the modified string. 
Ensure that all other characters remain unchanged.                                                                                                                                                              [ Condition : should not use isupper() , islower()]                                                                                                                input:         tHE FIRST LABOUR DAY WAS CELEBRATED  IN iNDIA on mAY 1, 1923, IN cHENNAI.                                                                                                         
output: The first labour day was celebrated in India on May 1, 1923, in Chennai.

"""
def convert_case(string):
    converted_string = ""
    for char in string:
        # Check if the character is uppercase
        if char >= 'A' and char <= 'Z':
            converted_string += char.lower()
        # Check if the character is lowercase
        elif char >= 'a' and char <= 'z':
            converted_string += char.upper()
        else:
            converted_string += char
    return converted_string

def main():
    input_string = input("Enter a string: ")
    converted_string = convert_case(input_string)
    print("Converted string:", converted_string)

if __name__ == "__main__":
    main()
