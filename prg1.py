"""Quwstion:
1. Reverse Words in a Sentence without reverse method,

This question focuses on reversing the order of words in a given sentence, demonstrating a developer’s proficiency with string manipulation, loops, conditionals, and other programming constructs.

Task: Write a Python function called reverse_words that takes a sentence as input and returns the sentence with the order of words reversed.

Input Format: The input will be a string representing the sentence.

Constraints

The sentence will contain only alphanumeric characters and spaces.
There will be no leading or trailing spaces.
The sentence will have at least one word.
Output Format: The output will be a string representing the sentence with the words reversed.

Sample Input: Python is awesome

Sample Output: awesome is Python"""



def reverse_words(a):
    if not a:
        return "Enter a sentence"

    # Check each word for alphanumeric characters
    for word in a.split():
        if not word.replace(' ', '').isalnum():
            return "Invalid characters found, please use alphanumeric characters only"

    split_input = a.split()
    reverse_input = split_input[::-1]
    joined_input = " ".join(reverse_input)

    return joined_input


# Test the function
input_sentence = input("Enter the sentence to reverse: ")
reversed_sentence = reverse_words(input_sentence)
print(reversed_sentence)


#another solution

"""def reverse_words (a):
    if not a:
        return "enter sentence"
    spliting_input = a.split()
    reversing_input = spliting_input[::-1]
    joining_input = " ".join(reversing_input)
    return joining_input

input_sentance = input("Enter the Reverse sentence: ")
reversed_input = reverse_words(input_sentance)
print(reversed_input)"""