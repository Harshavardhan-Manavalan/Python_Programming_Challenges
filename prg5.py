"""
Question :
Count Vowels and Consonants
     Write a Python function called count_vowels_consonants that takes a string as input and returns the count of vowels and consonants separately.

Input Format: The input will be a string representing the 
sentence.

Output Format: The output will be two integers representing the count of vowels and consonants respectively.

Sample Input: "Hello World"

Sample Output: (3, 7)
"""
def count_vowels_consonants(sentence):
    vowels = 0
    consonants = 0

    # Convert the sentence to lowercase to make the comparison case-insensitive
    sentence = sentence.lower()

    # Define a set of vowels
    vowel_set = {'a', 'e', 'i', 'o', 'u'}

    # Iterate through each character in the sentence
    for char in sentence:
        # Check if the character is an alphabet
        if char.isalpha():
            # Check if the character is a vowel
            if char in vowel_set:
                vowels += 1
            else:
                consonants += 1

    return (vowels, consonants)


# Test the function
sentence = input("Enter a sentence: ")
result = count_vowels_consonants(sentence)
print("Count of vowels and consonants:", result)
