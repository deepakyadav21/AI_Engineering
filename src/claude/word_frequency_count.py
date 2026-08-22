# This program counts how many times a given word appears in a sentence
import string


def count_word_occurrences(sentence, target_word):
    words = sentence.lower().split()
    target_word = target_word.lower().strip(string.punctuation)
    count = 0
    for word in words:
        cleaned_word = word.strip(string.punctuation)
        if cleaned_word == target_word:
            count += 1
    return count


sentence = input("Enter the sentence: ")
word = input("Enter the word to count: ")

print(
    "The given word appears",
    count_word_occurrences(sentence, word),
    "times in the sentence.",
)
