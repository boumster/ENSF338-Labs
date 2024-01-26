import re

def count_consonants(text):
    words = re.findall(r'\b\w+\b', text)
    total_consonants = 0
    total_words = 0

    for word in words:
        consonants = sum(1 for letter in word if letter.lower() not in ['a', 'e', 'i', 'o', 'u', 'y'])
        total_consonants += consonants
        total_words += 1

    average_consonants = total_consonants / total_words if total_words > 0 else 0
    return average_consonants

with open('textfile.txt', 'r') as file:
    text = file.read()

# Find the start of Chapter 1
start = text.find('CHAPTER 1')

# If Chapter 1 is found, start reading from there
if start != -1:
    text = text[start:]

average_consonants = count_consonants(text)
print(f"Average number of consonants per word: {average_consonants}")
